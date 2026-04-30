# awesome-mcp-servers

> Curated, working MCP servers for Claude Desktop, Claude Code, the Claude Agent SDK, and other MCP-compatible clients in 2026.

Maintained by [Brethof AI](https://brethof.com). Companion to
[awesome-llms-txt](https://github.com/BrethofAI/awesome-llms-txt) and
[awesome-ai-coding-agents](https://github.com/BrethofAI/awesome-ai-coding-agents).

## Why this list exists

The Model Context Protocol ([spec](https://modelcontextprotocol.io)) lets
LLM clients call out to external tools and data sources through a uniform
interface. By April 2026 there are hundreds of community MCP servers —
many stale, prototype-quality, or so under-documented they hide what they
actually do. This list curates servers that:

- **Work today** with Claude Desktop ≥ 1.0 or Claude Code ≥ 2.0.
- **Resolve to a real artefact** — installable from a registry, a published
  repo, or a working binary release. No "coming soon" placeholders.
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

- [Official Anthropic Servers](#official-anthropic-servers)
- [Brethof MCPs](#brethof-mcps)
- [Files, Filesystem & Local Data](#files-filesystem--local-data)
- [Web Search & Browsing](#web-search--browsing)
- [Browser Automation](#browser-automation)
- [Source Control](#source-control)
- [Issue Trackers & Project Management](#issue-trackers--project-management)
- [Communication](#communication)
- [Relational Databases](#relational-databases)
- [NoSQL & Document Databases](#nosql--document-databases)
- [Vector & Memory Stores](#vector--memory-stores)
- [Productivity & Notes](#productivity--notes)
- [Design & Creative](#design--creative)
- [Operations & Infrastructure](#operations--infrastructure)
- [AI & ML Platforms](#ai--ml-platforms)
- [Specialised / Vertical](#specialised--vertical)
- [Frameworks & SDKs for Building MCP Servers](#frameworks--sdks-for-building-mcp-servers)
- [Discovery hubs](#discovery-hubs)

## Official Anthropic Servers

Reference implementations from Anthropic. Source repository:
[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers).

- **[filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** — 🏷️ official ⚠️ mutating 🔒 local
  Read, write, and search files within explicitly-allowed directories.
- **[fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** — 🏷️ official 🛡️ read-only
  Fetch a single URL and return its content as Markdown for the model.
- **[git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** — 🏷️ official ⚠️ mutating 🔒 local
  Read repository state, view diffs, run common git commands.
- **[memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** — 🏷️ official ⚠️ mutating 🔒 local
  Reference knowledge-graph memory server. Persistent JSON-graph store.
- **[sequentialthinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** — 🏷️ official 🛡️ read-only
  Helper that exposes a structured "think step by step" planning tool.
- **[everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything)** — 🏷️ official
  Demo server exercising every MCP feature. Useful for testing clients.

## Brethof MCPs

MCP servers we maintain ourselves. Used internally by Brethof AI day to day.

- **[memory](https://github.com/BrethofAI/memory-mcp)** — 🏷️ brethof ⚠️ mutating 🔒 local
  SurrealDB-backed graph memory with project scoping, semantic search, and
  raw SurrealQL. Replaces the reference Anthropic memory server when you
  need cross-session continuity and graph queries.
- **[claw-code](https://github.com/BrethofAI/claw-code)** — 🏷️ brethof
  Local AI agent MCP exposing 6 MCP tools and 45 gateway tools to Claude
  Code, plus a 13-skill task runner. Bridges Claude Code into a local
  agent loop with adaptive memory.

## Files, Filesystem & Local Data

- **[everything-search](https://github.com/anaisbetts/mcp-everything-search)** — 🏷️ community 🛡️ read-only 🔒 local
  Voidtools `Everything` index integration for instant filesystem search
  on Windows.
- **[applescript](https://github.com/jasonjmcghee/mcp-server-applescript)** — 🏷️ community ⚠️ mutating 🔒 local
  AppleScript bridge for driving Finder, Spotlight, and other macOS apps.
- **[obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** — 🏷️ community ⚠️ mutating 🔒 local
  Read and edit notes in your Obsidian vault.

## Web Search & Browsing

- **[brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)** — 🏷️ official 🛡️ read-only
  Brave Search API integration. Web + local results.
- **[tavily](https://github.com/tavily-ai/tavily-mcp)** — 🏷️ official 🛡️ read-only
  Tavily's research-optimised search API for agents.
- **[exa](https://github.com/exa-labs/exa-mcp-server)** — 🏷️ official 🛡️ read-only
  Exa neural-search API; semantic + similarity search over the web.
- **[perplexity](https://github.com/jsonallen/perplexity-mcp)** — 🏷️ community 🛡️ read-only
  Perplexity Sonar models for grounded web answers.
- **[firecrawl](https://github.com/mendableai/firecrawl-mcp-server)** — 🏷️ official 🛡️ read-only
  Crawl + scrape websites and extract structured data.
- **[duckduckgo](https://github.com/nickclyde/duckduckgo-mcp-server)** — 🏷️ community 🛡️ read-only
  No-tracking search via DuckDuckGo.

## Browser Automation

- **[puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)** — 🏷️ official ⚠️ mutating
  Drive a Chromium browser. Click, type, screenshot, evaluate JS.
- **[playwright](https://github.com/microsoft/playwright-mcp)** — 🏷️ official ⚠️ mutating
  Microsoft's official Playwright MCP. Multi-browser, accessibility-tree
  snapshots designed for agent loops.
- **[browser-use](https://github.com/browser-use/browser-use)** — 🏷️ community ⚠️ mutating
  Vision + DOM-graph hybrid for resilient browser automation.

## Source Control

- **[github](https://github.com/modelcontextprotocol/servers/tree/main/src/github)** — 🏷️ official ⚠️ mutating
  Read repos, manage issues and PRs, push commits via the GitHub API.
- **[gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab)** — 🏷️ official ⚠️ mutating
  GitLab equivalent of the GitHub server.
- **[gitea](https://gitea.com/gitea/mcp-server)** — 🏷️ official ⚠️ mutating
  Self-hosted Gitea instances; full repo + issue + PR control.

## Issue Trackers & Project Management

- **[linear](https://github.com/jerhadf/linear-mcp-server)** — 🏷️ community ⚠️ mutating
  Read and modify Linear issues, projects, cycles, comments.
- **[atlassian](https://www.atlassian.com/blog/announcements/remote-mcp-server)** — 🏷️ official ⚠️ mutating
  First-party Jira + Confluence MCP from Atlassian.
- **[asana](https://github.com/cristip73/mcp-server-asana)** — 🏷️ community ⚠️ mutating
  Tasks, projects, sections, comments via the Asana API.
- **[trello](https://github.com/delorenj/mcp-server-trello)** — 🏷️ community ⚠️ mutating
  Trello board, list, and card operations.

## Communication

- **[slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)** — 🏷️ official ⚠️ mutating
  Read and post Slack messages, manage channels.
- **[discord](https://github.com/SaseQ/discord-mcp)** — 🏷️ community ⚠️ mutating
  Send, search, and moderate Discord messages.
- **[gmail](https://github.com/GongRzhe/Gmail-MCP-Server)** — 🏷️ community ⚠️ mutating
  Read, send, and search Gmail. Requires Google OAuth setup.
- **[telegram](https://github.com/chigwell/telegram-mcp)** — 🏷️ community ⚠️ mutating
  Send and read messages via Telegram bots.

## Relational Databases

- **[postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)** — 🏷️ official 🛡️ read-only
  Reference Postgres server: read-only SELECT against the configured DB.
- **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** — 🏷️ community ⚠️ mutating
  Crystal DBA's Postgres MCP with schema mutation and tuning advisors.
- **[sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)** — 🏷️ official ⚠️ mutating 🔒 local
  Read and modify a local SQLite database.
- **[mysql](https://github.com/benborla/mcp-server-mysql)** — 🏷️ community ⚠️ mutating
  MySQL/MariaDB read + write with safe-mode toggle.
- **[clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** — 🏷️ official 🛡️ read-only
  ClickHouse analytics queries with first-party SQL safety guardrails.

## NoSQL & Document Databases

- **[mongodb](https://github.com/mongodb-developer/mongodb-mcp-server)** — 🏷️ official ⚠️ mutating
  MongoDB query, aggregation, and CRUD.
- **[redis](https://github.com/modelcontextprotocol/servers/tree/main/src/redis)** — 🏷️ official ⚠️ mutating
  Redis keys, hashes, streams, pub/sub.
- **[surrealdb](https://github.com/aichipped/surrealdb-mcp-server)** — 🏷️ community ⚠️ mutating
  SurrealDB graph + document queries via SurrealQL.
- **[neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** — 🏷️ community ⚠️ mutating
  Neo4j Cypher query execution and schema introspection.

## Vector & Memory Stores

- **[chroma](https://github.com/chroma-core/chroma-mcp)** — 🏷️ official ⚠️ mutating 🔒 local
  ChromaDB collections, similarity search, persistent embeddings.
- **[qdrant](https://github.com/qdrant/mcp-server-qdrant)** — 🏷️ official ⚠️ mutating
  Qdrant vector search and collection management.
- **[pinecone](https://github.com/pinecone-io/pinecone-mcp)** — 🏷️ official ⚠️ mutating
  Pinecone managed vector search.
- **[weaviate](https://github.com/weaviate/mcp-server-weaviate)** — 🏷️ official ⚠️ mutating
  Weaviate hybrid (vector + keyword) retrieval.

## Productivity & Notes

- **[notion](https://github.com/makenotion/notion-mcp-server)** — 🏷️ official ⚠️ mutating
  Notion's first-party MCP. Read, edit, search pages and databases.
- **[google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive)** — 🏷️ official 🛡️ read-only
  Search and read Google Drive files.
- **[google-calendar](https://github.com/nspady/google-calendar-mcp)** — 🏷️ community ⚠️ mutating
  Read and create calendar events.
- **[apple-notes](https://github.com/sirmews/apple-notes-mcp)** — 🏷️ community 🛡️ read-only 🔒 local
  Read Apple Notes on macOS.
- **[airtable](https://github.com/felores/airtable-mcp)** — 🏷️ community ⚠️ mutating
  Airtable bases, tables, records.

## Design & Creative

- **[figma](https://www.figma.com/blog/mcp-figma-design-context-claude/)** — 🏷️ official 🛡️ read-only
  Figma's first-party MCP. Read design files, components, and variables
  to ground code-generation in real designs.
- **[blender-mcp](https://github.com/ahujasid/blender-mcp)** — 🏷️ community ⚠️ mutating 🔒 local
  Drive Blender via Python — modify scenes, run renders, manage assets.

## Operations & Infrastructure

- **[kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** — 🏷️ community ⚠️ mutating
  kubectl-equivalent operations on the configured cluster.
- **[helm](https://github.com/zekker6/mcp-helm)** — 🏷️ community ⚠️ mutating
  Manage Helm releases against a Kubernetes cluster.
- **[docker](https://github.com/QuantGeekDev/docker-mcp)** — 🏷️ community ⚠️ mutating 🔒 local
  Inspect, run, build, and remove containers via the local Docker daemon.
- **[aws](https://github.com/awslabs/mcp)** — 🏷️ official ⚠️ mutating
  Amazon-published MCPs covering AWS service catalog, Bedrock, S3, etc.

## AI & ML Platforms

- **[huggingface](https://github.com/evalstate/mcp-hfspace)** — 🏷️ community ⚠️ mutating
  Use HuggingFace Spaces as MCP-callable tools.
- **[ollama](https://github.com/NightTrek/Ollama-mcp)** — 🏷️ community ⚠️ mutating 🔒 local
  Pull, run, and manage Ollama models locally.
- **[lmstudio](https://lmstudio.ai/blog/lmstudio-v0.3.17)** — 🏷️ official ⚠️ mutating 🔒 local
  LM Studio's built-in MCP host (since v0.3.17). Run local models as
  MCP tools.

## Specialised / Vertical

- **[stripe](https://github.com/stripe/agent-toolkit)** — 🏷️ official ⚠️ mutating
  Stripe payments, customers, subscriptions, refunds. Includes safety
  rails for production keys.
- **[plaid](https://github.com/plaid/agent-toolkit)** — 🏷️ official 🛡️ read-only
  Banking data via Plaid for finance agents.
- **[quickbooks](https://github.com/notocrats/quickbooks-mcp)** — 🏷️ community ⚠️ mutating
  QuickBooks Online integration for accounting workflows.
- **[google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps)** — 🏷️ official 🛡️ read-only
  Google Maps directions, places, geocoding.
- **[spotify](https://github.com/varunneal/spotify-mcp)** — 🏷️ community ⚠️ mutating
  Spotify Web API: search, queue, playlists.

## Frameworks & SDKs for Building MCP Servers

- **[mcp-python](https://github.com/modelcontextprotocol/python-sdk)** — 🏷️ official
  Reference Python SDK. Includes `FastMCP` for terse decorator-based
  servers.
- **[mcp-typescript](https://github.com/modelcontextprotocol/typescript-sdk)** — 🏷️ official
  Reference TypeScript / Node SDK. Powers most npm-distributed servers.
- **[mcp-go](https://github.com/modelcontextprotocol/go-sdk)** — 🏷️ official
  Go SDK for building MCP servers. Single-binary deployment friendly.
- **[fastmcp](https://github.com/jlowin/fastmcp)** — 🏷️ community
  Originally-third-party Python framework that became the inspiration
  for the official `FastMCP` integration.
- **[mcp-rust](https://github.com/jeanlucthumm/mcp-rust)** — 🏷️ community
  Rust SDK for building servers with low memory + fast startup.

## Discovery hubs

Where to look for new servers as the ecosystem grows.

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** — Anthropic's reference servers + a list of community ones at the bottom.
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** — Largest community list. Less curation than ours; useful for completeness.
- **[Smithery](https://smithery.ai)** — Hosted MCP-server registry with one-click install for many clients.
- **[mcp.so](https://mcp.so)** — Searchable directory of public MCP servers.

## Related work

- **[awesome-llms-txt](https://github.com/BrethofAI/awesome-llms-txt)** — Tools that make themselves discoverable to AI agents.
- **[awesome-ai-coding-agents](https://github.com/BrethofAI/awesome-ai-coding-agents)** — Honest comparison of AI coding assistants. Most of them either ship MCP-host support or are themselves embeddable as MCP servers.

## Contributing

Open an issue with the server name, repo URL, what category it belongs
to, and one paragraph on what makes it worth listing. We will not list
servers that have not had a maintained release in the last 6 months
unless the maintainer explicitly tells us they're keeping it alive.

## License

[MIT](LICENSE).

---

Maintained by **[Brethof AI](https://brethof.com)** — AI tools built for
people who take their data seriously.
