# Listing copy

Text to paste into directory submission forms. Keep it in step with the
README.

## Name

Paper Nexus

## Server URL

https://papernex.us/mcp (Streamable HTTP, OAuth 2.1)

## Tagline (100 characters or fewer)

Find related scientific papers through the citation network of 225 million scholarly works.

## Short description (about 200 characters)

Search 225 million scholarly works and find related papers through their
citation network. Recommendations from one or more papers, a paper's key
references, and your Paper Nexus library.

## Long description

Paper Nexus maps the scientific literature by its citations, using 225 million
scholarly works from OpenAlex and Semantic Scholar. Connect it to your
assistant to:

- **Find a paper** by its title, a DOI, or a link to arXiv, PubMed, doi.org or a
  publisher's page.
- **Get related papers** from one paper or several. Related means connected in
  the citation network (cited alongside, citing the same work), not similar
  wording, so it finds the papers a field builds on even when they use
  different words. Several papers together find the work that connects them.
- **Read a paper's details** and its most-cited references.
- **Browse your Paper Nexus library**, if you allow it, and find what your
  collections are missing.

Every paper links to papernex.us, and every set of recommendations comes with
a link that opens the whole citation graph there. Sign in with a free Paper
Nexus account: 10 recommendations a week, no API key. Premium has 200 a day,
up to 10 papers per request, and filters.

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
