<p align="center">
  <img src="assets/logo.png" alt="Paper Nexus" width="96" height="96">
</p>

<h1 align="center">Paper Nexus for AI assistants</h1>

<p align="center">
  Find related scientific papers through their citation network, from Claude, ChatGPT, Cursor, VS Code or any MCP client.
</p>

<p align="center">
  <a href="https://lobehub.com/mcp/papernexus-papernexus-mcp"><img src="https://lobehub.com/badge/mcp/papernexus-papernexus-mcp" alt="MCP Badge"></a>
</p>

---

[Paper Nexus](https://papernex.us) maps the scientific literature by its
citations, using the scholarly works in OpenAlex and Semantic Scholar.
This repository holds its [MCP](https://modelcontextprotocol.io) server's
public definition: the connection details, a Claude Code plugin, a Gemini CLI
extension, the MCP Registry entry, and the tool reference. The server itself
is hosted; there is nothing to install or run.

```
https://papernex.us/mcp
```

Ask your assistant things like:

- "Find papers related to *Attention Is All You Need* and *BERT* together."
- "What are the main references of the AlphaFold 2 paper, and what else should I read around it?"
- "Starting from https://arxiv.org/abs/1512.03385, which papers on residual networks should I read?"
- "Go through my *Thesis / Methods* collection and suggest papers I haven't saved."

Every paper it returns links to papernex.us, and each set of recommendations
comes with a link that opens the whole citation graph in Paper Nexus.

## Connect

You sign in with a Paper Nexus account the first time you connect; a free
account works. There are no API keys: the server uses OAuth, so your
assistant opens a Paper Nexus page where you sign in and allow access.

### Claude (claude.ai and Claude Desktop)

Settings → Connectors → **Add custom connector**. Name it Paper Nexus, give
the URL `https://papernex.us/mcp`, then **Connect** and sign in.

### Claude Code

```bash
claude mcp add --transport http papernexus https://papernex.us/mcp
```

Or install the plugin, which adds the server and four skills that teach
Claude how to work with these tools:

| Skill | Use it to |
|---|---|
| `find-related-papers` | Find the papers related to ones you name: literature reviews, what to read next, work that builds on a paper |
| `check-references` | Check a reference list or `.bib` file: is each reference a real paper, and are its title, year, first author and DOI right? |
| `build-bibliography` | Get BibTeX, RIS or CSL-JSON for papers, from Paper Nexus's records rather than the assistant's memory |
| `find-missing-papers` | Find what a draft's references, a reading list or a library collection is missing |

```bash
claude plugin marketplace add PaperNexus/papernexus-mcp
claude plugin install papernexus@papernexus
```

Then run `/mcp`, choose `papernexus`, and sign in.

### ChatGPT

Turn on developer mode (Settings → Apps → Advanced settings), then create an
app with the URL `https://papernex.us/mcp` and OAuth authentication, and sign
in.

### Cursor

[Install in Cursor](https://cursor.com/en/install-mcp?name=papernexus&config=eyJ1cmwiOiJodHRwczovL3BhcGVybmV4LnVzL21jcCJ9),
or add it to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "papernexus": {
      "url": "https://papernex.us/mcp"
    }
  }
}
```

### VS Code

[Install in VS Code](https://insiders.vscode.dev/redirect/mcp/install?name=papernexus&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fpapernex.us%2Fmcp%22%7D),
or add it to `.vscode/mcp.json`:

```json
{
  "servers": {
    "papernexus": {
      "type": "http",
      "url": "https://papernex.us/mcp"
    }
  }
}
```

### Gemini CLI

```bash
gemini extensions install https://github.com/PaperNexus/papernexus-mcp
```

### Other clients

Any client that speaks MCP over Streamable HTTP with OAuth can connect to
`https://papernex.us/mcp`. The server supports Client ID Metadata Documents
and dynamic client registration, and every protocol revision from 2025-03-26
on.

## Tools

| Tool | What it does |
|---|---|
| `search_papers` | Find a paper by its title, a DOI or a link, and get its Paper Nexus id |
| `recommend_papers` | Papers related to one or more papers through their citation network, or to a library collection, in the order you choose (most related, most central, reviews or recent), leaving out papers you already have |
| `get_paper` | One paper's details, subject, keywords, summary, PDF link and most-cited references |
| `list_references` | The papers one paper cites, sorted, by year or filtered |
| `get_citation_edges` | Which of up to 100 papers cite which: the citations among them |
| `export_citations` | Up to 50 papers as BibTeX, RIS or CSL-JSON, for your reference manager |
| `verify_references` | Checks up to 50 references: is each a real paper and the one it names, and where do its title, year, first author and DOI differ from Paper Nexus's record |
| `get_usage` | How many counted calls your account has left |
| `list_library` | Your Paper Nexus library, if you allow "Read your library" when connecting |
| `add_to_library` | Saves papers to your library, into collections it can create, if you allow "Add papers to your library" when connecting |
| `move_papers`, `remove_from_library` | Moves papers between your collections, or removes them from your library, if you allow "Move and remove papers, and rename, move and delete collections" when connecting |
| `update_collection`, `delete_collection` | Renames, moves or deletes one of your collections, with the same permission |
| `list_citing_papers` | The papers citing one paper |
| `submit_feedback` | Sends the Paper Nexus team a note about wrong or missing data, an error, or a confusing tool |

`recommend_papers`, `list_references` and `list_citing_papers` also take filters (years,
citation counts, authors, venues, title words, citing or cited papers, open
access, document types) on every account. Each recommendation says which
origin papers it is linked to and how, so your assistant can tell you why a
paper is there. `recommend_papers` can also order the graph's papers by how
central they are to it, by how many of them a paper cites (as reviews do) or
by recency, list the graph's top authors and venues, and leave out papers you
have already read or saved.
Every tool that takes a paper takes its DOI, arXiv id, PMID, PMCID or
OpenAlex id as well as a Paper Nexus id, so there's no need to search first.
Every tool that lists papers takes `fields`, to return only the details you
need, such as titles and years. Arguments and results are in the [tool reference](docs/tools.md). Every tool
but `submit_feedback` and the five library tools that change your library is
read-only: the first only sends a note, `add_to_library` only adds papers and
collections, and the other four, which move and remove papers and collections,
are marked destructive so apps ask you before running them.

In apps that show MCP Apps views, such as Claude on the web, `recommend_papers`
also draws its result in the conversation as the graph Paper Nexus shows for
it: your paper in the middle, the related papers around it, coloured by year.
It expands to an interactive view with the list of papers and a switch between
similarity and citation links, and opens the same graph on papernex.us. Other
apps show the same result as text.

## Allowance

`recommend_papers` and `list_citing_papers` count against your allowance.
The other tools share a larger daily limit of lookups (`search_papers`,
`get_paper`, `get_citation_edges`, `export_citations`, `add_to_library`,
`move_papers` and `remove_from_library` use one per query or paper, and
`verify_references` one per reference), and every tool a limit of calls a
minute: 60 on Premium, 30 on a free account. `get_usage` uses no lookup.
`submit_feedback` has its own limit of 10 notes a day.
`get_usage` tells your assistant how many calls are left.

| Plan | Counted calls | Lookups | Origin papers per recommendation |
|---|---|---|---|
| Free | 10 a week | 100 a day | up to 10 |
| Premium | 200 a day | 5,000 a day | up to 100 |

A filtered call is counted like any other, and takes up to 10 origin papers
on every plan. A recommendation or citing list
that fails or finds nothing isn't counted. See
[pricing](https://papernex.us/pricing) for Premium.

## Privacy and access

- Connecting asks for your permission on a Paper Nexus page that names the app
  and where it will send you back. Library access is asked for separately, as
  three permissions: reading your library; adding papers and collections to
  it; and moving and removing papers and renaming, moving and deleting
  collections. Only the third can remove or move anything, and removed papers
  and deleted collections can't be restored.
- Paper Nexus never sees your conversation, only the tool calls your assistant
  makes. Recommendation requests are saved to your Paper Nexus history, as on
  the site.
- `add_to_library` saves papers to your library only with the "Add papers to
  your library" permission, and the four tools that change it only with the
  "Move and remove papers" one. If you connected before a permission existed,
  reconnect to grant it.
- `submit_feedback` sends the Paper Nexus team a note your assistant writes,
  when you ask it to or when it finds a problem with a result. It is marked as
  a tool that isn't read-only, so apps that ask before running one ask you
  first.
- You can see and revoke connected apps in Paper Nexus under Account settings
  → AI assistants.

[Privacy policy](https://papernex.us/privacy) ·
[Terms](https://papernex.us/terms)

## Support

[Open an issue](https://github.com/PaperNexus/papernexus-mcp/issues) or email
[info@papernex.us](mailto:info@papernex.us).

## License

The files in this repository are MIT licensed; see [LICENSE](LICENSE). The
Paper Nexus service and its data are covered by its
[terms](https://papernex.us/terms).
