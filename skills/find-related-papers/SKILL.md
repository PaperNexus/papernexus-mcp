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
   bring two lines of work together ("papers that connect X and Y"). If the
   tool offers `filters` (years, citation counts, authors, venues, open
   access, document types), pass the user's constraints there instead of
   filtering the results yourself: the search goes deeper to fill the list.
3. **Go deeper where it helps.** `get_paper` gives one paper's details and its
   most-cited references (where a paper comes from). `list_citing_papers`,
   where offered, lists the papers citing it, newest or most cited first (where
   a paper went next).
4. **Answer with links.** Every paper in a result has a papernex.us `url`; give
   it beside each paper you mention, and give `graph_url` so the user can open
   the whole graph in Paper Nexus and explore it visually.

If the user has connected their library (`list_library` is offered), their
collections are a good source of origin papers: "find what I'm missing for my
thesis chapter" means list that collection, then recommend from its papers.

## Allowance

`recommend_papers` and `list_citing_papers` count against the account's
allowance; `search_papers`, `get_paper` and `list_library` don't.

- **Free accounts:** 10 counted calls a week, and up to 2 origin papers per
  recommendation.
- **Premium:** 200 counted calls a day, up to 10 origin papers, and filters
  where the tool offers them.

So search and confirm the right paper before recommending, rather than
recommending from a guess. A call that fails or finds nothing isn't counted.
When a limit is reached, the tool says so and gives the upgrade link; pass it
on rather than retrying.

## Don'ts

- Don't invent Paper Nexus ids, titles or citation counts; use what the tools
  return.
- Don't present the results as a complete bibliography. They are the papers
  most connected to the origins in the citation network, most related
  first.
- Paper Nexus has metadata, not full text. For a paper's content, link to it.
