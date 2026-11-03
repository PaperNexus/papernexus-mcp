---
name: find-related-papers
description: Find scientific papers related to ones the user names, through their citation network, with the Paper Nexus tools. Use for literature reviews, "what else should I read", finding work that builds on a paper, or checking a paper's references and citing papers.
---

# Find related papers with Paper Nexus

Paper Nexus finds related papers through the citation network of the
scholarly works in OpenAlex and Semantic Scholar. Related means cited alongside the
origins or citing the same work, not "similar text". That makes it good at finding the papers a field actually
builds on, including ones that use different words for the same idea.

## Workflow

1. **Find the paper's id.** Call `search_papers` with the title (or part of
   it), a DOI, or a link to the paper (doi.org, arXiv, PubMed, a publisher
   page). Pick the result whose title, year and authors match what the user
   means. If `closest_matches` is true, nothing matched every word: check the
   titles before going on, and ask the user when two or more could be the one.
2. **Get recommendations.** Call `recommend_papers` with one or more ids.
   Several origins merge their related papers, with papers related to more
   than one of them first. Origins from unrelated fields give a mix of each
   field's papers, not papers bridging them. Pass the user's constraints in
   `filters` (years, citation counts, authors, venues, title words, citing or
   cited papers, open access, document types) instead of filtering the
   results yourself: the search goes deeper to fill the list. For "papers
   that connect X and Y", pass X and Y as `cites` with `cites_match: "all"`;
   for one topic among a paper's citing papers, pair `cites` with `title`.
   For a paper with more than 1,000 citing papers, `cites` checks only papers
   near the origins, and the result's first line says so: then tell the user
   the list may miss recent or narrow-topic work, rather than presenting an
   empty or short list as the whole answer.
   For "the work that builds on X", pass X as the origin and as `cites`: the
   papers citing X, closest to it first.
   Each recommendation's `evidence` says which origins it is linked to
   (`linked_origins`), whether it cites them or they cite it, and how many
   co-citations and shared references link it (`link_counts`). Use it to say
   why a paper is there, and with several origins, which one it belongs to;
   rank a paper held up by one or two links below one with many.
   A paper with `citation_linked: false` ("no citation link") was added from
   OpenAlex's related works to fill the list, so treat it as a weaker lead.
3. **Go deeper where it helps.** `get_paper` gives one paper's details,
   including its DOI and arXiv id, and its most-cited references (where a
   paper comes from). `list_citing_papers`
   lists the papers citing it, newest or most cited first (where
   a paper went next), and takes the same `filters` (years are `year_from`
   and `year_to`) to list only the citing papers by an author, in a venue or
   with a word in the title. Most cited first is led by famous papers that
   cite it in passing, so for the citers that matter, prefer step 2's `cites`
   filter.
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
- **Premium:** 200 counted calls a day and up to 10 origin papers.
- **Filters** work on every account, and a filtered call counts like any other.
- **Lookups:** the other tools share 100 calls a day (free) or 1,000
  (Premium), and every tool a limit of 30 calls a minute, so don't loop over
  `get_paper` for a long list when `fields` on one listing gives what you need.

So search and confirm the right paper before recommending, rather than
recommending from a guess. A call that fails or finds nothing isn't counted.
When a limit is reached, the tool says so and when it resets; tell the user
rather than retrying.

## Don'ts

- Don't invent Paper Nexus ids, titles or citation counts; use what the tools
  return.
- Don't present the results as a complete bibliography. They are the papers
  most connected to the origins in the citation network, most related
  first.
- Don't present the order as a relevance score or a measure of importance. It
  orders one list by citation linkage and, without filters, lifts recent
  papers and damps very highly cited ones.
- Paper Nexus has metadata, not full text. For a paper's content, link to it.
