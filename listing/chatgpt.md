# ChatGPT plugin submission

ChatGPT and Codex list MCP-backed plugins in one directory. The submission is
a ZIP uploaded at [platform.openai.com/plugins](https://platform.openai.com/plugins);
OpenAI's steps are in
[Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission).

The package is [`chatgpt/`](../chatgpt): `plugin.json` holds the listing copy,
the starter prompts, the five positive and three negative review cases and
the release notes; `mcp.json` names the server and its OAuth. Edit them
there, not here. Build the ZIP with:

```sh
scripts/build-chatgpt-zip.sh   # writes dist/papernexus-chatgpt-<version>.zip
```

CI checks the listing against the directory's limits
(`scripts/check-chatgpt-listing.py`): 30 characters for the name and the
subtitle, at most three starter prompts of 128 characters, exactly five
positive and three negative cases.

OpenAI's guidelines forbid advertising pricing, plans or upgrades, in the
listing and in tool output. The server's tool results never mention them, so
keep the listing free of them too; don't paste the copy from
[descriptions.md](descriptions.md), which names the allowances.

## Not in the ZIP

- **Demo video.** `review.demo_recording_url` is left out of `plugin.json` so
  it can be entered in the portal. A field the ZIP sets is read-only there.
- **Reviewer access.** Enter it under Metadata & Skills → Review information →
  Review details. The ZIP rejects `test_credentials` and
  `reviewer_instructions`. Use the dedicated reviewer account: email and
  password, no MFA and no Google sign-in, set to Premium so the allowance
  doesn't run out mid-review. Its credentials never go in this repository.
- **Domain verification.** After the upload, MCPs → Connect shows a token.
  papernex.us serves it at `/.well-known/openai-apps-challenge` once it is set
  as `mcp_openai_apps_challenge` in the server's production config and
  deployed.

## Review cases

Run each one with the reviewer account before submitting, and check that the
papers named in each `expected_behavior` still come back near the top.
