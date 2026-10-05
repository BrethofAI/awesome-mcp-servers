# awesome-mcp-servers

> Working MCP servers for Claude Desktop, Claude Code, the Claude Agent SDK, and other MCP-compatible clients in 2026, each labelled with who publishes it, where it runs, and what it can change.

Maintained by [Brethof AI](https://brethof.ai). Companion to
[awesome-llms-txt](https://github.com/BrethofAI/awesome-llms-txt) and
[awesome-ai-coding-agents](https://github.com/BrethofAI/awesome-ai-coding-agents).

## Why this list exists

The Model Context Protocol ([spec](https://modelcontextprotocol.io)) lets
LLM clients call out to external tools and data sources through a uniform
interface. By 2026 there are hundreds of MCP servers, and many hide what they
actually do. This list is a catalog: it takes every submission that is

- **Real** — there is code to read or install, or a documented hosted
  endpoint that answers.
- **Working** — it connects from an MCP client such as Claude Desktop or
  Claude Code.
- **Honest** — what it says it does holds up.
- **In scope** — it is an MCP server.

New, small, and single-vendor servers are welcome. Instead of filtering by
taste, we label every entry: who publishes it, where it runs, what it can
change, and whether it needs a paid account. Licences are named when they
are not OSI open source, or when there is no public source at all.

We decline only:

1. Nothing real to point at — no code and no documented, reachable endpoint.
2. Crypto pay-per-call or wallet-signing servers (x402 and similar).
3. Misleading claims we can't label around.
4. Off-topic submissions and spam.

Entries that stop working are removed by our weekly check. Where several
builds of the same server exist, we link the most-recently-maintained
official one; if forks compete, the most active fork wins.

## Legend

- 🏷️ `official` — published by the originating company (Anthropic, Stripe,
  Atlassian, etc.) or the project itself.
- 🏷️ `community` — third-party server, not published by the company or
  project it connects to.
- 🏷️ `brethof` — maintained by Brethof AI.
- 🛡️ `read-only` — server cannot mutate anything in the connected system.
- ⚠️ `mutating` — server can write, send, or modify state. Authorise with care.
- 🔒 `local` — runs entirely on your machine, no remote calls during use.
- ☁️ `hosted` — runs on the vendor's servers; you connect to their endpoint.
- 💰 `paid` — needs a paid account (a time-limited trial doesn't count as free).
- 🆕 `new` — listed in the last 60 days.

<!-- LIST:START -->
## Contents

- [Official Anthropic Servers](#official-anthropic-servers) (7)
- [Files, Filesystem & Local Data](#files-filesystem--local-data) (1)
- [Web Search & Browsing](#web-search--browsing) (8)
- [Browser Automation](#browser-automation) (3)
- [Source Control](#source-control) (2)
- [Issue Trackers & Project Management](#issue-trackers--project-management) (5)
- [Communication](#communication) (6)
- [Relational Databases](#relational-databases) (4)
- [NoSQL & Document Databases](#nosql--document-databases) (2)
- [Vector & Memory Stores](#vector--memory-stores) (7)
- [Productivity & Notes](#productivity--notes) (6)
- [Design & Creative](#design--creative) (3)
- [Operations & Infrastructure](#operations--infrastructure) (7)
- [AI & ML Platforms](#ai--ml-platforms) (4)
- [Specialised / Vertical](#specialised--vertical) (11)
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
- **[time](https://github.com/modelcontextprotocol/servers/tree/main/src/time)** — 🆕 new 🏷️ official 🛡️ read-only 🔒 local  
  Current time and timezone conversion (`get_current_time`, `convert_time`).

## Files, Filesystem & Local Data

- **[obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** — 🏷️ community ⚠️ mutating 🔒 local  
  Read and edit notes in your Obsidian vault.

## Web Search & Browsing

- **[brave-search](https://github.com/brave/brave-search-mcp-server)** — 🆕 new 🏷️ official 🛡️ read-only  
  Brave's official server for the Brave Search API: web, local, image, video, and news search plus summarizer; needs `BRAVE_API_KEY`. Replaces the archived reference Brave server.
- **[communicate-docs](https://developer.communicate.so/docs/mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Communicate's public developer-docs server: three read-only tools for its developer guide, OpenAPI summary, and support contact. Hosted at `https://communicate.so/mcp`, no auth; it cannot reach workspaces or send messages. No public source.
- **[context7](https://github.com/upstash/context7)** — 🆕 new 🏷️ official 🛡️ read-only  
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
- **[chrome-devtools](https://github.com/ChromeDevTools/chrome-devtools-mcp)** — 🆕 new 🏷️ official ⚠️ mutating  
  Chrome DevTools team's server: control and inspect a live Chrome for automation, debugging (network, console, screenshots), and performance traces. Sends usage statistics to Google by default (`--no-usage-statistics` opts out).
- **[playwright](https://github.com/microsoft/playwright-mcp)** — 🏷️ official ⚠️ mutating  
  Microsoft's official Playwright MCP. Multi-browser, accessibility-tree snapshots designed for agent loops.

## Source Control

- **[gitea](https://gitea.com/gitea/gitea-mcp)** — 🏷️ official ⚠️ mutating  
  Self-hosted Gitea instances; full repo + issue + PR control.
- **[github](https://github.com/github/github-mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating  
  GitHub's official server: repos, issues, pull requests, Actions, code security, grouped into toolsets. Local binary or remote at `https://api.githubcopilot.com/mcp/`; `--read-only` drops all write tools.

## Issue Trackers & Project Management

- **[asana](https://developers.asana.com/docs/using-asanas-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Asana's hosted MCP server (`https://mcp.asana.com/v2/mcp`): tasks, projects, reports. OAuth; replaces the deprecated `/sse` beta endpoint.
- **[atlassian](https://github.com/atlassian/atlassian-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Atlassian's official remote MCP server: Jira, Confluence, Jira Service Management, Bitbucket, Compass. OAuth 2.1 or API tokens.
- **[linear](https://linear.app/docs/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Linear's hosted MCP server (`https://mcp.linear.app/mcp`; read-only variant at `/mcp/readonly`): issues, projects, cycles, comments. OAuth 2.1 or API key.
- **[orbit](https://github.com/Noveum/orbit/blob/main/docs/mcp.md)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Open-source task manager (issues, boards, sprints, projects, docs) with an MCP server. The `orbit.write` scope creates and updates issues, comments, projects, and sprints. Hosted free at `https://orbit.noveum.ai/mcp` (OAuth), or self-host it (self-hosting is in preview). Apache-2.0.
- **[trello](https://github.com/delorenj/mcp-server-trello)** — 🏷️ community ⚠️ mutating  
  Trello board, list, and card operations.

## Communication

- **[autoposting](https://docs.autoposting.ai/mcp/overview)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Draft, schedule, and publish social posts (X, LinkedIn, Instagram, Threads, YouTube), carousels, and video clips. Hosted at `https://app.autoposting.ai/mcp` (OAuth 2.1); the tools you see depend on the scopes you grant, and some are destructive. Needs a paid Autoposting plan. No public server source or licence.
- **[bulkpublish](https://github.com/azeemkafridi/bulkpublish-api/tree/main/mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Schedule and publish social posts to 15 platforms, upload media, and read analytics. 72 tools in the MIT stdio server (`@bulkpublish/mcp-server`); a 20-tool core set is hosted at `https://mcp.bulkpublish.com/mcp` (OAuth 2.1). There is a free plan.
- **[discord](https://github.com/SaseQ/discord-mcp)** — 🏷️ community ⚠️ mutating  
  Send, search, and moderate Discord messages.
- **[google-workspace](https://github.com/taylorwilsdon/google_workspace_mcp)** — 🏷️ community ⚠️ mutating  
  Gmail, Calendar, Drive, Docs, Sheets, Chat and more behind one server (120+ tools in core/extended/complete tiers). Uses your own Google OAuth client.
- **[slack](https://docs.slack.dev/ai/slack-mcp-server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
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
- **[supabase](https://github.com/supabase/mcp)** — 🆕 new 🏷️ official ⚠️ mutating  
  Supabase's official server (`https://mcp.supabase.com/mcp`): database, docs, and project tools. Scope it with `project_ref` and `read_only=true`.

## NoSQL & Document Databases

- **[mongodb](https://github.com/mongodb-js/mongodb-mcp-server)** — 🏷️ official ⚠️ mutating  
  MongoDB's official server for databases and Atlas clusters: query, aggregation, CRUD. `--readOnly` restricts it to read tools.
- **[neo4j](https://github.com/neo4j/mcp)** — 🏷️ official ⚠️ mutating  
  Neo4j's official server: `read-cypher` and `write-cypher` tools against your graph; `NEO4J_MCP_READ_ONLY=true` disables writes.

## Vector & Memory Stores

- **[brethof-brain](https://brethof.ai/brain/)** — 🆕 new 🏷️ brethof ⚠️ mutating ☁️ hosted  
  Persistent memory for AI agents across sessions, projects and machines. Every session opens with a brief — your standing rules, what each project is, where the last sessions stopped — and the records that bear on a prompt arrive with it. It curates itself into records per project, keeps the full chat history searchable, and adds notes, playbooks and an optional graph of decisions: each one dated, with its reason and what it replaced, returned alongside search results. Proven on nine platforms: Claude Code (Linux, Windows), Codex, Qwen Code, Cline, OpenCode, Kilo Code, OpenClaw, Hermes Agent and dsh. Memory lives on your machine (local edition, Docker or Podman) or encrypted under a passphrase only you hold (hosted); each exchange is processed by our hub, which keeps none of it. Free tier; the client is source-available. Disclosure: maintained by us.
- **[chroma](https://github.com/chroma-core/chroma-mcp)** — 🏷️ official ⚠️ mutating 🔒 local  
  ChromaDB collections, similarity search, persistent embeddings. Still in Chroma's docs, but no release since v0.2.6 (Aug 2025).
- **[claimidx](https://github.com/claimidx/claimidx)** — 🆕 new 🏷️ official ⚠️ mutating  
  Shared index of known software failures and their fixes, for coding agents: ask before retrying, then record the fix. Runs locally (PyPI `claimidx`, Apache-2.0) but connects to a public commons at home.claimidx.com by default and syncs with it at session start. Since v0.7.14, publishing a claim to the commons asks for confirmation (earlier versions shared automatically); `CLAIMIDX_COMMONS=0` turns the commons off.
- **[contextstream](https://github.com/contextstream/mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Persistent memory and code search for coding agents: saves decisions, lessons, and plans across sessions. Indexing sends your source code to ContextStream's hosted service, and transcript saving and Git metadata capture are on by default. The client is MIT; the hosted backend is closed. Free starting credits.
- **[pinecone](https://github.com/pinecone-io/pinecone-mcp)** — 🏷️ official ⚠️ mutating  
  Pinecone managed vector search.
- **[qdrant](https://github.com/qdrant/mcp-server-qdrant)** — 🏷️ official ⚠️ mutating  
  Qdrant vector search and collection management.
- **[weaviate](https://docs.weaviate.io/weaviate/configuration/mcp-server)** — 🏷️ official ⚠️ mutating  
  MCP server built into Weaviate (preview from v1.37.1; `MCP_SERVER_ENABLED=true`, served at `/v1/mcp`): hybrid search, collection config, object upsert; respects RBAC. Replaces the deprecated standalone server.

## Productivity & Notes

- **[airtable](https://support.airtable.com/articles/9897799762-using-the-airtable-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Airtable's hosted MCP server (`https://mcp.airtable.com/mcp`): bases, tables, records. OAuth or personal access token.
- **[apple-notes](https://github.com/sweetrb/apple-notes-mcp)** — 🏷️ community ⚠️ mutating 🔒 local  
  Read, search, create, edit, and organise Apple Notes on macOS via AppleScript.
- **[google-calendar](https://github.com/nspady/google-calendar-mcp)** — 🏷️ community ⚠️ mutating  
  Read and create calendar events.
- **[notion](https://developers.notion.com/docs/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Notion's hosted MCP server: search the workspace, read and edit pages in Markdown. OAuth, respects each user's existing permissions. (The self-hosted makenotion/notion-mcp-server is no longer maintained.)
- **[process-street](https://www.process.st/help/docs/mcp-server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Process Street's hosted server: workflows, workflow runs, tasks, users, and data sets. It can create and manage runs and assigned tasks within your Process Street permissions. `https://mcp.process.st/` (interactive auth or API key). Needs a paid plan after a 14-day trial; organisations that require SAML SSO are not supported. No public source.
- **[screenpipe](https://github.com/screenpipe/screenpipe/tree/main/packages/screenpipe-mcp)** — 🆕 new 🏷️ official ⚠️ mutating  
  Search your recorded screen text, audio transcripts, meetings, and activity summaries; can also control recording, run pipes, and edit memories. Reads your full screen and audio history, so grant it with care. Source-available under the Screenpipe Commercial License (not an OSI open-source licence).

## Design & Creative

- **[cadre](https://github.com/ArthurBrioche/cadre-video-editor-plugin)** — 🆕 new 🏷️ official ⚠️ mutating 🔒 local  
  Bridge to Cadre, a screen recorder and non-destructive video editor for Apple Silicon Macs: start and stop recordings, then apply cuts, zooms, captions, and styling, preview, and export MP4 through the running app. The bridge is MIT; Cadre itself is proprietary, and export needs a Cadre Pro subscription.
- **[mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)** — 🏷️ community ⚠️ mutating 🔒 local  
  Drive Blender via Python — modify scenes, run renders, manage assets. Formerly blender-mcp; the PyPI package is now `mcp-for-blender`.
- **[orkas-video-studio](https://github.com/Orkas-AI/Orkas-VideoStudio)** — 🆕 new 🏷️ official ⚠️ mutating  
  Local-first video toolkit for coding agents: compose, edit, generate, and assemble videos from an editable `plan.json` timeline, through a CLI and an MCP server. Early development: install from source, since the npm packages aren't published yet. Optional generation calls providers with your own keys. MIT.

## Operations & Infrastructure

- **[aws](https://github.com/awslabs/mcp)** — 🏷️ official ⚠️ mutating  
  Amazon-published MCPs covering AWS service catalog, Bedrock, S3, etc.
- **[docker-mcp-gateway](https://github.com/docker/mcp-gateway)** — 🏷️ official ⚠️ mutating  
  Docker's MCP Toolkit CLI plugin (`docker mcp`): runs catalog MCP servers in isolated containers behind one gateway, with Docker Desktop secrets management.
- **[grafana](https://github.com/grafana/mcp-grafana)** — 🆕 new 🏷️ official ⚠️ mutating  
  Grafana's official server: dashboards, datasource queries, incidents, annotations. Can create and update dashboards and incidents; `--disable-write` makes it read-only.
- **[helm](https://github.com/zekker6/mcp-helm)** — 🏷️ community ⚠️ mutating  
  Manage Helm releases against a Kubernetes cluster.
- **[kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** — 🏷️ community ⚠️ mutating  
  kubectl-equivalent operations on the configured cluster.
- **[sentry](https://github.com/getsentry/toolkit)** — 🆕 new 🏷️ official ⚠️ mutating  
  Sentry's official server: issues, events, projects, alerts and monitors; can update issues and create projects. Remote at `https://mcp.sentry.dev/mcp` or stdio. Licence: FSL-1.1-Apache-2.0.
- **[shipvela](https://github.com/stefanautomateed/shipvela-codex)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Public beta. Create hosting projects, deploy a connected GitHub repo or a small static site, and read deployment status, build logs, and usage. Hosted at `https://shipvela.com/mcp` (OAuth with PKCE); free Hobby plan, and each publish counts against your plan's allowance. Plugin files are MIT per the README; the hosted service is proprietary.

## AI & ML Platforms

- **[aident-loadout](https://github.com/Aident-AI/aident-skill)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Gateway that lets an agent use 1,000+ third-party apps and tools (Gmail, Slack, Linear, Notion, HubSpot, and more) through your connected accounts, with credentials in Aident's vault and an audit history. Hosted at `https://loadout.aident.ai/mcp` (OAuth); free to start, with top-ups for more usage. The skill repo is MIT; the service is proprietary.
- **[api-market](https://api.market/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Gateway to the API.market catalogue of 580+ third-party APIs (image and video generation, search, scraping, maps, data) through five tools. Hosted at `https://api.market/api/mcp/gateway` (OAuth or API key). Calls can spend quota or wallet funds and change subscriptions. Proprietary; no public source.
- **[huggingface](https://github.com/huggingface/hf-mcp-server)** — 🏷️ official ⚠️ mutating  
  Hugging Face's official server: Hub search and details, plus Gradio Spaces as tools. Hosted at `https://hf.co/mcp` or run locally.
- **[runapi](https://github.com/runapi-ai/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Browse a catalog of image, video, music, and text-to-speech models, check current pricing, and create and poll generation jobs. Hosted at `https://mcp.runapi.ai/mcp` or local via `npx @runapi.ai/mcp`. Catalog tools work without sign-in; jobs spend prepaid pay-as-you-go credits.

## Specialised / Vertical

- **[careclinic](https://careclinic.io/careclinic-mcp/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Your CareClinic health record in chat: today's medication schedule, recent symptoms and mood, and insights. A check-in tool logs entries after you confirm them. Hosted at `https://mcp.careclinic.io/mcp` (OAuth with your CareClinic account). Handles personal health data. No public source; the repo is all rights reserved.
- **[invompt](https://github.com/Invompt/invompt-mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Create, revise, archive, and email invoices, quotes, estimates, and pro formas from chat. Hosted at `https://mcp.invompt.com/mcp` (OAuth); you can start without an account, but emailing documents needs a registered one. The MIT repo also has a local-beta CLI.
- **[kleap](https://github.com/kleaphq/cli)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  No-code website builder: create, edit, and publish sites, manage files, site databases, and custom domains (including a `buy_domain` tool). Hosted at `https://kleap.co/api/mcp` (OAuth) or a local stdio server from the MIT CLI; read-only API keys are available. AI edits use Kleap credits; there is a free plan.
- **[llm-pulse](https://llmpulse.ai/features/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  AI-search visibility analytics: brand mentions, citations, sentiment, and share of voice. With the write scope it can add prompts, competitors, tags, and annotations, and launch content tasks. Hosted at `https://api.llmpulse.ai/api/v1/mcp` (OAuth or API key). Needs a paid LLM Pulse plan after a 14-day trial. The server source is private; the repo holds an MIT stdio wrapper.
- **[pocket-drives](https://github.com/RevList/pocket-drives-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Search, quote, and check availability for peer-to-peer luxury, exotic, and EV car rentals from independent hosts (five US markets at listing time). Hosted at `https://pocketdrives.ai/mcp`, no auth; it does not book, which happens in the iOS app. No public source or licence.
- **[robot-speed](https://www.robot-speed.com/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  SEO tools: 12 free audit tools with no account at `https://www.robot-speed.com/api/mcp/free`; the full 39-tool server at `/api/mcp` (OAuth) also manages content, Search Console data, and reports, and needs a Robot Speed subscription after its trial. No public server source.
- **[spotify](https://github.com/varunneal/spotify-mcp)** — 🏷️ community ⚠️ mutating  
  Spotify Web API: search, queue, playlists.
- **[statsnet](https://github.com/usenetstate/statsnet-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Company background checks worldwide: registration, executives, government contracts, courts, and finances (`search_companies`, `get_company`). Hosted at `https://statsnet.co/mcp`; the public company card needs no auth, while contacts, relations, and exports need a Statsnet subscription. No public server source.
- **[stripe](https://docs.stripe.com/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Stripe's hosted MCP server (`https://mcp.stripe.com`): payments, customers, subscriptions, refunds via OAuth or agent API keys. Refunds and outbound payments need human confirmation. From 2026-10-31 it accepts only Agent-tagged keys or OAuth.
- **[trends-mcp](https://github.com/trendsmcp-ai/Trends-MCP)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Live trend data from Google Search, YouTube, TikTok, Reddit, Amazon, Wikipedia, news, app stores, npm, Steam, and more (`get_time_series`, `get_growth`, `get_top_trends`). Hosted at `https://api.trendsmcp.ai/mcp` or through the repo's MIT stdio adapter. Needs an API key, which comes with a free monthly quota.
- **[wine-labs](https://winelabs.ai/agents)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Fine-wine market data: wine and LWIN matching, retail and auction prices, exchange order books, merchants, and critic data. Account-scoped cellar and portfolio workflows can create or update data. Hosted at `https://chat.wine-labs.com/mcp` (browser OAuth); free tier, with deeper workflows on paid plans. No public server source.

## Frameworks & SDKs for Building MCP Servers

- **[fastmcp](https://github.com/PrefectHQ/fastmcp)** — 🏷️ community  
  Python framework for MCP servers and clients, now under PrefectHQ. FastMCP 1.0 was incorporated into the official Python SDK in 2024; this is the actively maintained standalone project.
- **[mcp-go](https://github.com/modelcontextprotocol/go-sdk)** — 🏷️ official  
  Go SDK for building MCP servers. Single-binary deployment friendly.
- **[mcp-python](https://github.com/modelcontextprotocol/python-sdk)** — 🏷️ official  
  Reference Python SDK. Includes `FastMCP` for terse decorator-based servers.
- **[mcp-typescript](https://github.com/modelcontextprotocol/typescript-sdk)** — 🏷️ official  
  Reference TypeScript / Node SDK. Powers most npm-distributed servers.

<!-- LIST:END -->

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
not the list above. If you built the server, say so in the issue.

## License

[MIT](LICENSE).

---

Maintained by **[Brethof AI](https://brethof.ai)** — AI tools built for
people who take their data seriously.
