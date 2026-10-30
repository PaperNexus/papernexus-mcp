# ChatGPT / Codex plugin submission

For the "With MCP" plugin submission. The server URL is
`https://papernex.us/mcp`; the portal reads the tools and their annotations
from it.

OpenAI's guidelines forbid advertising pricing, plans or upgrades, in the
listing and in tool output. The server's tool results never mention them, so
keep this copy free of them too: use the description below, not the one in
[descriptions.md](descriptions.md), which names the allowances.

## Description

Paper Nexus maps the scientific literature by its citations, using the
scholarly works in OpenAlex and Semantic Scholar. Find a paper by its title,
a DOI or a link; get the papers related to one paper or several through the
citation network, each with the links that put it there; read a paper's
details and most-cited references; see the papers that cite it; narrow
recommendations and citing papers with filters (years, citations, authors,
venues, title words, citing or cited papers, open access); and browse your
Paper Nexus library, if you allow it. Every paper links to papernex.us, and
every set of recommendations comes with a link to the whole citation graph.
Sign in with your Paper Nexus account.

## Starter prompts

- Find papers related to "Attention Is All You Need".
- What should I read next after the ResNet paper (arXiv 1512.03385)?
- Find papers related to both "Deep learning" (LeCun, Bengio, Hinton 2015) and "Mastering the game of Go with deep neural networks and tree search"?
- Show me the main references of the AlphaGo paper ("Mastering the game of Go with deep neural networks and tree search").

## Positive test cases

Each should call the tools named and answer with papernex.us links.

1. **"Find papers related to Attention Is All You Need."**
   `search_papers` finds the 2017 paper; `recommend_papers` with its id returns
   related papers, most related first (attention and neural machine translation
   work such as Bahdanau et al. and "Sequence to Sequence Learning"), with
   papernex.us links and a graph link.
2. **"Who wrote the paper at https://doi.org/10.1038/nature16961, how often is it cited, and what are its most cited references?"**
   `search_papers` with the link finds "Mastering the game of Go with deep
   neural networks and tree search" (Nature, 2016); `get_paper` returns its
   authors (David Silver first), citation count and top references
   (AlexNet's "ImageNet classification with deep convolutional neural
   networks", Sutton and Barto's "Reinforcement Learning: An Introduction" and
   DQN's "Human-level control through deep reinforcement learning" among
   them).
3. **"Recommend papers related to both 'Deep learning' by LeCun, Bengio and Hinton (2015) and 'Mastering the game of Go with deep neural networks and tree search'."**
   Two `search_papers` calls, then one `recommend_papers` call with both ids;
   the answer describes the related papers, those related to both first.
4. **"Search for papers titled 'protein structure prediction' and tell me which is most cited."**
   `search_papers` returns several matches with ids, years and citation
   counts; the assistant names the most cited without further calls.
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
or more papers through the citation network, each with the citation links
behind it; a paper's details and most-cited references; the papers citing a
paper; filters on recommendations and citing papers; your remaining allowance; and read-only access to your Paper Nexus library. Every
tool that lists papers can return only the fields asked for.
