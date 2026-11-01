# Tool reference

Every tool is read-only: it never changes your papers, your library or
anything outside Paper Nexus. Each result comes back two ways: a short text
list for the model, and the same data as structured content. A paper id is a
6-character Paper Nexus id such as `0Bwo97`; wherever a tool takes one, a
`papernex.us/paper/<id>` link works too.

Every tool that lists papers takes `fields`: the names of the paper fields to
return, such as `["title", "year"]`, to keep a long result short. It cuts each
listed paper in the text and the structured content alike. A paper's `id`
always comes back, since the other tools take it, and so does everything that
isn't part of a listed paper, such as `graph_url`, totals and cursors. Leave
`fields` out for every field. Each tool's table below lists the fields it
offers.

What you can use depends on your plan and on what you allowed when you
connected:

| Tool | Available to | Counts against |
|---|---|---|
| `search_papers` | Every account | Lookups |
| `recommend_papers` | Every account | The allowance |
| `recommend_papers` `filters` | Every account | The allowance |
| `get_paper` | Every account | Lookups |
| `get_usage` | Every account | Lookups |
| `list_citing_papers` | Every account | The allowance |
| `list_citing_papers` `filters` | Every account | The allowance |
| `list_library` | Every account, when you allow "Read your library" while connecting | Lookups |

