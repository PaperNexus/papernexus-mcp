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

Which tools you see depends on your account and on what you allowed when you
connected:

| Tool | Offered | Counts against the allowance |
|---|---|---|
| `search_papers` | Always | No |
| `recommend_papers` | Always | Yes |
| `get_paper` | Always | No |
| `get_usage` | Always | No |
| `list_library` | When you allow "Read your library" while connecting | No |
| `list_citing_papers` | Rolling out; not yet offered on every account | Yes |
| `recommend_papers` `filters` | Rolling out, Premium; not yet offered on every account | Yes |

See [Allowance](../README.md#allowance) for the limits.

## `search_papers`

Find papers by title and get their Paper Nexus ids.

| Argument | Type | Notes |
|---|---|---|
| `query` | string, required | A title or part of one, a DOI, or a link to a paper (doi.org, arXiv, PubMed, publisher pages). At most 512 characters. |
| `limit` | integer | 1–20, default 10 |
| `fields` | array of strings | Any of `id`, `title`, `authors`, `year`, `doi`, `url` |

Returns `results`: up to `limit` papers, best match first, each with `id`,
`title`, `authors` (the first three), `year`, `doi` and `url`. When nothing
matched every word of the query, the nearest titles come back with
`closest_matches: true`. `too_broad`, `timed_out` and `unread_link` explain an
empty or partial answer.

## `recommend_papers`

Papers related to one or more origin papers, found through their citation
network: papers cited alongside them, and papers that cite the same work.
Several origins find papers related to all of them.

| Argument | Type | Notes |
|---|---|---|
| `papers` | array of strings, required | 1–10 Paper Nexus ids or links. Free accounts combine up to 2. |
| `limit` | integer | 1–50, default 25 |
| `fields` | array of strings | Any of `id`, `title`, `authors`, `year`, `venue`, `doi`, `cited_by_count`, `open_access`, `url`. Cuts the origins as well as the recommendations. |
| `filters` | object | Where offered; see below |

Returns `origins` (the papers you passed), `recommendations`, most related
first, `not_found` (ids that aren't Paper Nexus papers), and `graph_url`, which
opens the whole graph on papernex.us. Each paper has `id`, `title`, `authors`
(the first three), `year`, `venue`, `doi`, `cited_by_count`, `open_access` and
`url`. The graph is also saved to your Paper Nexus history.

### Filters

Where `filters` is offered, every recommended paper passes all the filters
given. The search goes deeper than plain recommendations to fill the list, so
pass filters here rather than filtering the results yourself.

| Filter | Type | Notes |
|---|---|---|
| `year_min`, `year_max` | integer | Publication year range |
| `min_citations`, `max_citations` | integer ≥ 0 | Citation count range |
| `open_access` | boolean | Only papers free to read |
| `types` | array | Any of `article`, `preprint`, `review`, `book`, `dissertation`, `report`, `letter`, `dataset`, `conference-paper`, `data-paper`, `software-paper` |
| `venues` | array, up to 5 | Journals or conferences, any of which may match: a full name, two or more words of one ("Physical Review"), or an acronym ("CVPR", "PNAS"). A single word matches only a venue of that name. Each up to 100 characters. |
| `authors` + `authors_match` | array, up to 5; `any` or `all` | "Geoffrey Hinton" or "Hinton G"; accents and case are ignored. Each up to 100 characters. |
| `cites` + `cites_match` | array, up to 3; `any` or `all` | Keep papers that cite these papers |
| `cited_by` + `cited_by_match` | array, up to 3; `any` or `all` | Keep papers that these papers cite |

A filtered result adds `rank` to each recommendation and `matches_filters` to
each origin, whatever `fields` asks for, plus `filters` (the filters as
understood) and `filter_summary`, which says when fewer papers passed than
were asked for. Its `graph_url` reopens the same filtered graph.

## `get_paper`

One paper's details and its most-cited references.

| Argument | Type | Notes |
|---|---|---|
| `paper` | string, required | A Paper Nexus id or link |
| `references` | integer | How many references to list, most cited first: 0–50, default 10 |
| `fields` | array of strings | Any of `id`, `title`, `authors`, `year`, `venue`, `doi`, `cited_by_count`, `open_access`, `url`. Cuts the references only; the paper itself always comes back whole. |

Returns `paper` (`id`, `title`, `authors`, `year`, `venue`, `type`, `doi`,
`cited_by_count`, `reference_count`, `open_access`, `url`, `graph_url`),
`references`, and `references_indexed` (how many of its references are papers
in Paper Nexus). Each reference has the same fields as a recommendation. Paper
Nexus keeps a paper's first five authors. Not counted, and not saved to your
history.

## `get_usage`

How many counted calls your account has left. Call it before a task that needs
many `recommend_papers` or `list_citing_papers` calls, to plan within the
allowance instead of running into it. It takes no arguments and isn't counted
itself.

Returns `tier` (`free` or `premium`), `usage_period` (`weekly` or `daily`),
`limit`, `used`, `remaining`, `resets_at` (when the current window ends, in
UTC; null when none is open, and the next counted call opens one) and
`counted_tools` (the counted tools your account sees).

## `list_citing_papers`

The papers that cite one paper. Rolling out; not yet offered on every account.

| Argument | Type | Notes |
|---|---|---|
| `paper` | string, required | A Paper Nexus id or link |
| `sort` | string | `newest` (default), `oldest` or `most_cited` |
| `year_from`, `year_to` | integer | Only citing papers published in this span |
| `offset` | integer | 0–1000, default 0 |
| `limit` | integer | 1–50, default 25 |
| `fields` | array of strings | Any of `id`, `title`, `authors`, `year`, `venue`, `doi`, `cited_by_count`, `url` |

Returns `results` (`id`, `title`, `authors` (the first three), `year`, `venue`,
`doi`, `cited_by_count`, `url`), `total` (citing papers in Paper Nexus, or null
when not known exactly), `complete`, `sort`, `offset`, and `next_offset` for the
next page (null on the last one). `total` counts the citing papers Paper Nexus
holds, so it can be lower than a paper's `cited_by_count`. With `year_from` or
`year_to`, a year with many citing papers may list only its most cited ones;
the text names those years, and `complete` is then false.

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
