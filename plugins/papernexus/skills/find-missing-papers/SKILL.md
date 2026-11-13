---
name: find-missing-papers
description: Find the papers a reference list, draft, reading list or library collection is missing, with the Paper Nexus tools - work closely tied by citations to the papers already there but not among them. Use for "what am I missing", "is my related work complete", gap checks on a thesis chapter, review or grant bibliography, or keeping a Paper Nexus collection up to date.
---

# Find what a reference list is missing

Given the papers someone already has, Paper Nexus can find the ones most tied
to them through citations: cited alongside them, or citing the same work. The
ones not already in the list are the candidates for what is missing. This is
a different job from recommending from one paper: there are many starting
papers and only a few counted calls, so choosing the origins is most of the
work.

## Workflow

1. **Get the list and resolve it.** From a draft or bibliography, call
   `search_papers` with the references as `queries` (up to 20 per call);
   references with a DOI, arXiv id or PMID need no search. From the user's
   library, call `list_library` with the collection (offered only when
   library access was allowed; it lists the papers directly in a collection,
   not its subcollections). Keep every resolved id: that is the "already
   have" set. Say which references Paper Nexus doesn't have, since they can't
   be origins and can't be recognised in results.
2. **Check the budget.** Call `get_usage`. `recommend_papers` is counted (10
   calls a week on a free account, 200 a day on Premium) and takes up to 2
   origins per call on a free account, 10 on Premium. Plan the calls before
   making any, and tell the user the plan when it uses most of what is left.
3. **Choose origins by topic, not by fame.** Group the list into its themes
   (the chapter's sections, or the clusters you can see in titles and
   venues) and make one call per theme with that theme's most central
   papers as origins. Don't mix themes in one call: origins from unrelated
   fields give a mix of each field's papers. Prefer specific, on-topic
   papers over famous background ones, whose neighbourhoods are broad.
   Ask the user which themes matter most when the budget can't cover all.
4. **Recommend, with the user's constraints as `filters`.** "Recent work I
   missed" is `year_min`; "the classics" is `min_citations`; reviews are
   `types: ["review"]`. Ask for `limit` 50 when most results will be papers
   already in the list, and `fields` of `id`, `title`, `authors`, `year`,
   `cited_by_count`, `url` and `evidence` to keep long results short.
5. **Remove what they already have.** Drop every result whose id is in the
   "already have" set, and treat a result with the same title and first
   author as one of theirs too (a preprint and its published version are
   often separate records). What is left are the candidates.
6. **Rank the candidates by evidence.** Put first the papers that came back
   for several themes or are linked to several origins (`linked_origins`),
   and those with many co-citations and shared references (`link_counts`).
   A paper with `citation_linked: false` was added to fill the list: a weak
   lead. For the few strongest candidates, `get_paper` (several at once as
   `papers`) gives the subject, keywords and one-sentence summary to say what
   each is about.
7. **Answer by theme.** For each theme: the origins you used, then the
   missing candidates with year, a line on why each is there (which of their
   papers it is tied to, from the evidence), and its papernex.us `url`. Give
   each call's `graph_url` so the user can explore the neighbourhood. Say
   which themes you didn't cover.

To go further for one paper in the list: `list_citing_papers` with
`sort: "newest"` shows what has cited it since (counted), and
`recommend_papers` with the paper as origin and as `filters.cites` gives the
citing papers closest to it.

## Don'ts

- Don't say the list is complete, or that these are all the missing papers.
  The results are the papers most connected to the chosen origins, from a
  few calls.
- Don't tell the user they must cite a paper. A strong citation link means
  the field cites them together, not that the paper supports their argument:
  Paper Nexus has metadata, not full text.
- Don't spend counted calls one paper at a time over a whole collection.
  Group, then call.
- Don't present a paper as missing without checking it against the list by
  title as well as id.
- Cite only papers a tool returned, with the link it gave. Don't add missing
  papers from memory, even obvious ones; if you think of one, look it up
  with `search_papers` first and say it came from you, not the citation
  links.
