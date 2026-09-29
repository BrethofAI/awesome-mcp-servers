# awesome-mcp-servers

> Curated, working MCP servers for Claude Desktop, Claude Code, the Claude Agent SDK, and other MCP-compatible clients in 2026.

Maintained by [Brethof AI](https://brethof.ai). Companion to
[awesome-llms-txt](https://github.com/BrethofAI/awesome-llms-txt) and
[awesome-ai-coding-agents](https://github.com/BrethofAI/awesome-ai-coding-agents).

## Why this list exists

The Model Context Protocol ([spec](https://modelcontextprotocol.io)) lets
LLM clients call out to external tools and data sources through a uniform
interface. By 2026 there are hundreds of community MCP servers — many stale,
prototype-quality, or so under-documented they hide what they actually do.
This list curates servers that:

- **Work today** with Claude Desktop ≥ 1.0 or Claude Code ≥ 2.0.
- **Resolve to a real artefact** — installable from a registry, a published
  repo, or a working binary release. No "coming soon" placeholders, and every
  link is checked (a CI-style sweep cuts entries whose URL 404s).
- **State their permissions clearly** — so you know what the server can
  read, write, or execute on your behalf before you allow it.

Our entries default to the most-recently-maintained official build. If
multiple forks compete, the most active fork at audit time wins.

## Legend

- 🏷️ `official` — published by the originating company (Anthropic, Stripe,
  Atlassian, etc.) or the project itself.
- 🏷️ `community` — third-party server. Quality varies; we link only ones
  we've used or that have credible maintainers.
- 🏷️ `brethof` — maintained by Brethof AI.
- 🛡️ `read-only` — server cannot mutate anything in the connected system.
- ⚠️ `mutating` — server can write, send, or modify state. Authorise with care.
- 🔒 `local` — runs entirely on your machine, no remote calls during use.

## Contents

- [Official Anthropic Servers](#official-anthropic-servers) (7)
- [Files, Filesystem & Local Data](#files-filesystem--local-data) (1)
- [Web Search & Browsing](#web-search--browsing) (7)
- [Browser Automation](#browser-automation) (3)
- [Source Control](#source-control) (2)
- [Issue Trackers & Project Management](#issue-trackers--project-management) (4)
- [Communication](#communication) (4)
- [Relational Databases](#relational-databases) (4)
- [NoSQL & Document Databases](#nosql--document-databases) (2)
- [Vector & Memory Stores](#vector--memory-stores) (5)
- [Productivity & Notes](#productivity--notes) (5)
- [Design & Creative](#design--creative) (1)
- [Operations & Infrastructure](#operations--infrastructure) (6)
- [AI & ML Platforms](#ai--ml-platforms) (1)
- [Specialised / Vertical](#specialised--vertical) (2)
- [Frameworks & SDKs for Building MCP Servers](#frameworks--sdks-for-building-mcp-servers) (4)

<!-- The list below is generated from entries/*.yaml by scripts/gen_awesome_readme.py. Edit the YAML, not this section. -->

## Official Anthropic Servers

Reference implementations from Anthropic, kept in [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers). (Several earlier reference servers — github, slack, postgres, gdrive and others — have moved to their vendors' own MCP servers or the project's archive; we list them under their current homes as they're re-verified.)

- **[everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything)** — 🏷️ official  
  Demo server exercising every MCP feature. Useful for testing clients.
- **[fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** — 🏷️ official 🛡️ read-only  
  Fetch a single URL and return its content as Markdown for the model.
- **[filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** — 🏷️ official ⚠️ mutating 🔒 local  
  Read, write, and search files within explicitly-allowed directories.
- **[git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** — 🏷️ official ⚠️ mutating 🔒 local  
  Read repository state, view diffs, run common git commands.
- **[memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** — 🏷️ official ⚠️ mutating 🔒 local  
  Reference knowledge-graph memory server. Persistent JSON-graph store.
- **[sequentialthinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** — 🏷️ official 🛡️ read-only  
  Helper that exposes a structured "think step by step" planning tool.
- **[time](https://github.com/modelcontextprotocol/servers/tree/main/src/time)** — 🏷️ official 🛡️ read-only 🔒 local  
  Current time and timezone conversion (`get_current_time`, `convert_time`).

## Files, Filesystem & Local Data

- **[obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** — 🏷️ community ⚠️ mutating 🔒 local  
  Read and edit notes in your Obsidian vault.

## Web Search & Browsing

- **[brave-search](https://github.com/brave/brave-search-mcp-server)** — 🏷️ official 🛡️ read-only  
  Brave's official server for the Brave Search API: web, local, image, video, and news search plus summarizer; needs `BRAVE_API_KEY`. Replaces the archived reference Brave server.
- **[context7](https://github.com/upstash/context7)** — 🏷️ official 🛡️ read-only  
  Upstash's up-to-date library documentation for coding agents (`resolve-library-id`, `query-docs`). Remote at `https://mcp.context7.com/mcp`; an API key is recommended.
- **[duckduckgo](https://github.com/nickclyde/duckduckgo-mcp-server)** — 🏷️ community 🛡️ read-only  
  No-tracking search via DuckDuckGo.
- **[exa](https://github.com/exa-labs/exa-mcp-server)** — 🏷️ official 🛡️ read-only  
  Exa neural-search API; semantic + similarity search over the web.
- **[firecrawl](https://github.com/firecrawl/firecrawl-mcp-server)** — 🏷️ official 🛡️ read-only  
  Crawl + scrape websites and extract structured data.
- **[perplexity](https://github.com/perplexityai/modelcontextprotocol)** — 🏷️ official 🛡️ read-only  
  Perplexity's official server for its API Platform: grounded web search and answers. Hosted remote, or `npx @perplexity-ai/mcp-server` with an API key.
- **[tavily](https://github.com/tavily-ai/tavily-mcp)** — 🏷️ official 🛡️ read-only  
  Tavily's research-optimised search API for agents.

## Browser Automation

- **[browser-use](https://github.com/browser-use/browser-use)** — 🏷️ community ⚠️ mutating  
  Vision + DOM-graph hybrid for resilient browser automation.
- **[chrome-devtools](https://github.com/ChromeDevTools/chrome-devtools-mcp)** — 🏷️ official ⚠️ mutating  
  Chrome DevTools team's server: control and inspect a live Chrome for automation, debugging (network, console, screenshots), and performance traces. Sends usage statistics to Google by default (`--no-usage-statistics` opts out).
- **[playwright](https://github.com/microsoft/playwright-mcp)** — 🏷️ official ⚠️ mutating  
  Microsoft's official Playwright MCP. Multi-browser, accessibility-tree snapshots designed for agent loops.

## Source Control

- **[gitea](https://gitea.com/gitea/gitea-mcp)** — 🏷️ official ⚠️ mutating  
  Self-hosted Gitea instances; full repo + issue + PR control.
- **[github](https://github.com/github/github-mcp-server)** — 🏷️ official ⚠️ mutating  
  GitHub's official server: repos, issues, pull requests, Actions, code security, grouped into toolsets. Local binary or remote at `https://api.githubcopilot.com/mcp/`; `--read-only` drops all write tools.

## Issue Trackers & Project Management

- **[asana](https://developers.asana.com/docs/using-asanas-mcp-server)** — 🏷️ official ⚠️ mutating  
  Asana's hosted MCP server (`https://mcp.asana.com/v2/mcp`): tasks, projects, reports. OAuth; replaces the deprecated `/sse` beta endpoint.
- **[atlassian](https://github.com/atlassian/atlassian-mcp-server)** — 🏷️ official ⚠️ mutating  
  Atlassian's official remote MCP server: Jira, Confluence, Jira Service Management, Bitbucket, Compass. OAuth 2.1 or API tokens.
- **[linear](https://linear.app/docs/mcp)** — 🏷️ official ⚠️ mutating  
  Linear's hosted MCP server (`https://mcp.linear.app/mcp`; read-only variant at `/mcp/readonly`): issues, projects, cycles, comments. OAuth 2.1 or API key.
- **[trello](https://github.com/delorenj/mcp-server-trello)** — 🏷️ community ⚠️ mutating  
  Trello board, list, and card operations.

## Communication

- **[discord](https://github.com/SaseQ/discord-mcp)** — 🏷️ community ⚠️ mutating  
  Send, search, and moderate Discord messages.
- **[google-workspace](https://github.com/taylorwilsdon/google_workspace_mcp)** — 🏷️ community ⚠️ mutating  
  Gmail, Calendar, Drive, Docs, Sheets, Chat and more behind one server (120+ tools in core/extended/complete tiers). Uses your own Google OAuth client.
- **[slack](https://docs.slack.dev/ai/slack-mcp-server/)** — 🏷️ official ⚠️ mutating  
  Slack's hosted MCP server (`https://mcp.slack.com/mcp`): search channels, send messages, manage canvases. OAuth with per-tool scopes; workspace admins approve and manage access.
- **[telegram](https://github.com/chigwell/telegram-mcp)** — 🏷️ community ⚠️ mutating  
  Read and send Telegram messages, chats, contacts, and media as your own user account (Telethon session), not a bot.

## Relational Databases

- **[clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** — 🏷️ official 🛡️ read-only  
  ClickHouse analytics queries. Read-only by default; writes need `CLICKHOUSE_ALLOW_WRITE_ACCESS=true`, and destructive statements a further opt-in.
- **[mysql](https://github.com/benborla/mcp-server-mysql)** — 🏷️ community ⚠️ mutating  
  MySQL/MariaDB read + write with safe-mode toggle.
- **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** — 🏷️ community ⚠️ mutating  
  Crystal DBA's Postgres MCP with schema mutation and tuning advisors.
- **[supabase](https://github.com/supabase/mcp)** — 🏷️ official ⚠️ mutating  
  Supabase's official server (`https://mcp.supabase.com/mcp`): database, docs, and project tools. Scope it with `project_ref` and `read_only=true`.

## NoSQL & Document Databases

- **[mongodb](https://github.com/mongodb-js/mongodb-mcp-server)** — 🏷️ official ⚠️ mutating  
  MongoDB's official server for databases and Atlas clusters: query, aggregation, CRUD. `--readOnly` restricts it to read tools.
- **[neo4j](https://github.com/neo4j/mcp)** — 🏷️ official ⚠️ mutating  
  Neo4j's official server: `read-cypher` and `write-cypher` tools against your graph; `NEO4J_MCP_READ_ONLY=true` disables writes.

## Vector & Memory Stores

- **[brethof-brain](https://brethof.ai/brain/)** — 🏷️ brethof ⚠️ mutating  
  Persistent memory for AI agents across sessions, projects and machines. Every session opens with a brief — your standing rules, what each project is, where the last sessions stopped — and the records that bear on a prompt arrive with it. It curates itself into records per project, keeps the full chat history searchable, and adds notes, playbooks and an optional knowledge graph with dated connections you can query in Cypher. Proven on nine platforms: Claude Code (Linux, Windows), Codex, Qwen Code, Cline, OpenCode, Kilo Code, OpenClaw, Hermes Agent and dsh. Memory lives on your machine (local edition, Docker or Podman) or encrypted under a passphrase only you hold (hosted); each exchange is processed by our hub, which keeps none of it. Free tier; the client is source-available. Disclosure: maintained by us.
- **[chroma](https://github.com/chroma-core/chroma-mcp)** — 🏷️ official ⚠️ mutating 🔒 local  
  ChromaDB collections, similarity search, persistent embeddings.
- **[pinecone](https://github.com/pinecone-io/pinecone-mcp)** — 🏷️ official ⚠️ mutating  
  Pinecone managed vector search.
- **[qdrant](https://github.com/qdrant/mcp-server-qdrant)** — 🏷️ official ⚠️ mutating  
  Qdrant vector search and collection management.
- **[weaviate](https://docs.weaviate.io/weaviate/configuration/mcp-server)** — 🏷️ official ⚠️ mutating  
  MCP server built into Weaviate (preview from v1.37.1; `MCP_SERVER_ENABLED=true`, served at `/v1/mcp`): hybrid search, collection config, object upsert; respects RBAC. Replaces the deprecated standalone server.

## Productivity & Notes

- **[airtable](https://support.airtable.com/articles/9897799762-using-the-airtable-mcp-server)** — 🏷️ official ⚠️ mutating  
  Airtable's hosted MCP server (`https://mcp.airtable.com/mcp`): bases, tables, records. OAuth or personal access token.
- **[apple-notes](https://github.com/sweetrb/apple-notes-mcp)** — 🏷️ community ⚠️ mutating 🔒 local  
  Read, search, create, edit, and organise Apple Notes on macOS via AppleScript.
- **[google-calendar](https://github.com/nspady/google-calendar-mcp)** — 🏷️ community ⚠️ mutating  
  Read and create calendar events.
- **[notion](https://developers.notion.com/docs/mcp)** — 🏷️ official ⚠️ mutating  
  Notion's hosted MCP server: search the workspace, read and edit pages in Markdown. OAuth, respects each user's existing permissions. (The self-hosted makenotion/notion-mcp-server is no longer maintained.)
- **[screenpipe](https://github.com/screenpipe/screenpipe/tree/main/packages/screenpipe-mcp)** — 🏷️ official ⚠️ mutating  
  Search your recorded screen text, audio transcripts, meetings, and activity summaries; can also control recording, run pipes, and edit memories. Reads your full screen and audio history, so grant it with care. Source-available under the Screenpipe Commercial License (not an OSI open-source licence).

## Design & Creative

- **[mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)** — 🏷️ community ⚠️ mutating 🔒 local  
  Drive Blender via Python — modify scenes, run renders, manage assets. Formerly blender-mcp; the PyPI package is now `mcp-for-blender`.

## Operations & Infrastructure

- **[aws](https://github.com/awslabs/mcp)** — 🏷️ official ⚠️ mutating  
  Amazon-published MCPs covering AWS service catalog, Bedrock, S3, etc.
- **[docker-mcp-gateway](https://github.com/docker/mcp-gateway)** — 🏷️ official ⚠️ mutating  
  Docker's MCP Toolkit CLI plugin (`docker mcp`): runs catalog MCP servers in isolated containers behind one gateway, with Docker Desktop secrets management.
- **[grafana](https://github.com/grafana/mcp-grafana)** — 🏷️ official ⚠️ mutating  
  Grafana's official server: dashboards, datasource queries, incidents, annotations. Can create and update dashboards and incidents; `--disable-write` makes it read-only.
- **[helm](https://github.com/zekker6/mcp-helm)** — 🏷️ community ⚠️ mutating  
  Manage Helm releases against a Kubernetes cluster.
- **[kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** — 🏷️ community ⚠️ mutating  
  kubectl-equivalent operations on the configured cluster.
- **[sentry](https://github.com/getsentry/sentry-mcp)** — 🏷️ official ⚠️ mutating  
  Sentry's official server: issues, events, projects, alerts and monitors; can update issues and create projects. Remote at `https://mcp.sentry.dev/mcp` or stdio. Licence: FSL-1.1-Apache-2.0.

## AI & ML Platforms

- **[huggingface](https://github.com/huggingface/hf-mcp-server)** — 🏷️ official ⚠️ mutating  
  Hugging Face's official server: Hub search and details, plus Gradio Spaces as tools. Hosted at `https://hf.co/mcp` or run locally.

## Specialised / Vertical

- **[spotify](https://github.com/varunneal/spotify-mcp)** — 🏷️ community ⚠️ mutating  
  Spotify Web API: search, queue, playlists.
- **[stripe](https://docs.stripe.com/mcp)** — 🏷️ official ⚠️ mutating  
  Stripe's hosted MCP server (`https://mcp.stripe.com`): payments, customers, subscriptions, refunds via OAuth or agent API keys. Refunds and outbound payments need human confirmation. From 2026-10-31 it accepts only Agent-tagged keys or OAuth.

## Frameworks & SDKs for Building MCP Servers

- **[fastmcp](https://github.com/PrefectHQ/fastmcp)** — 🏷️ community  
  Python framework for MCP servers and clients, now under PrefectHQ. FastMCP 1.0 was incorporated into the official Python SDK in 2024; this is the actively maintained standalone project.
- **[mcp-go](https://github.com/modelcontextprotocol/go-sdk)** — 🏷️ official  
  Go SDK for building MCP servers. Single-binary deployment friendly.
- **[mcp-python](https://github.com/modelcontextprotocol/python-sdk)** — 🏷️ official  
  Reference Python SDK. Includes `FastMCP` for terse decorator-based servers.
- **[mcp-typescript](https://github.com/modelcontextprotocol/typescript-sdk)** — 🏷️ official  
  Reference TypeScript / Node SDK. Powers most npm-distributed servers.

## Discovery hubs

Where to look for new servers as the ecosystem grows.

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** — Anthropic's reference servers + a list of community ones at the bottom.
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** — Largest community list. Less curation than ours; useful for completeness.
- **[Smithery](https://smithery.ai)** — Hosted MCP-server registry with one-click install for many clients.
- **[mcp.so](https://mcp.so)** — Searchable directory of public MCP servers.

## Related work

- **[awesome-llms-txt](https://github.com/BrethofAI/awesome-llms-txt)** — Tools that make themselves discoverable to AI agents.
- **[awesome-ai-coding-agents](https://github.com/BrethofAI/awesome-ai-coding-agents)** — Honest comparison of AI coding assistants. Most either ship MCP-host support or are themselves embeddable as MCP servers.
- **[awesome-local-ai](https://github.com/BrethofAI/awesome-local-ai)** — Local-AI tools, many of which integrate with these MCPs.
- **[awesome-private-ai](https://github.com/BrethofAI/awesome-private-ai)** — Privacy-respecting AI architectures; relevant when picking which MCPs you let touch your data.

## Contributing

Open an issue with the server name, repo URL, the category it belongs to, and
one paragraph on what makes it worth listing. Entries live as one YAML file
each under `entries/`; this README is generated from them, so edit the YAML,
not the list above. We won't list servers without a maintained release in the
last 6 months unless the maintainer says they're keeping it alive.

## License

[MIT](LICENSE).

---

Maintained by **[Brethof AI](https://brethof.ai)** — AI tools built for
people who take their data seriously.
