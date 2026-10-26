---
name: find-related-papers
description: Find scientific papers related to ones the user names, through their citation network, with the Paper Nexus tools. Use for literature reviews, "what else should I read", finding work that builds on a paper, or checking a paper's references and citing papers.
---

# Find related papers with Paper Nexus

Paper Nexus finds related papers through the citation network of 225 million
scholarly works (OpenAlex and Semantic Scholar). Related means cited alongside the
origins or citing the same work, not "similar text". That makes it good at finding the papers a field actually
builds on, including ones that use different words for the same idea.

## Workflow

1. **Find the paper's id.** Call `search_papers` with the title (or part of
   it), a DOI, or a link to the paper (doi.org, arXiv, PubMed, a publisher
   page). Pick the result whose title, year and authors match what the user
   means. If `closest_matches` is true, nothing matched every word: check the
   titles before going on, and ask the user when two or more could be the one.
2. **Get recommendations.** Call `recommend_papers` with one or more ids.
   Several origins find papers related to all of them, which is the way to
   bring two lines of work together ("papers that connect X and Y"). Pass the
   user's constraints in `filters` (years, citation counts, authors, venues,
   open access, document types) instead of filtering the results yourself:
   the search goes deeper to fill the list. Filters are a Premium feature; on
   a free account the tool says so.
3. **Go deeper where it helps.** `get_paper` gives one paper's details and its
   most-cited references (where a paper comes from). `list_citing_papers`
   lists the papers citing it, newest or most cited first (where
   a paper went next).
4. **Answer with links.** Every paper in a result has a papernex.us `url`; give
   it beside each paper you mention, and give `graph_url` so the user can open
   the whole graph in Paper Nexus and explore it visually.

When you only need some details of each paper, say titles and years to scan
a long list, pass `fields`: the result stays short,
and every paper still carries its id for the next call.

If the user allowed library access when connecting (`list_library` is
listed), their collections are a good source of origin papers: "find what I'm
missing for my thesis chapter" means list that collection, then recommend from
its papers.

## Allowance

`recommend_papers` and `list_citing_papers` count against the account's
allowance; the other tools don't. Before a task that needs many counted calls,
such as recommending from every paper in a collection, call `get_usage` to see
how many are left and plan within them.

- **Free accounts:** 10 counted calls a week, and up to 2 origin papers per
  recommendation.
- **Premium:** 200 counted calls a day, up to 10 origin papers, and filters.
- **Lookups:** the other tools share 100 calls a day (free) or 1,000
  (Premium), and every tool a limit of 30 calls a minute, so don't loop over
  `get_paper` for a long list when `fields` on one listing gives what you need.

So search and confirm the right paper before recommending, rather than
recommending from a guess. A call that fails or finds nothing isn't counted.
When a limit is reached, the tool says so and when it resets, and a free
account also gets the upgrade link; pass that on rather than retrying.

## Don'ts

- Don't invent Paper Nexus ids, titles or citation counts; use what the tools
  return.
- Don't present the results as a complete bibliography. They are the papers
  most connected to the origins in the citation network, most related
  first.
- Paper Nexus has metadata, not full text. For a paper's content, link to it.
