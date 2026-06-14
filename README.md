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

- [Official Anthropic Servers](#official-anthropic-servers) (6)
- [Files, Filesystem & Local Data](#files-filesystem--local-data) (1)
- [Web Search & Browsing](#web-search--browsing) (5)
- [Browser Automation](#browser-automation) (2)
- [Source Control](#source-control) (1)
- [Issue Trackers & Project Management](#issue-trackers--project-management) (4)
- [Communication](#communication) (3)
- [Relational Databases](#relational-databases) (3)
- [NoSQL & Document Databases](#nosql--document-databases) (2)
- [Vector & Memory Stores](#vector--memory-stores) (4)
- [Productivity & Notes](#productivity--notes) (4)
- [Design & Creative](#design--creative) (1)
- [Operations & Infrastructure](#operations--infrastructure) (4)
- [AI & ML Platforms](#ai--ml-platforms) (3)
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
- [Helium MCP](https://github.com/connerlambden/helium-mcp) — Real-time news with 37-dimension bias scoring, ML options pricing, and live market data. [Interactive demo](https://connerlambden.github.io/helium-news-explorer/) · [REST API](https://heliumtrades.com/mcp-page/)

## Files, Filesystem & Local Data

- **[obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** — 🏷️ community ⚠️ mutating 🔒 local  
  Read and edit notes in your Obsidian vault.

## Web Search & Browsing

- **[duckduckgo](https://github.com/nickclyde/duckduckgo-mcp-server)** — 🏷️ community 🛡️ read-only  
  No-tracking search via DuckDuckGo.
- **[exa](https://github.com/exa-labs/exa-mcp-server)** — 🏷️ official 🛡️ read-only  
  Exa neural-search API; semantic + similarity search over the web.
- **[firecrawl](https://github.com/mendableai/firecrawl-mcp-server)** — 🏷️ official 🛡️ read-only  
  Crawl + scrape websites and extract structured data.
- **[perplexity](https://github.com/jsonallen/perplexity-mcp)** — 🏷️ community 🛡️ read-only  
  Perplexity Sonar models for grounded web answers.
- **[tavily](https://github.com/tavily-ai/tavily-mcp)** — 🏷️ official 🛡️ read-only  
  Tavily's research-optimised search API for agents.

## Browser Automation

- **[browser-use](https://github.com/browser-use/browser-use)** — 🏷️ community ⚠️ mutating  
  Vision + DOM-graph hybrid for resilient browser automation.
- **[playwright](https://github.com/microsoft/playwright-mcp)** — 🏷️ official ⚠️ mutating  
  Microsoft's official Playwright MCP. Multi-browser, accessibility-tree snapshots designed for agent loops.

## Source Control

- **[gitea](https://gitea.com/gitea/mcp-server)** — 🏷️ official ⚠️ mutating  
  Self-hosted Gitea instances; full repo + issue + PR control.

## Issue Trackers & Project Management

- **[asana](https://github.com/cristip73/mcp-server-asana)** — 🏷️ community ⚠️ mutating  
  Tasks, projects, sections, comments via the Asana API.
- **[atlassian](https://www.atlassian.com/blog/announcements/remote-mcp-server)** — 🏷️ official ⚠️ mutating  
  First-party Jira + Confluence MCP from Atlassian.
- **[linear](https://github.com/jerhadf/linear-mcp-server)** — 🏷️ community ⚠️ mutating  
  Read and modify Linear issues, projects, cycles, comments.
- **[trello](https://github.com/delorenj/mcp-server-trello)** — 🏷️ community ⚠️ mutating  
  Trello board, list, and card operations.

## Communication

- **[discord](https://github.com/SaseQ/discord-mcp)** — 🏷️ community ⚠️ mutating  
  Send, search, and moderate Discord messages.
- **[gmail](https://github.com/GongRzhe/Gmail-MCP-Server)** — 🏷️ community ⚠️ mutating  
  Read, send, and search Gmail. Requires Google OAuth setup.
- **[telegram](https://github.com/chigwell/telegram-mcp)** — 🏷️ community ⚠️ mutating  
  Send and read messages via Telegram bots.

## Relational Databases

- **[clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** — 🏷️ official 🛡️ read-only  
  ClickHouse analytics queries with first-party SQL safety guardrails.
- **[mysql](https://github.com/benborla/mcp-server-mysql)** — 🏷️ community ⚠️ mutating  
  MySQL/MariaDB read + write with safe-mode toggle.
- **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** — 🏷️ community ⚠️ mutating  
  Crystal DBA's Postgres MCP with schema mutation and tuning advisors.

## NoSQL & Document Databases

- **[mongodb](https://github.com/mongodb-developer/mongodb-mcp-server)** — 🏷️ official ⚠️ mutating  
  MongoDB query, aggregation, and CRUD.
- **[neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** — 🏷️ community ⚠️ mutating  
  Neo4j Cypher query execution and schema introspection.

## Vector & Memory Stores

- **[chroma](https://github.com/chroma-core/chroma-mcp)** — 🏷️ official ⚠️ mutating 🔒 local  
  ChromaDB collections, similarity search, persistent embeddings.
- **[pinecone](https://github.com/pinecone-io/pinecone-mcp)** — 🏷️ official ⚠️ mutating  
  Pinecone managed vector search.
- **[qdrant](https://github.com/qdrant/mcp-server-qdrant)** — 🏷️ official ⚠️ mutating  
  Qdrant vector search and collection management.
- **[weaviate](https://github.com/weaviate/mcp-server-weaviate)** — 🏷️ official ⚠️ mutating  
  Weaviate hybrid (vector + keyword) retrieval.

## Productivity & Notes

- **[airtable](https://github.com/felores/airtable-mcp)** — 🏷️ community ⚠️ mutating  
  Airtable bases, tables, records.
- **[apple-notes](https://github.com/sirmews/apple-notes-mcp)** — 🏷️ community 🛡️ read-only 🔒 local  
  Read Apple Notes on macOS.
- **[google-calendar](https://github.com/nspady/google-calendar-mcp)** — 🏷️ community ⚠️ mutating  
  Read and create calendar events.
- **[notion](https://github.com/makenotion/notion-mcp-server)** — 🏷️ official ⚠️ mutating  
  Notion's first-party MCP. Read, edit, search pages and databases.

## Design & Creative

- **[blender-mcp](https://github.com/ahujasid/blender-mcp)** — 🏷️ community ⚠️ mutating 🔒 local  
  Drive Blender via Python — modify scenes, run renders, manage assets.

## Operations & Infrastructure

- **[aws](https://github.com/awslabs/mcp)** — 🏷️ official ⚠️ mutating  
  Amazon-published MCPs covering AWS service catalog, Bedrock, S3, etc.
- **[docker](https://github.com/QuantGeekDev/docker-mcp)** — 🏷️ community ⚠️ mutating 🔒 local  
  Inspect, run, build, and remove containers via the local Docker daemon.
- **[helm](https://github.com/zekker6/mcp-helm)** — 🏷️ community ⚠️ mutating  
  Manage Helm releases against a Kubernetes cluster.
- **[kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** — 🏷️ community ⚠️ mutating  
  kubectl-equivalent operations on the configured cluster.

## AI & ML Platforms

- **[huggingface](https://github.com/evalstate/mcp-hfspace)** — 🏷️ community ⚠️ mutating  
  Use HuggingFace Spaces as MCP-callable tools.
- **[lmstudio](https://lmstudio.ai/blog/lmstudio-v0.3.17)** — 🏷️ official ⚠️ mutating 🔒 local  
  LM Studio's built-in MCP host (since v0.3.17). Run local models as MCP tools.
- **[ollama](https://github.com/NightTrek/Ollama-mcp)** — 🏷️ community ⚠️ mutating 🔒 local  
  Pull, run, and manage Ollama models locally.

## Specialised / Vertical

- **[spotify](https://github.com/varunneal/spotify-mcp)** — 🏷️ community ⚠️ mutating  
  Spotify Web API: search, queue, playlists.
- **[stripe](https://github.com/stripe/agent-toolkit)** — 🏷️ official ⚠️ mutating  
  Stripe payments, customers, subscriptions, refunds. Includes safety rails for production keys.

## Frameworks & SDKs for Building MCP Servers

- **[fastmcp](https://github.com/jlowin/fastmcp)** — 🏷️ community  
  Originally-third-party Python framework that became the inspiration for the official `FastMCP` integration.
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
