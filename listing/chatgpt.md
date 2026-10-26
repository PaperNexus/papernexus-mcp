# ChatGPT / Codex plugin submission

For the "With MCP" plugin submission. The server URL is
`https://papernex.us/mcp`; the portal reads the tools and their annotations
from it.

## Starter prompts

- Find papers related to "Attention Is All You Need".
- What should I read next after the ResNet paper (arXiv 1512.03385)?
- Which papers connect "Deep learning" (LeCun, Bengio, Hinton 2015) and "Mastering the game of Go with deep neural networks and tree search"?
- Show me the main references of the AlphaFold 2 paper.

## Positive test cases

Each should call the tools named and answer with papernex.us links.

1. **"Find papers related to Attention Is All You Need."**
   `search_papers` finds the 2017 paper; `recommend_papers` with its id returns
   related papers, most related first (attention and neural machine translation
   work such as Bahdanau et al. and "Sequence to Sequence Learning"), with
   papernex.us links and a graph link.
2. **"Who wrote the paper at https://doi.org/10.1038/s41586-021-03819-2, how often is it cited, and what are its most cited references?"**
   `search_papers` with the link finds "Highly accurate protein structure
   prediction with AlphaFold" (Nature, 2021); `get_paper` returns its authors,
   citation count and top references (ResNet, "Attention Is All You Need" and
   BERT among them).
3. **"Recommend papers related to both 'Deep learning' by LeCun, Bengio and Hinton (2015) and 'Mastering the game of Go with deep neural networks and tree search'."**
   Two `search_papers` calls, then one `recommend_papers` call with both ids;
   the answer describes papers related to both.
4. **"Search for papers titled 'protein structure prediction' and tell me which is most cited."**
   `search_papers` returns several matches with ids and years; the assistant
   may use `get_paper` to compare citation counts.
5. **"Give me 5 papers to read around doi:10.1038/nature14539, with links."**
   `search_papers` with the DOI finds "Deep learning" (Nature, 2015);
   `recommend_papers` with `limit` 5 returns five papers with papernex.us links.

## Negative test cases

The tools should not be called.

1. **"What's the weather in Paris tomorrow?"** Nothing to do with papers.
2. **"Write me a 500-word essay on the causes of World War I."** A writing task;
   it names no paper and asks for no literature.
3. **"Give me the full text of the AlphaFold 2 paper."** Paper Nexus has
   metadata, not full text; the assistant may find the paper and link to it,
   but must not present tool output as the paper's text.

## Reviewer access

Create a dedicated Paper Nexus account for the reviewer, sign in with an email
and password (no MFA, no Google sign-in), and set it to Premium so the
allowance doesn't run out mid-review. Enter its credentials in the portal
only, never in this repository.

## Release notes (1.0.0)

First release: search papers by title, DOI or link; recommendations from one
or more papers through the citation network; a paper's details and most-cited
references; the papers citing a paper; filters on recommendations for
Premium accounts; your remaining allowance; and read-only access to your Paper Nexus
library. Every tool that lists papers can return only the fields asked for.
