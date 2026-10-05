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

- [Reference servers (MCP steering group)](#reference-servers-mcp-steering-group) (7)
- [Files, Filesystem & Local Data](#files-filesystem--local-data) (1)
- [Web Search & Browsing](#web-search--browsing) (9)
- [Browser Automation](#browser-automation) (3)
- [Source Control](#source-control) (3)
- [Issue Trackers & Project Management](#issue-trackers--project-management) (5)
- [Communication](#communication) (7)
- [Relational Databases](#relational-databases) (4)
- [NoSQL & Document Databases](#nosql--document-databases) (2)
- [Vector & Memory Stores](#vector--memory-stores) (7)
- [Productivity & Notes](#productivity--notes) (7)
- [Design & Creative](#design--creative) (4)
- [Operations & Infrastructure](#operations--infrastructure) (11)
- [AI & ML Platforms](#ai--ml-platforms) (4)
- [Specialised / Vertical](#specialised--vertical) (12)
- [Frameworks & SDKs for Building MCP Servers](#frameworks--sdks-for-building-mcp-servers) (4)

<!-- The list below is generated from entries/*.yaml by scripts/gen_awesome_readme.py. Edit the YAML, not this section. -->

## Reference servers (MCP steering group)

Reference implementations maintained by the MCP steering group, kept in [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers). (Several earlier reference servers — github, slack, postgres, gdrive and others — have moved to their vendors' own MCP servers or the project's archive; we list them under their current homes as they're re-verified.)

- **[everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything)** — 🏷️ official  
  Demo server exercising every MCP feature. Useful for testing clients.
- **[fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** — 🏷️ official 🛡️ read-only  
  Fetch a single URL and return its content as Markdown for the model.
- **[filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** — 🏷️ official ⚠️ mutating 🔒 local  
  Read, write, and search files within explicitly-allowed directories.
- **[git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** — 🏷️ official ⚠️ mutating 🔒 local  
  Read repository state, view diffs, run common git commands.
- **[memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** — 🏷️ official ⚠️ mutating 🔒 local  
  Reference knowledge-graph memory server: entities, relations, and observations persisted to a local JSONL file.
- **[sequentialthinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** — 🏷️ official 🛡️ read-only 🔒 local  
  Helper that exposes a structured "think step by step" planning tool.
- **[time](https://github.com/modelcontextprotocol/servers/tree/main/src/time)** — 🆕 new 🏷️ official 🛡️ read-only 🔒 local  
  Current time and timezone conversion (`get_current_time`, `convert_time`).

## Files, Filesystem & Local Data

- **[obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** — 🏷️ community ⚠️ mutating 🔒 local  
  Read, search, edit and delete notes in your Obsidian vault, through the Local REST API community plugin (which must be installed and given an API key).  
  <sub>★ 4.5k · last push 2026-08-31</sub>

## Web Search & Browsing

- **[brave-search](https://github.com/brave/brave-search-mcp-server)** — 🆕 new 🏷️ official 🛡️ read-only  
  Brave's official server for the Brave Search API: web, local, place, image, video, and news search, summarizer, and LLM-context retrieval; needs `BRAVE_API_KEY` (the free monthly credit requires a card on file). Replaces the archived reference Brave server.  
  <sub>★ 1.5k · v2.1.4 (2026-09-17)</sub>
- **[communicate-docs](https://communicate.so/mcp/server-card)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Communicate's public developer-docs server: three read-only tools for its developer guide, OpenAPI summary, and support contact. Hosted at `https://communicate.so/mcp`, no auth; it cannot reach workspaces or send messages. No public source.
- **[context7](https://github.com/upstash/context7)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Upstash's up-to-date library documentation for coding agents (`resolve-library-id`, `query-docs`). Remote at `https://mcp.context7.com/mcp`; an API key is recommended.  
  <sub>★ 62.7k · @upstash/context7-opencode@0.2.0 (2026-10-02)</sub>
- **[duckduckgo](https://github.com/nickclyde/duckduckgo-mcp-server)** — 🏷️ community 🛡️ read-only  
  DuckDuckGo web search plus page fetch-and-parse; no API key, runs locally over stdio or HTTP, with built-in rate limiting.  
  <sub>★ 1.5k · v0.7.0 (2026-09-04)</sub>
- **[exa](https://github.com/exa-labs/exa-mcp-server)** — 🏷️ official 🛡️ read-only ☁️ hosted  
  Exa web search and page fetch, plus advanced filtered search and multi-step agent_run research. Hosted at mcp.exa.ai with a free keyless rate-limited tier; OAuth or API key for higher limits and agent runs.  
  <sub>★ 5.1k · last push 2026-10-02</sub>
- **[firecrawl](https://github.com/firecrawl/firecrawl-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Scrape, search, map, and crawl websites into Markdown or schema-defined JSON; also browser interaction (click/type), an async research agent, and scheduled change monitors. Hosted keyless endpoint covers scrape/search/parse; other tools need a free or paid API key.  
  <sub>★ 7.6k · v3.2.1 (2025-09-26)</sub>
- **[microsoft-learn](https://learn.microsoft.com/en-us/training/support/mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Microsoft's hosted Learn MCP server (`https://learn.microsoft.com/api/mcp`): search official Microsoft/Azure docs, fetch full articles, search code samples. No auth, free; refreshed daily.
- **[perplexity](https://github.com/perplexityai/modelcontextprotocol)** — 🏷️ official 🛡️ read-only ☁️ hosted 💰 paid  
  Perplexity's official server for its API Platform: web search, quick answers, deep research and reasoning, with citations. Hosted at `https://api.perplexity.ai/mcp` (OAuth or API key), or `npx @perplexity-ai/mcp-server` with an API key. Tool calls are billed at API rates.  
  <sub>★ 2.6k · last push 2026-09-25</sub>
- **[tavily](https://github.com/tavily-ai/tavily-mcp)** — 🏷️ official 🛡️ read-only ☁️ hosted  
  Tavily's agent search API: `tavily_search`, `tavily_extract`, `tavily_map`, `tavily_crawl`, `tavily_research`. Hosted at `https://mcp.tavily.com/mcp/` (API key or OAuth) or run locally with `npx tavily-mcp`; free account tier.  
  <sub>★ 2.4k · last push 2026-09-29</sub>

## Browser Automation

- **[browser-use](https://docs.browser-use.com/open-source/customize/integrations/mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Browser Use's own server. Local stdio (`uvx --from 'browser-use[cli]' browser-use --mcp`) gives direct browser tools (navigate, click, type, scroll, tabs, extract, screenshot) plus an autonomous agent tool that needs your OpenAI or Anthropic key. A hosted Cloud MCP at `https://api.browser-use.com/v3/mcp` (API key, pay-as-you-go credits) runs agent sessions in Browser Use's cloud.
- **[chrome-devtools](https://github.com/ChromeDevTools/chrome-devtools-mcp)** — 🆕 new 🏷️ official ⚠️ mutating  
  Chrome DevTools team's server: control and inspect a live Chrome for automation, debugging (network, console, screenshots), and performance traces. Sends usage statistics to Google by default (`--no-usage-statistics` opts out).  
  <sub>★ 53k · chrome-devtools-mcp-v1.10.1 (2026-09-23)</sub>
- **[playwright](https://github.com/microsoft/playwright-mcp)** — 🏷️ official ⚠️ mutating  
  Microsoft's official Playwright MCP. Multi-browser, accessibility-tree snapshots designed for agent loops.  
  <sub>★ 37.8k · v0.0.83 (2026-09-28)</sub>

## Source Control

- **[gitea](https://gitea.com/gitea/gitea-mcp)** — 🏷️ official ⚠️ mutating  
  Self-hosted Gitea instances; full repo + issue + PR control.
- **[github](https://github.com/github/github-mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  GitHub's official server: repos, issues, pull requests, Actions, code security, grouped into toolsets. Local binary or remote at `https://api.githubcopilot.com/mcp/`; `--read-only` drops all write tools.  
  <sub>★ 33.4k · v1.14.0 (2026-10-02)</sub>
- **[gitlab](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  GitLab's built-in MCP server (beta) at `https://<instance>/api/v4/mcp` (gitlab.com, Self-Managed, Dedicated): issues, merge requests, work items, repository, CI, with opt-in wikis and code security toolsets. OAuth 2.0 with dynamic client registration. All tiers; Free is limited to 60 requests a minute.

## Issue Trackers & Project Management

- **[asana](https://developers.asana.com/docs/using-asanas-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Asana's hosted MCP server (`https://mcp.asana.com/v2/mcp`): tasks, projects, reports. OAuth; the old `/sse` beta endpoint was shut down on 2026-05-11.
- **[atlassian](https://github.com/atlassian/atlassian-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Atlassian's official remote MCP server (`https://mcp.atlassian.com/v2/mcp`): Jira, Confluence, Jira Service Management, Bitbucket, Compass, Loom. OAuth 2.1 or API tokens; the legacy `/sse` endpoint was retired after 2026-06-30.  
  <sub>★ 1.1k · last push 2026-09-15</sub>
- **[linear](https://linear.app/docs/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Linear's hosted MCP server (`https://mcp.linear.app/mcp`; read-only variant at `/mcp/readonly`): issues, projects, cycles, comments. OAuth 2.1 or API key.
- **[orbit](https://github.com/Noveum/orbit/blob/main/docs/mcp.md)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Open-source task manager (issues, boards, sprints, projects, docs) with an MCP server. The `orbit.write` scope creates and updates issues, comments, projects, and sprints. Hosted free at `https://orbit.noveum.ai/mcp` (OAuth), or self-host it (self-hosting is in preview). Apache-2.0.
- **[trello](https://support.atlassian.com/trello/docs/connect-trello-to-ai-assistants-with-trello-mcp/)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Atlassian's hosted Trello server (`https://mcp.trello.com/v1`, OAuth 2.0): read, search, create, update, move, and archive boards, lists, cards, checklists, labels, and comments. No permanent deletes. Works on all Trello plans.

## Communication

- **[autoposting](https://docs.autoposting.ai/mcp/overview)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Draft, schedule, and publish social posts (X, LinkedIn, Instagram, Threads, YouTube), carousels, and video clips. Hosted at `https://app.autoposting.ai/mcp` (OAuth 2.1, 70 tools); also a local stdio CLI (`ap mcp`) that calls the same API. The tools you see depend on the scopes you grant, and some are destructive. Needs a paid Autoposting plan. No public server source or licence.
- **[bulkpublish](https://github.com/azeemkafridi/bulkpublish-api/tree/main/mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Schedule and publish social posts to 15 platforms, upload media, and read analytics. 79 tools in the MIT stdio server (`@bulkpublish/mcp-server`); a 20-tool core set is hosted at `https://mcp.bulkpublish.com/mcp` (OAuth 2.1). There is a free plan.
- **[discord](https://github.com/SaseQ/discord-mcp)** — 🏷️ community ⚠️ mutating  
  Discord bot (needs a bot token): send, edit, read, and react to messages and DMs; manage channels, roles, webhooks, events, invites, and forums; kick, ban, and timeout members.  
  <sub>★ 530 · v1.0.0 (2026-03-16)</sub>
- **[google-workspace](https://github.com/taylorwilsdon/google_workspace_mcp)** — 🏷️ community ⚠️ mutating  
  Gmail, Calendar, Drive, Docs, Sheets, Chat, Forms, Tasks, Apps Script and more behind one server (120+ tools in core/extended/complete tiers; --read-only available). Uses your own Google OAuth client.  
  <sub>★ 3.3k · v2.0.1 (2026-10-04)</sub>
- **[google-workspace-official](https://developers.google.com/workspace/guides/configure-mcp-servers)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Google's official remote servers, one per product: Gmail (drafts only, no send), Drive, Docs, Sheets, Slides, Calendar, Chat, People. Developer Preview; needs a Google Cloud project and your own OAuth client.
- **[slack](https://docs.slack.dev/ai/slack-mcp-server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Slack's hosted MCP server (`https://mcp.slack.com/mcp`): search channels, send messages, manage canvases. OAuth with per-tool scopes; workspace admins approve and manage access.
- **[telegram](https://github.com/chigwell/telegram-mcp)** — 🏷️ community ⚠️ mutating  
  Read and send Telegram messages, chats, contacts, and media as your own user account (Telethon session), not a bot.  
  <sub>★ 1.8k · v3.2.66 (2026-10-05)</sub>

## Relational Databases

- **[clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  ClickHouse's official server: `run_query`, `list_databases`, `list_tables` (plus chDB). Read-only by default; writes need `CLICKHOUSE_ALLOW_WRITE_ACCESS=true`, and destructive statements also need `CLICKHOUSE_ALLOW_DROP=true`. ClickHouse Cloud users can instead use the hosted remote MCP at `https://mcp.clickhouse.cloud/mcp` (OAuth, SELECT-only, enabled per service).  
  <sub>★ 879 · v0.7.0 (2026-09-21)</sub>
- **[mysql](https://github.com/benborla/mcp-server-mysql)** — 🏷️ community ⚠️ mutating  
  MySQL via one `mysql_query` tool: read-only by default; INSERT/UPDATE/DELETE each enabled by env flag. Multi-DB mode, SSH tunnelling, optional HTTP transport.  
  <sub>★ 2.1k · v2.0.9 (2026-06-19)</sub>
- **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** — 🏷️ community ⚠️ mutating  
  Postgres MCP Pro (Crystal DBA): index tuning, EXPLAIN plans with hypothetical indexes, health checks, and schema-aware SQL. Unrestricted read/write mode, or a restricted read-only mode with time limits. Last PyPI release is v0.3.0 (May 2025); main has newer fixes.  
  <sub>★ 3.4k · v0.3.0 (2025-05-16)</sub>
- **[supabase](https://github.com/supabase/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Supabase's official server (`https://mcp.supabase.com/mcp`): database, docs, and project tools. Scope it with `project_ref` and `read_only=true`.  
  <sub>★ 2.9k · mcp-server-supabase-v0.13.0 (2026-09-17)</sub>

## NoSQL & Document Databases

- **[mongodb](https://github.com/mongodb-js/mongodb-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  MongoDB's official server for databases and Atlas clusters: query, aggregation, CRUD, Atlas admin. Run it locally (`--readOnly` restricts it to read tools) or use the Atlas-managed hosted endpoint `https://mcp.mongodb.com` (OAuth; org-level read-only mode).  
  <sub>★ 1.1k · v3.0.5 (2026-10-01)</sub>
- **[neo4j](https://github.com/neo4j/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Neo4j's official local server: `read-cypher` and `write-cypher` tools against your graph; `NEO4J_MCP_READ_ONLY=true` disables writes. Aura users can instead use the hosted MCP for Aura (`https://<INSTANCE_ID>.mcp-instances.neo4j.io`, OAuth).  
  <sub>★ 296 · v1.6.0 (2026-09-10)</sub>

## Vector & Memory Stores

- **[brethof-brain](https://brethof.ai/brain/)** — 🆕 new 🏷️ brethof ⚠️ mutating ☁️ hosted  
  Persistent memory for AI agents across sessions, projects and machines. Every session opens with a brief — your standing rules, what each project is, where the last sessions stopped — and the records that bear on a prompt arrive with it. It curates itself into records per project, keeps the full chat history searchable, and adds notes, playbooks and an optional graph of decisions: each one dated, with its reason and what it replaced, returned alongside search results. Proven on nine platforms: Claude Code (Linux, Windows), Codex, Qwen Code, Cline, OpenCode, Kilo Code, OpenClaw, Hermes Agent and dsh. Memory lives on your machine (local edition, Docker or Podman) or encrypted under a passphrase only you hold (hosted); each exchange is processed by our hub, which keeps none of it. Free tier; the client is source-available. Disclosure: maintained by us.
- **[chroma](https://github.com/chroma-core/chroma-mcp)** — 🏷️ official ⚠️ mutating 🔒 local  
  ChromaDB collections, similarity search, persistent embeddings (ephemeral, persistent, HTTP or Chroma Cloud client). Still the server in Chroma's docs, but unmaintained: no release since v0.2.6 (Aug 2025), and a reported SQL-injection issue and 15 PRs sit unanswered.  
  <sub>★ 598 · v0.2.6 (2025-08-14)</sub>
- **[claimidx](https://github.com/claimidx/claimidx)** — 🆕 new 🏷️ official ⚠️ mutating  
  Shared index of known software failures and their fixes, for coding agents: ask before retrying, then record the fix. Runs locally (PyPI `claimidx`, Apache-2.0) but connects to a public commons at home.claimidx.com by default and syncs with it at session start. Since v0.7.14, publishing a claim to the commons asks for confirmation (earlier versions shared automatically); `CLAIMIDX_COMMONS=0` turns the commons off.  
  <sub>★ 2 · v0.7.14 (2026-10-02)</sub>
- **[contextstream](https://github.com/contextstream/mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Persistent memory and code search for coding agents: saves decisions, lessons, and plans across sessions. Indexing sends your source code to ContextStream's hosted service, and transcript saving and Git metadata capture are on by default. The client is MIT; the hosted backend is closed. Free tier: 10,000 credits a month, no card.  
  <sub>★ 44 · v1.0.13 (2026-10-04)</sub>
- **[pinecone](https://github.com/pinecone-io/pinecone-mcp)** — 🏷️ official ⚠️ mutating  
  Pinecone's Developer MCP: search Pinecone docs, list, describe and create indexes, upsert and search records, and rerank. Runs with `npx @pinecone-database/mcp` and an API key (docs search works without one). Only indexes with integrated embedding are supported. Separately, each Pinecone Assistant is a hosted MCP endpoint for retrieving context.  
  <sub>★ 71 · v0.3.0 (2026-08-07)</sub>
- **[qdrant](https://github.com/qdrant/mcp-server-qdrant)** — 🏷️ official ⚠️ mutating  
  Semantic memory on Qdrant: store text with metadata and search it (`qdrant-store`, `qdrant-find`); a missing collection is created automatically. Connects to a Qdrant URL or runs an embedded local database. Last release v0.8.1 (Dec 2025).  
  <sub>★ 1.5k · v0.8.1 (2025-12-10)</sub>
- **[weaviate](https://docs.weaviate.io/weaviate/configuration/mcp-server)** — 🏷️ official ⚠️ mutating  
  MCP server built into Weaviate (GA in v1.38; `MCP_SERVER_ENABLED=true`, served at `/v1/mcp`, always on in Weaviate Cloud): hybrid search, collection config, tenant listing, object upsert. Self-hosted defaults to read-only (`MCP_SERVER_WRITE_ACCESS_ENABLED=true` for writes); respects RBAC. Replaces the deprecated standalone server.

## Productivity & Notes

- **[airtable](https://support.airtable.com/articles/9897799762-using-the-airtable-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Airtable's hosted MCP server (`https://mcp.airtable.com/mcp`): bases, tables, records. OAuth or personal access token.
- **[apple-notes](https://github.com/sweetrb/apple-notes-mcp)** — 🏷️ community ⚠️ mutating 🔒 local  
  Read, search, create, edit, organise, and export Apple Notes on macOS via AppleScript, Shortcuts, and read-only access to the Notes database; no network requests.  
  <sub>★ 145 · v2.14.0 (2026-10-03)</sub>
- **[google-calendar](https://github.com/nspady/google-calendar-mcp)** — 🏷️ community ⚠️ mutating  
  Read, create, update, delete and respond to events across multiple accounts and calendars, with free/busy lookup. Uses your own Google OAuth client. (Google's own Calendar server is listed separately as a Developer Preview.)  
  <sub>★ 1.2k · v2.7.0 (2026-09-28)</sub>
- **[notion](https://developers.notion.com/guides/mcp/overview)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Notion's hosted MCP server: search the workspace, read and edit pages in Markdown. OAuth, respects each user's existing permissions. (The self-hosted makenotion/notion-mcp-server is no longer maintained.)
- **[process-street](https://www.process.st/help/docs/mcp-server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Process Street's hosted server: workflows, workflow runs, tasks, users, data sets and reports. It can create and manage runs and assigned tasks within your Process Street permissions. `https://mcp.process.st/` (OAuth sign-in, including SAML SSO organisations, or an admin-generated API key). Needs a paid plan after a 14-day trial. No public source.
- **[screenpipe](https://github.com/screenpipe/screenpipe/tree/main/packages/screenpipe-mcp)** — 🆕 new 🏷️ official ⚠️ mutating  
  Search your recorded screen text, audio transcripts, meetings, and activity summaries; can also control recording, run pipes, and edit memories. Reads your full screen and audio history, so grant it with care. Source-available under the Screenpipe Commercial License (not an OSI open-source licence).
- **[zapier](https://docs.zapier.com/mcp/home)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Zapier's hosted MCP server (`https://mcp.zapier.com/api/v1/connect`): 40,000+ actions across 9,000+ apps using the accounts you've connected in Zapier. OAuth or connection token (send it in a header, not the URL). Each successful call uses 2 tasks from your Zapier plan.

## Design & Creative

- **[cadre](https://github.com/ArthurBrioche/cadre-video-editor-plugin)** — 🆕 new 🏷️ official ⚠️ mutating 🔒 local  
  Bridge to Cadre, a screen recorder and non-destructive video editor for Apple Silicon Macs: start and stop recordings, then apply cuts, zooms, captions, and styling, preview, and export MP4 through the running app. The bridge is MIT; Cadre itself is proprietary, and export needs a Cadre Pro subscription.  
  <sub>★ 0 · mcpb-v1.2.3 (2026-09-30)</sub>
- **[figma](https://developers.figma.com/docs/figma-mcp-server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Figma's official server: design context, variables, screenshots and Code Connect for design-to-code; write tools create and edit native Figma/FigJam content (beta). Remote at `https://mcp.figma.com/mcp` (all plans; only clients in Figma's MCP Catalog may connect) or via the desktop app (paid Dev/Full seat). Rate limits by plan and seat.
- **[mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)** — 🏷️ community ⚠️ mutating 🔒 local  
  Drive Blender via Python — modify scenes, objects and materials, render views, import Poly Haven/Sketchfab assets, generate 3D models. Formerly blender-mcp; the PyPI package is now `mcp-for-blender`. Sends anonymous usage telemetry by default (`DISABLE_TELEMETRY=true` to turn it off).  
  <sub>★ 30k · last push 2026-10-05</sub>
- **[orkas-video-studio](https://github.com/Orkas-AI/Orkas-VideoStudio)** — 🆕 new 🏷️ official ⚠️ mutating  
  Local-first video toolkit for coding agents: compose, edit, generate, and assemble videos from an editable `plan.json` timeline, through a CLI and an MCP server. Early development: install from source, since the npm packages aren't published yet. Optional generation calls providers with your own keys. MIT.  
  <sub>★ 497 · last push 2026-09-22</sub>

## Operations & Infrastructure

- **[aws](https://github.com/awslabs/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  AWS's official MCP servers: an open-source monorepo of local servers (docs, IaC, Bedrock, S3, and more), plus the AWS-hosted AWS MCP Server (`https://aws-mcp.us-east-1.api.aws/mcp`, GA May 2026) that calls any AWS API and searches AWS docs. No extra charge; you pay for the AWS resources used.  
  <sub>★ 9.8k · 2026.09.20260930084625 (2026-09-30)</sub>
- **[azure](https://github.com/microsoft/mcp/tree/main/servers/Azure.Mcp.Server)** — 🆕 new 🏷️ official ⚠️ mutating  
  Microsoft's official Azure MCP Server (GA in 2.0): tools for 45+ Azure service areas (storage, databases, monitoring/KQL, deployments). Runs locally via `npx -y @azure/mcp@latest server start`, NuGet, PyPI or Docker, or self-hosted remotely. Entra ID via Azure Identity, respects RBAC; `--read-only` blocks writes. MIT.
- **[cloudflare](https://github.com/cloudflare/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Cloudflare's official API server (`https://mcp.cloudflare.com/mcp`): the whole Cloudflare API (~2,500 endpoints) through Code Mode `search`/`execute` tools. OAuth or API token. Cloudflare also runs product servers (docs, bindings, builds, observability, Radar, browser, logs) under `*.mcp.cloudflare.com`. Apache-2.0.  
  <sub>★ 922 · last push 2026-10-02</sub>
- **[datadog](https://docs.datadoghq.com/bits_ai/mcp_server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Datadog's hosted MCP server (per-site endpoints, e.g. US1 `https://mcp.datadoghq.com/api/unstable/mcp-server/mcp`; not GovCloud): logs, metrics, monitors, dashboards, incidents, chosen via `?toolsets=`. OAuth, access token or API+app keys; write tools need the `mcp_write` permission.
- **[docker-mcp-gateway](https://github.com/docker/mcp-gateway)** — 🏷️ official ⚠️ mutating  
  Docker's MCP Toolkit CLI plugin (`docker mcp`): runs catalog MCP servers in isolated containers behind one gateway, with Docker Desktop secrets management.  
  <sub>★ 1.6k · last push 2026-09-23</sub>
- **[grafana](https://github.com/grafana/mcp-grafana)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Grafana's official server: dashboards, datasource queries, alerting, incidents, annotations. Can create and update dashboards, alerts and incidents; --disable-write makes it read-only. Grafana Cloud users can connect to the hosted https://mcp.grafana.com/mcp (OAuth) instead.  
  <sub>★ 3.5k · v2.0.0 (2026-10-01)</sub>
- **[helm](https://github.com/zekker6/mcp-helm)** — 🏷️ community 🛡️ read-only  
  Query Helm chart repositories and OCI registries: list charts and versions, read values, contents, dependencies and images. Cannot touch cluster releases. Public instance at https://mcp-helm.zekker.dev/mcp.  
  <sub>★ 26 · v1.4.2 (2026-09-30)</sub>
- **[kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** — 🏷️ community ⚠️ mutating  
  kubectl-equivalent operations on the configured cluster.  
  <sub>★ 1.6k · v4.1.9 (2026-10-02)</sub>
- **[sentry](https://github.com/getsentry/toolkit)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Sentry's official server: issues, events, traces, logs, replays, releases, alerts and monitors; can update issues and projects, create teams and DSNs, and create or delete alert rules and monitors. Hosted at `https://mcp.sentry.dev/mcp` (OAuth) or stdio via `npx @sentry/mcp-server` for self-hosted Sentry; AI search tools need your own LLM key. Licence: FSL-1.1-Apache-2.0.  
  <sub>★ 912 · cli@0.46.0 (2026-10-01)</sub>
- **[shipvela](https://github.com/stefanautomateed/shipvela-codex)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Public beta. Create hosting projects, deploy a connected GitHub repo or a small static site, and read deployment status, build logs, and usage. Hosted at `https://shipvela.com/mcp` (OAuth with PKCE); free Hobby plan, and each publish counts against your plan's allowance. Plugin files are MIT per the README; the hosted service is proprietary.  
  <sub>★ 0 · last push 2026-10-05</sub>
- **[vercel](https://vercel.com/docs/agent-resources/vercel-mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Vercel's hosted MCP server (`https://mcp.vercel.com`): docs search, teams, projects, deployments and logs, Web Analytics; can deploy code and make purchases. OAuth; only Vercel-approved clients can connect. Acts with your full Vercel account access. All plans.

## AI & ML Platforms

- **[aident-loadout](https://github.com/Aident-AI/aident-skill)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Gateway that lets an agent use 1,000+ third-party apps and tools (Gmail, Slack, Linear, Notion, HubSpot, and more) through your connected accounts, with credentials in Aident's vault and an audit history. Hosted at `https://loadout.aident.ai/mcp` (OAuth); free to start, with top-ups for more usage. The skill repo is MIT; the service is proprietary.  
  <sub>★ 5 · last push 2026-09-27</sub>
- **[api-market](https://api.market/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Gateway to the API.market catalogue of 600+ third-party APIs (3,810+ tools: image and video generation, search, scraping, maps, data). Hosted at `https://api.market/api/mcp/gateway` (OAuth or API key). Calls can spend free-tier quota or pay-as-you-go wallet funds. Proprietary; no public source.
- **[huggingface](https://github.com/huggingface/hf-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Hugging Face's official server: Hub search and details, docs search, Gradio Spaces as tools, plus optional repo creation, Jobs and Sandboxes. Hosted at https://huggingface.co/mcp or run locally.  
  <sub>★ 302 · v0.4.28 (2026-10-05)</sub>
- **[runapi](https://github.com/runapi-ai/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Browse a catalog of image, video, music, and text-to-speech models, check current pricing, and create and poll generation jobs. Hosted at `https://mcp.runapi.ai/mcp` (OAuth or API key) or local via `npx @runapi.ai/mcp`, whose catalog tools work without an API key; jobs spend prepaid pay-as-you-go credits.  
  <sub>★ 55 · v0.15.0 (2026-09-30)</sub>

## Specialised / Vertical

- **[careclinic](https://careclinic.io/careclinic-mcp/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Your CareClinic health record in chat: today's medication schedule, recent symptoms and mood, and insights. A check-in tool logs entries after you confirm them. Hosted at `https://mcp.careclinic.io/mcp` (OAuth with your CareClinic account). Handles personal health data. No public source; the repo is all rights reserved.
- **[hubspot](https://developers.hubspot.com/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  HubSpot's hosted MCP server (`https://mcp.hubspot.com`): read and write CRM records, activities, content, campaigns and pipelines. OAuth with PKCE via an MCP connector you create in HubSpot. A local developer MCP server ships with the HubSpot CLI (`hs mcp setup`).
- **[invompt](https://github.com/Invompt/invompt-mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Create, revise, archive, and email invoices, quotes, estimates, and pro formas from chat. Hosted at `https://mcp.invompt.com/mcp` (OAuth); you can start without an account, but emailing documents needs a registered one. The MIT repo also has a local-beta CLI.  
  <sub>★ 0 · last push 2026-09-30</sub>
- **[kleap](https://github.com/kleaphq/cli)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  No-code website builder: create, edit, and publish sites, manage files, site databases, and custom domains (including a `buy_domain` tool). Hosted at `https://kleap.co/api/mcp` (OAuth) or a local stdio server from the MIT CLI; read-only API keys are available. AI edits use Kleap credits; there is a free plan.  
  <sub>★ 1 · last push 2026-09-27</sub>
- **[llm-pulse](https://llmpulse.ai/features/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  AI-search visibility analytics: brand mentions, citations, sentiment, and share of voice. With the write scope it can add prompts, competitors, tags, and annotations, generate content briefs, and launch audits. Hosted at `https://api.llmpulse.ai/api/v1/mcp` (OAuth 2.1; API key on Scale plan and above). Needs a paid LLM Pulse plan after a 14-day trial. The server source is private; the repo holds an MIT stdio wrapper.
- **[pocket-drives](https://github.com/RevList/pocket-drives-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Search, quote, and check availability for peer-to-peer luxury, exotic, and EV car rentals from independent hosts (five US markets at listing time). Hosted at `https://pocketdrives.ai/mcp`, no auth; it does not book, which happens in the iOS app or on pocketdrives.ai. No public source or licence.  
  <sub>★ 0 · last push 2026-08-21</sub>
- **[robot-speed](https://www.robot-speed.com/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  SEO tools: 12 free audit tools with no account at `https://www.robot-speed.com/api/mcp/free`; the full 39-tool server at `/api/mcp` (OAuth) also manages content, Search Console data, and reports, and needs a Robot Speed subscription after its trial. No public server source.
- **[spotify](https://github.com/jamiew/spotify-mcp)** — 🏷️ community ⚠️ mutating 💰 paid  
  Spotify Web API: search, playback and queue control, playlists, and library (28 tools); updated for Spotify's February 2026 API changes. Needs your own Spotify developer app and Premium. Maintained fork of the now-inactive varunneal/spotify-mcp. Spotify's own connector is currently Claude-only.  
  <sub>★ 11 · v0.7.0 (2026-09-20)</sub>
- **[statsnet](https://github.com/usenetstate/statsnet-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Company background checks worldwide: registration, executives, government contracts, courts, and finances (`search_companies`, `get_company`). Hosted at `https://statsnet.co/mcp` with no auth; it returns the public company card only, while contacts, relations, and exports need a Statsnet subscription through its separate REST API. No public server source.  
  <sub>★ 0 · last push 2026-09-16</sub>
- **[stripe](https://docs.stripe.com/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Stripe's hosted MCP server (`https://mcp.stripe.com`): payments, customers, subscriptions, refunds via OAuth or agent API keys. Refunds and outbound payments need human confirmation. From 2026-10-31 it accepts only Agent-tagged keys or OAuth.
- **[trends-mcp](https://github.com/trendsmcp-ai/Trends-MCP)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Live trend data from Google Search, YouTube, TikTok, Reddit, Amazon, Wikipedia, news, app stores, npm, Steam, and more (`get_time_series`, `get_growth`, `get_top_trends`). Hosted at `https://api.trendsmcp.ai/mcp` or through the repo's MIT stdio adapter. Needs an API key, which comes with a free monthly quota.  
  <sub>★ 44 · last push 2026-08-29</sub>
- **[wine-labs](https://winelabs.ai/agents)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Fine-wine market data: wine and LWIN matching, retail and auction prices, exchange order books, merchants, and critic data, plus cellar CSV/Excel processing jobs. Hosted at `https://chat.wine-labs.com/mcp` (browser OAuth). Billed in credits: existing API allowance, monthly from $25, or pay-as-you-go from $5. No public server source.

## Frameworks & SDKs for Building MCP Servers

- **[fastmcp](https://github.com/PrefectHQ/fastmcp)** — 🏷️ community  
  Python framework for MCP servers and clients, now under PrefectHQ. FastMCP 1.0 was incorporated into the official Python SDK in 2024; this is the actively maintained standalone project.  
  <sub>★ 28k · v4.0.11 (2026-10-04)</sub>
- **[mcp-go](https://github.com/modelcontextprotocol/go-sdk)** — 🏷️ official  
  Official Go SDK for MCP servers and clients, maintained with Google. Single-binary deployment friendly. Apache-2.0 for new code, MIT for existing code.  
  <sub>★ 5.2k · v1.8.0 (2026-09-14)</sub>
- **[mcp-python](https://github.com/modelcontextprotocol/python-sdk)** — 🏷️ official  
  Reference Python SDK (PyPI `mcp`). v2 renamed the decorator-based `FastMCP` class to `MCPServer`; standalone FastMCP is a separate project.  
  <sub>★ 24.5k · v2.3.0 (2026-10-02)</sub>
- **[mcp-typescript](https://github.com/modelcontextprotocol/typescript-sdk)** — 🏷️ official  
  Reference TypeScript / Node SDK. v2 ships as `@modelcontextprotocol/server` and `@modelcontextprotocol/client`; v1 `@modelcontextprotocol/sdk` is maintained on the `v1.x` branch.  
  <sub>★ 13.5k · v2.3.1 (2026-10-05)</sub>

<!-- LIST:END -->

## Discovery hubs

Where to look for new servers as the ecosystem grows.

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** — the reference servers maintained by the MCP steering group + a list of community ones at the bottom.
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