Every call also counts toward a limit of 30 calls a minute. Past a limit, the
tool answers with an error naming the limit and when it resets. See
[Allowance](../README.md#allowance) for the limits.

## `search_papers`

Find papers by title and get their Paper Nexus ids.

| Argument | Type | Notes |
|---|---|---|
| `query` | string, required | A title or part of one, a DOI, or a link to a paper (doi.org, arXiv, PubMed, publisher pages). At most 512 characters. |
| `limit` | integer | 1–20, default 10 |
| `fields` | array of strings | Any of `id`, `title`, `authors`, `year`, `doi`, `cited_by_count`, `url` |

Returns `results`: up to `limit` papers, best match first, each with `id`,
`title`, `authors` (the first three), `year`, `doi`, `cited_by_count` (null
when not known) and `url`, so comparing matches by citations takes no further
calls. When nothing
matched every word of the query, the nearest titles come back with
`closest_matches: true`. `too_broad`, `timed_out` and `unread_link` explain an
empty or partial answer.

## `recommend_papers`

Papers related to one or more origin papers, found through their citation
network: papers cited alongside them, and papers that cite the same work.
Several origins merge their related papers, with papers related to more than
one of them first. Origins from unrelated fields give a mix of each field's
papers, not papers bridging them; to keep only papers linked to every origin,
pass the origins as `filters.cites` with `cites_match: "all"`, or narrow by
topic with `filters.title`.

| Argument | Type | Notes |
|---|---|---|
| `papers` | array of strings, required | 1–10 Paper Nexus ids or links. Free accounts combine up to 2. |
| `limit` | integer | 1–50, default 25 |
| `fields` | array of strings | Any of `id`, `title`, `authors`, `year`, `venue`, `doi`, `cited_by_count`, `open_access`, `url`, `evidence`. Cuts the origins as well as the recommendations. |
| `filters` | object | See below |

Returns `origins` (the papers you passed), `recommendations`, most related
first, `not_found` (ids that aren't Paper Nexus papers), and `graph_url`, which
opens the whole graph on papernex.us. That graph usually holds more papers
than `limit`: the list is its top papers. Each paper has `id`, `title`, `authors`
(the first three), `year`, `venue`, `doi`, `cited_by_count`, `open_access` and
`url`, and each recommendation also has `evidence`. The graph is also saved to
your Paper Nexus history.

The order weighs how strongly each paper is linked to the origins through
citations, over a sample of the citing papers and references of a widely
cited origin. Without filters, it also damps very highly cited papers and
lifts recent ones. It orders this one list: it isn't a probability of
relevance or a measure of a paper's importance.

### Evidence

`evidence` gives the citation links behind a recommendation. It holds only
what the citation graph records, and a part is left out when the graph
doesn't record it:

| Field | Meaning |
|---|---|
| `linked_origins` | The origins it was found through: cited alongside them, sharing references with them, or citing or cited by them |
| `cites` | The origins it cites |
| `cited_by` | The origins that cite it |
| `citation_linked` | Present only as `false`: the paper wasn't found through citations, but added from OpenAlex's related works to fill a short list, after every linked paper |
| `link_counts` | By origin id, `co_cited` (papers citing both it and the origin) and `shared_references` (references both cite), for the origins with either |

The counts are taken over what was read for each origin, which each origin in
`origins` reports as `sampled` (`citing_papers`, `references`). For a widely
cited origin that is a sample, so treat the counts as how strongly a paper is
linked, not as totals. A paper held up by one or two links is a weaker lead
than one with dozens.

Origins are given by their ids. In the text, each paper's line names them by
their number in the origin list ("cites origin 2", "origin 1: 12 co-citations,
3 shared references"), and marks a paper without a citation link "no citation
link". Author names are given first name first.

### Filters

With `filters`, every recommended paper passes all the filters given. A
filtered call is counted like any other. The search goes deeper than plain recommendations to fill the list, so
pass filters here rather than filtering the results yourself.

| Filter | Type | Notes |
|---|---|---|
| `year_min`, `year_max` | integer | Publication year range |
| `min_citations`, `max_citations` | integer ≥ 0 | Citation count range |
| `open_access` | boolean | Only papers free to read |
| `types` | array | Any of `article`, `preprint`, `review`, `book`, `dissertation`, `report`, `letter`, `dataset`, `conference-paper`, `data-paper`, `software-paper` |
| `venues` | array, up to 5 | Journals or conferences, any of which may match: a full name, two or more words of one ("Physical Review"), or an acronym ("CVPR", "PNAS"). A single word matches only a venue of that name. Each up to 100 characters. |
| `authors` + `authors_match` | array, up to 5; `any` or `all` | "Geoffrey Hinton" or "Hinton G"; accents and case are ignored. Each up to 100 characters. |
| `title` + `title_match` | array, up to 5; `any` or `all` | Words or phrases the title must contain, such as "QROM" or "surface code". They match whole words, so QROM doesn't match QROMs; case, accents and punctuation are ignored. Each up to 100 characters. Pair it with `cites` to find the papers citing a paper that are about one topic; see [Heavily cited papers](#heavily-cited-papers). |
| `cites` + `cites_match` | array, up to 3; `any` or `all` | Keep papers that cite these papers |
| `cited_by` + `cited_by_match` | array, up to 3; `any` or `all` | Keep papers that these papers cite |

A filtered result adds `rank` to each recommendation and `matches_filters` to
each origin, whatever `fields` asks for, plus `filters` (the filters as
understood) and `filter_summary`. Its `graph_url` reopens the same filtered
graph, at the size Paper Nexus shows on its site (25, 50 or 100 papers), so it
can hold more papers than `limit`.

`filter_summary` has `requested` (papers the search tried to find),
`returned` (papers it found that pass), `checked` (nearby papers it checked
against the filters), `budget_hit` (true when the list is short because the
search reached the most papers it checks, so more that pass may exist further
out), `deadline_hit` (the search ran out of time), `matched` (the author and
venue names each filter matched) and `notes` (why the list is short, if it
is, and anything else to know).

### Heavily cited papers

Paper Nexus stores up to 1,000 of each paper's citing papers. For a paper
with more, the `cites` filter can't list every paper that cites it, so the
search checks only papers near the origins: papers cited alongside them, or
sharing their references. Topics far from the origins' neighbourhood, and
especially recent work, can come back with few results or none, even when many
papers that cite it exist. "Papers citing *Attention Is All You Need* since
2024 about retrieval" is an example. When this applies, the result's first
line says so, and `filter_summary.sampled_cites` names the papers
(`id`, `title`). `list_citing_papers` with filters checks only a sample of such
a paper's citing papers too.

## `get_paper`

One paper's details and its most-cited references.

| Argument | Type | Notes |
|---|---|---|
| `paper` | string, required | A Paper Nexus id or link |
| `references` | integer | How many references to list, most cited first: 0–50, default 10 |
| `fields` | array of strings | Any of `id`, `title`, `authors`, `year`, `venue`, `doi`, `cited_by_count`, `open_access`, `url`. Cuts the references only; the paper itself always comes back whole. |

Returns `paper` (`id`, `title`, `authors`, `year`, `venue`, `type`, `doi`,
`arxiv_id`, `cited_by_count`, `reference_count`, `open_access`, `url`,
`graph_url`),
`references`, and `references_indexed` (how many of its references are papers
in Paper Nexus). Each reference has the same fields as a recommendation. Paper
Nexus keeps a paper's first five authors. It uses a lookup, not the allowance,
and isn't saved to your history.

## `get_usage`

How many calls your account has left. Call it before a task that needs many
calls, to plan within the limits instead of running into them. It takes no
arguments. It isn't counted against the allowance, but it uses one lookup.

Returns `checked_at` (the report's time, in UTC), `tier` (`free` or
`premium`), `usage_period` (`weekly` or `daily`), `limit`, `used`,
`remaining`, `resets_at` (when the current window ends, in UTC; null when none
is open, and the next counted call opens one) and
`counted_tools` (the counted tools your account sees), plus `lookups` (`limit`,
`used`, `remaining`, `resets_at` and `tools`, the daily limit the other tools
share) and `calls_per_minute`. Each window starts at its first call, not at
midnight, so the allowance and the lookups can reset at different times; the
text says how long each has left.

## `list_citing_papers`

The papers that cite one paper, newest, earliest or most cited first.

| Argument | Type | Notes |
|---|---|---|
| `paper` | string, required | A Paper Nexus id or link |
| `sort` | string | `newest` (default), `oldest` or `most_cited` |
| `year_from`, `year_to` | integer | Only citing papers published in this span |
| `offset` | integer | 0–1000, default 0 |
| `limit` | integer | 1–50, default 25 |
| `fields` | array of strings | Any of `id`, `title`, `authors`, `year`, `venue`, `doi`, `cited_by_count`, `open_access`, `url` |
| `filters` | object | See below |

Returns `results` (`id`, `title`, `authors` (the first three), `year`, `venue`,
`doi`, `cited_by_count`, `open_access`, `url`), `total` (citing papers in Paper Nexus, or null
when not known exactly), `complete`, `sort`, `offset`, and `next_offset` for the
next page (null on the last one). `total` counts the citing papers Paper Nexus
holds, so it can be lower than a paper's `cited_by_count`. With `year_from` or
`year_to`, a year with many citing papers may list only its most cited ones;
the text names those years, and `complete` is then false.

With `filters`, only the citing papers that pass every filter are listed, in
the same order. They are `recommend_papers`' [filters](#filters) except
`year_min` and `year_max`: use `year_from` and `year_to` for the years.
The result adds `filters` (the filters as understood)
and `filter_summary`: `checked` (citing papers checked against the filters)
and `passed` (those that pass). `total` still counts every citing paper, not
only those that pass.

For a paper with more than 1,000 citing papers, only a sample of them is
checked: those in range among its 200 newest, 200 earliest and 200 most cited
citing papers and the 50 most cited from each year, 2,000 at most, whatever
the sort. A recent three-year range therefore checks about 350. The order is within that sample, so "newest first" means
the newest of those. `complete` is then false, and the text says what was
checked and that more that pass may exist.

To find the citing papers most closely related to a paper, rather than all of
them by date or citation count, call `recommend_papers` with the paper as the
origin and as `filters.cites`. Most cited first ranks by citations alone, so
it is led by widely cited papers that cite this one in passing.

## `list_library`

Your own Paper Nexus library. Offered only when you allowed "Read your
library" while connecting; it can read your library and never change it.

| Argument | Type | Notes |
|---|---|---|
| `collection` | string | A collection's name, path ("Thesis / Methods") or id. Without it, the first page lists your collections and your first papers. |
| `cursor` | string | `next_cursor` from the previous page |
| `limit` | integer | 1–100, default 50 |
| `fields` | array of strings | Any of `id`, `title`, `authors`, `year`, `venue`, `doi`, `url`, `collections` |

Returns `items` (each paper's `id`, `title`, `authors` (the first three),
`year`, `venue`, `doi`, `url` and the paths of the `collections` it is in),
`next_cursor` (null on the last page), and `collection` when you asked for
one. A first page without a collection also has `counts` (`papers` and
`collections`) and `collections`: each one's `id`, `name`, `path` and whether
it is `monitored` for new citing papers. With a
collection, only the papers directly in it are listed, not those in its
subcollections. A paper you imported that matched nothing in Paper Nexus has a
null `id`.
