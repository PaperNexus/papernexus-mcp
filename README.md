<p align="center">
  <img src="assets/logo.png" alt="Paper Nexus" width="96" height="96">
</p>

<h1 align="center">Paper Nexus for AI assistants</h1>

<p align="center">
  Find related scientific papers through their citation network, from Claude, ChatGPT, Cursor, VS Code or any MCP client.
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

Or install the plugin, which adds a skill that teaches Claude a
literature-search workflow with these tools:

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
| `recommend_papers` | Papers related to one or more papers through their citation network |
| `get_paper` | One paper's details and its most-cited references |
| `get_usage` | How many counted calls your account has left |
| `list_library` | Your Paper Nexus library, if you allow "Read your library" when connecting |
| `list_citing_papers` | The papers citing one paper |

`recommend_papers` and `list_citing_papers` also take filters (years,
citation counts, authors, venues, title words, citing or cited papers, open
access, document types) on every account. Each recommendation says which
origin papers it is linked to and how, so your assistant can tell you why a
paper is there.
Every tool that lists papers takes `fields`, to return only the details you
need, such as titles and years. Arguments and results are in the [tool reference](docs/tools.md). Every tool
is read-only.

## Allowance

`recommend_papers` and `list_citing_papers` count against your allowance.
The other tools share a larger daily limit of lookups, and every tool a limit
of 30 calls a minute. `get_usage` tells your assistant how many calls are left.

| Plan | Counted calls | Lookups | Origin papers per recommendation |
|---|---|---|---|
| Free | 10 a week | 100 a day | up to 2 |
| Premium | 200 a day | 1,000 a day | up to 10 |

A filtered call is counted like any other. A recommendation or citing list
that fails or finds nothing isn't counted. See
[pricing](https://papernex.us/pricing) for Premium.

## Privacy and access

- Connecting asks for your permission on a Paper Nexus page that names the app
  and where it will send you back. Library access is asked for separately and
  is read-only.
- Paper Nexus never sees your conversation, only the tool calls your assistant
  makes. Recommendation requests are saved to your Paper Nexus history, as on
  the site.
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
