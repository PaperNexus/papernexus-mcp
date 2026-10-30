# Listing copy

Text to paste into directory submission forms. Keep it in step with the
README.

## Name

Paper Nexus

## Server URL

https://papernex.us/mcp (Streamable HTTP, OAuth 2.1)

## Tagline (100 characters or fewer)

Find related scientific papers through their citation network, from OpenAlex and Semantic Scholar.

## Short description (about 200 characters)

Search the scholarly literature and find related papers through their
citation network: recommendations from one or more papers, a paper's key
references and citing papers, and your library.

## Long description

Paper Nexus maps the scientific literature by its citations, using the
scholarly works in OpenAlex and Semantic Scholar. Connect it to your
assistant to:

- **Find a paper** by its title, a DOI, or a link to arXiv, PubMed, doi.org or a
  publisher's page.
- **Get related papers** from one paper or several. Related means connected in
  the citation network (cited alongside, citing the same work), not similar
  wording, so it finds the papers a field builds on even when they use
  different words. Several papers together put the work related to more than
  one of them first.
- **Read a paper's details** and its most-cited references, and see the
  papers that cite it.
- **See why each paper is recommended**: which of your papers it is linked
  to, and whether it cites them or they cite it.
- **Narrow recommendations and citing papers with filters** (Premium): years,
  citation counts, authors, venues, title words, citing or cited papers, open
  access and document types.
- **Browse your Paper Nexus library**, if you allow it, and find what your
  collections are missing.

Every paper links to papernex.us, and every set of recommendations comes with
a link that opens the whole citation graph there. Sign in with a free Paper
Nexus account: 10 counted calls a week (recommendations and citing-paper
lists), no API key. Premium has 200 a day, up to 10 papers per request, and
filters.

## Example prompts

For forms that ask for example prompts or use cases. Each works on a free
account except the fourth, which uses filters (Premium).

1. **Find papers related to "Attention Is All You Need" and tell me which to
   read first.** Searches for the paper, then lists related work, most related
   first, each with the citation links behind it and a link to the full graph.
2. **Who wrote "Mastering the game of Go with deep neural networks and tree
   search", how often is it cited, and what are its most cited references?**
   Reads the paper's details and its key references in one lookup.
3. **What should I read next after the ResNet paper
   (https://arxiv.org/abs/1512.03385)?** Finds a paper from a link, then
   recommends from it.
4. **Which papers from 2024 on build on "Denoising Diffusion Probabilistic
   Models"? Give me the ten closest.** Recommendations narrowed to papers
   that cite it, from 2024 on.
5. **Look at my Paper Nexus library and suggest papers my "Thesis" collection
   is missing.** Reads a collection (with the library permission) and
   recommends from the papers in it.

## Categories

Research, Education, Science, Productivity (choose whichever the directory offers)

## Keywords / tags

research, academic, scientific papers, citations, literature review,
bibliography, science, OpenAlex, Semantic Scholar, citation graph

## Links

- Website: https://papernex.us
- Documentation: https://github.com/PaperNexus/papernexus-mcp#readme
- Support: https://github.com/PaperNexus/papernexus-mcp/issues and info@papernex.us
- Privacy policy: https://papernex.us/privacy
- Terms of service: https://papernex.us/terms
- Pricing: https://papernex.us/pricing
- Logo: `assets/logo.png` (512 × 512 PNG), `assets/logo.svg`

## Authentication

OAuth 2.1 with PKCE. Discovery through
`https://papernex.us/.well-known/oauth-protected-resource/mcp` and
`https://papernex.us/.well-known/oauth-authorization-server`. Clients may use a
Client ID Metadata Document or dynamic client registration. Scopes:
`papers:read` (always granted) and `library:read` (optional, shown separately
on the consent page).

## Tool annotations

Every tool is marked `readOnlyHint: true`, `destructiveHint: false`,
`idempotentHint: true`, `openWorldHint: false`, and every tool has a title.
