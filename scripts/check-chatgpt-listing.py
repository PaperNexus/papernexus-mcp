"""
Checks chatgpt/plugin.json against the limits the ChatGPT plugin directory
applies at final submission, which a ZIP upload alone does not enforce:
https://developers.openai.com/plugins/deploy/submission#manifest-fields
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATEGORIES = {
    'Productivity', 'Creativity', 'Developer Tools', 'Business & Operations', 'Data & Analytics',
    'Communication', 'Education & Research', 'Security', 'Finance', 'Healthcare', 'Travel',
    'Entertainment', 'Other',
}
LISTING_URLS = ('websiteURL', 'supportURL', 'privacyPolicyURL', 'termsOfServiceURL')

manifest = json.loads((ROOT / 'chatgpt' / 'plugin.json').read_text())
openai = manifest['extensions']['com.openai']
listing = openai['interface']
cases = openai['review']['test_cases']
problems = []


def at_most(field, value, limit):
    if len(value) > limit:
        problems.append(f'{field} is {len(value)} characters, over {limit}: {value!r}')


at_most('description', manifest['description'], 1024)
at_most('displayName', listing['displayName'], 30)
at_most('shortDescription', listing['shortDescription'], 30)
at_most('longDescription', listing['longDescription'], 4000)
at_most('developerName', listing['developerName'], 80)
if listing['category'] not in CATEGORIES:
    problems.append(f'category {listing["category"]!r} is not one of the directory\'s')
if len(listing['capabilities']) > 20:
    problems.append('more than 20 capabilities')
for capability in listing['capabilities']:
    at_most('capability', capability, 120)
prompts = listing.get('defaultPrompt', [])
if len(prompts) > 3:
    problems.append(f'{len(prompts)} starter prompts, over 3')
for prompt in prompts:
    at_most('defaultPrompt', prompt, 128)
for field in LISTING_URLS:
    if not listing.get(field, '').startswith('https://'):
        problems.append(f'{field} must be an HTTPS URL')
for field in ('logo', 'composerIcon'):
    if not (ROOT / 'chatgpt' / listing[field]).is_file():
        problems.append(f'{field} {listing[field]} is not in chatgpt/')
if len(cases['positive']) != 5 or len(cases['negative']) != 3:
    problems.append(f'review needs exactly 5 positive and 3 negative cases, '
                    f'not {len(cases["positive"])} and {len(cases["negative"])}')
for case in cases['positive']:
    missing = [k for k in ('description', 'prompt', 'tools_triggered', 'expected_behavior') if not case.get(k)]
    if missing:
        problems.append(f'positive case {case.get("prompt")!r} lacks {missing}')
for case in cases['negative']:
    if not case.get('description') or not case.get('prompt'):
        problems.append(f'negative case {case.get("prompt")!r} lacks a description or prompt')
for forbidden in ('test_credentials', 'reviewer_instructions'):
    if forbidden in openai['review']:
        problems.append(f'review.{forbidden} must be entered in the portal, not the ZIP')

if problems:
    sys.exit('\n'.join(problems))
print('chatgpt/plugin.json fits the directory limits')
