# Directory submissions

Where Paper Nexus is listed, what each place needs, and which file here it
reads. Paste text from [descriptions.md](descriptions.md).

Before the first submission:

- The repository is public at `github.com/PaperNexus/papernexus-mcp`, with
  topics `mcp`, `mcp-server`, `model-context-protocol`, `research`,
  `scientific-papers`, `citations` and `gemini-cli-extension`.
- A free account and a Premium account can both connect from claude.ai and
  ChatGPT, and the tools answer.

| Directory | How | Reads from this repo |
|---|---|---|
| Official MCP Registry | `mcp-publisher login dns --domain papernex.us` with the private key whose public half is in papernex.us's `v=MCPv1` TXT record, then `mcp-publisher publish` from the repo root | `server.json` |
| Claude directory (connector and plugin) | claude.ai/directory/manage on a paid plan: submit the server URL as a connector and this repo as a plugin | `.claude-plugin/plugin.json`, `.mcp.json`, `skills/`, `assets/logo.png` |
| ChatGPT / Codex plugin directory | OpenAI Platform plugin portal → With MCP; domain verification token served at `https://papernex.us/.well-known/openai-apps-challenge` | Copy from [chatgpt.md](chatgpt.md) |
| Gemini CLI extensions | Listed from the `gemini-cli-extension` topic | `gemini-extension.json` |
| Glama | Claim the server after it is indexed | `glama.json` |
| PulseMCP | Indexes the official registry; claim the listing | — |
| Smithery | Add a server by URL | — |
| mcp.so, MCP Market, cursor.directory | Submission forms | — |
| awesome-mcp-servers | Pull request | [awesome-mcp-servers.md](awesome-mcp-servers.md) |

## Releasing a new version

Change `version` in `server.json`, `.claude-plugin/plugin.json` and
`gemini-extension.json` together (CI checks they agree), commit, tag
`v<version>`, run `mcp-publisher publish`, and submit the update in the Claude
directory portal.
