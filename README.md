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
change, whether it needs a paid account, and whether it takes crypto
payment. Licences are named when they are not OSI open source, or when
there is no public source at all.

We decline only:

1. Nothing real to point at — no code and no documented, reachable endpoint.
2. Misleading claims we can't label around, and scams.
3. Off-topic submissions and spam.

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
- 🪙 `crypto` — takes payment in cryptocurrency, for example x402, where your
  AI client pays per call from a wallet. Crypto is one payment option among
  others; the label shows it so you can decide what the client may spend.
- 🆕 `new` — listed in the last 60 days.

<!-- LIST:START -->
## Contents

- [Reference servers (MCP steering group)](#reference-servers-mcp-steering-group) (7)
- [Files, Filesystem & Local Data](#files-filesystem--local-data) (2)
- [Web Search & Browsing](#web-search--browsing) (11)
- [Browser Automation](#browser-automation) (5)
- [Source Control](#source-control) (3)
- [Issue Trackers & Project Management](#issue-trackers--project-management) (5)
- [Communication](#communication) (11)
- [Relational Databases](#relational-databases) (4)
- [NoSQL & Document Databases](#nosql--document-databases) (2)
- [Vector & Memory Stores](#vector--memory-stores) (9)
- [Productivity & Notes](#productivity--notes) (9)
- [Design & Creative](#design--creative) (10)
- [Operations & Infrastructure](#operations--infrastructure) (14)
- [AI & ML Platforms](#ai--ml-platforms) (6)
- [Specialised / Vertical](#specialised--vertical) (36)
- [Frameworks & SDKs for Building MCP Servers](#frameworks--sdks-for-building-mcp-servers) (5)

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

- **[coding-tools-mcp](https://github.com/mybolide/coding-tools-mcp)** — 🆕 new 🏷️ community ⚠️ mutating 🔒 local  
  Desktop app (Rust and Tauri 2; Windows installer and an unsigned macOS build) that turns a project folder into an MCP workspace: read and search files, `apply_patch`, run shell commands (`exec_command`), Git status, diff, log and blame, and history-session tools that save progress under `docs/history-session/`. Writes, deletes and commands are confined to the workspace by a policy check (on Windows not an OS sandbox). Serves Streamable HTTP on 127.0.0.1 and can publish it through an frp or Cloudflare tunnel with OAuth, so ChatGPT and other remote clients can reach it; it can also proxy other MCP servers you configure. Free. A rewrite in a GitHub fork of xyTom/coding-tools-mcp; it declares Apache-2.0 in its package metadata, but the repo has no LICENSE file.
- **[obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** — 🏷️ community ⚠️ mutating 🔒 local  
  Read, search, edit and delete notes in your Obsidian vault, through the Local REST API community plugin (which must be installed and given an API key).  
  <sub>★ 4.5k · last push 2026-08-31</sub>

## Web Search & Browsing

- **[brave-search](https://github.com/brave/brave-search-mcp-server)** — 🆕 new 🏷️ official 🛡️ read-only  
  Brave's official server for the Brave Search API: web, local, place, image, video, and news search, summarizer, and LLM-context retrieval; needs `BRAVE_API_KEY` (the free monthly credit requires a card on file). Replaces the archived reference Brave server.  
  <sub>★ 1.6k · v2.1.4 (2026-09-17)</sub>
- **[communicate-docs](https://communicate.so/mcp/server-card)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Communicate's public developer-docs server: three read-only tools for its developer guide, OpenAPI summary, and support contact. Hosted at `https://communicate.so/mcp`, no auth; it cannot reach workspaces or send messages. No public source.
- **[context7](https://github.com/upstash/context7)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Upstash's up-to-date library documentation for coding agents (`resolve-library-id`, `query-docs`). Remote at `https://mcp.context7.com/mcp`; an API key is recommended.  
  <sub>★ 64k · @upstash/context7-mcp@4.4.4 (2026-10-19)</sub>
- **[curlshot](https://curlshot.com/docs/guides/ai-agents)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  CurlShot screenshots of public web pages, two tools: `take_screenshot` renders a page in a real browser and returns PNG, JPEG, WebP, PDF or a scrolling video, with ads and cookie banners hidden by default; `list_devices` lists phone, tablet and desktop presets. Hosted at `https://curlshot.com/api/mcp` (API key as a Bearer token; `list_devices` works without one). Each successful render uses one screenshot of the monthly quota: free plan 100 a month with no card, paid plans from $19 a month. No public source.
- **[docsy](https://github.com/getremcp/docsy-plugin)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Docsy's version-aware developer documentation index, five tools: `resolve-library-id`, `list-library-versions`, `query-docs` (focused excerpts or publisher links for one library and version), `search` and `fetch`, each result with a link to the original source. Hosted at `https://docsy.remcp.site/mcp/registry` (OAuth 2.1 sign-in) or `https://docsy.remcp.site/mcp/public` (no account, rate-limited, public docs only). Free to use under fair-use limits, per Docsy's terms. No public server source; the MIT repo holds plugin manifests and install guides, and the TypeScript SDK and CLI are open source (MIT).
- **[duckduckgo](https://github.com/nickclyde/duckduckgo-mcp-server)** — 🏷️ community 🛡️ read-only  
  DuckDuckGo web search plus page fetch-and-parse; no API key, runs locally over stdio or HTTP, with built-in rate limiting.  
  <sub>★ 1.6k · v0.7.0 (2026-09-04)</sub>
- **[exa](https://github.com/exa-labs/exa-mcp-server)** — 🏷️ official 🛡️ read-only ☁️ hosted  
  Exa web search and page fetch, plus advanced filtered search and multi-step agent_run research. Hosted at mcp.exa.ai with a free keyless rate-limited tier; OAuth or API key for higher limits and agent runs.  
  <sub>★ 5.2k · last push 2026-10-30</sub>
- **[firecrawl](https://github.com/firecrawl/firecrawl-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Scrape, search, map, and crawl websites into Markdown or schema-defined JSON; also browser interaction (click/type), an async research agent, and scheduled change monitors. Hosted keyless endpoint covers scrape/search/parse; other tools need a free or paid API key.  
  <sub>★ 7.7k · v3.2.1 (2025-09-26)</sub>
- **[microsoft-learn](https://learn.microsoft.com/en-us/training/support/mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Microsoft's hosted Learn MCP server (`https://learn.microsoft.com/api/mcp`): search official Microsoft/Azure docs, fetch full articles, search code samples. No auth, free; refreshed daily.
- **[perplexity](https://github.com/perplexityai/modelcontextprotocol)** — 🏷️ official 🛡️ read-only ☁️ hosted 💰 paid  
  Perplexity's official server for its API Platform: web search, quick answers, deep research and reasoning, with citations. Hosted at `https://api.perplexity.ai/mcp` (OAuth or API key), or `npx @perplexity-ai/mcp-server` with an API key. Tool calls are billed at API rates.  
  <sub>★ 2.6k · last push 2026-10-21</sub>
- **[tavily](https://github.com/tavily-ai/tavily-mcp)** — 🏷️ official 🛡️ read-only ☁️ hosted  
  Tavily's agent search API: `tavily_search`, `tavily_extract`, `tavily_map`, `tavily_crawl`, `tavily_research`. Hosted at `https://mcp.tavily.com/mcp/` (API key or OAuth) or run locally with `npx tavily-mcp`; free account tier.  
  <sub>★ 2.5k · last push 2026-10-29</sub>

## Browser Automation

- **[browser-use](https://docs.browser-use.com/open-source/customize/integrations/mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Browser Use's own server. Local stdio (`uvx --from 'browser-use[cli]' browser-use --mcp`) gives direct browser tools (navigate, click, type, scroll, tabs, extract, screenshot) plus an autonomous agent tool that needs your OpenAI or Anthropic key. A hosted Cloud MCP at `https://api.browser-use.com/v3/mcp` (API key, pay-as-you-go credits) runs agent sessions in Browser Use's cloud.
- **[chrome-devtools](https://github.com/ChromeDevTools/chrome-devtools-mcp)** — 🆕 new 🏷️ official ⚠️ mutating  
  Chrome DevTools team's server: control and inspect a live Chrome for automation, debugging (network, console, screenshots), and performance traces. Sends usage statistics to Google by default (`--no-usage-statistics` opts out).  
  <sub>★ 54.6k · chrome-devtools-mcp-v1.12.0 (2026-10-22)</sub>
- **[mac-mcp](https://github.com/bulutarkan/mac-mcp)** — 🆕 new 🏷️ community ⚠️ mutating 🔒 local  
  Whole-Mac control: native apps through macOS Accessibility (observe, click, type), Safari and Chrome tabs worked in the background, files with undo, screenshots, clipboard, Spotlight, scheduled tasks, paired Macs and iPhone Mirroring, and hand-off to agent CLIs such as Codex and Claude Code. Menu bar app plus a server on 127.0.0.1 (`npx @bulutarkan/mac-mcp install`, a curl installer, or an unnotarized .pkg); needs Accessibility, Screen Recording and Automation permissions. Switching from the default `standard` profile to `trusted` lets it run any shell command, AppleScript or page JavaScript as your user; it is not a sandbox. No telemetry; optional ngrok/Cloudflare tunnel for ChatGPT and voice via Edge TTS and Groq go online. MIT.  
  <sub>★ 96 · v2.3.1-r5 (2026-10-28)</sub>
- **[playwright](https://github.com/microsoft/playwright-mcp)** — 🏷️ official ⚠️ mutating  
  Microsoft's official Playwright MCP. Multi-browser, accessibility-tree snapshots designed for agent loops.  
  <sub>★ 39k · v0.0.84 (2026-10-31)</sub>
- **[remcp](https://github.com/getremcp/remcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Remote control of computers you pair to a ReMCP account: read, write, patch, move and delete files, run terminal commands and processes, drive native desktop apps through Accessibility/UI Automation and Chrome or Edge through CDP, take screenshots and screen recordings, read system diagnostics and edit DOCX/XLSX/PDF files, plus account tools to list, pair, disable and remove devices. Calls run with the full rights of the account running the agent and there is no per-call confirmation (a catastrophic-command blocklist is on by default; allowed folders are optional). You install an outbound-only device agent (`npx --yes @remcp/remcp@latest connect`, or a PowerShell bootstrap on Windows) and connect your client to `https://remcp.site/mcp` with ReMCP OAuth. File contents pass through ReMCP's backend and relay (not end-to-end encrypted); usage metrics are on unless you opt out. No public pricing page. Device client and runtime are MIT; the hosted backend's source is not public.

## Source Control

- **[gitea](https://gitea.com/gitea/gitea-mcp)** — 🏷️ official ⚠️ mutating  
  Self-hosted Gitea instances; full repo + issue + PR control.
- **[github](https://github.com/github/github-mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  GitHub's official server: repos, issues, pull requests, Actions, code security, grouped into toolsets. Local binary or remote at `https://api.githubcopilot.com/mcp/`; `--read-only` drops all write tools.  
  <sub>★ 34.1k · v2.0.3 (2026-10-21)</sub>
- **[gitlab](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  GitLab's built-in MCP server (beta) at `https://<instance>/api/v4/mcp` (gitlab.com, Self-Managed, Dedicated): issues, merge requests, work items, repository, CI, with opt-in wikis and code security toolsets. OAuth 2.0 with dynamic client registration. All tiers; Free is limited to 60 requests a minute.

## Issue Trackers & Project Management

- **[asana](https://developers.asana.com/docs/using-asanas-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Asana's hosted MCP server (`https://mcp.asana.com/v2/mcp`): tasks, projects, reports. OAuth; the old `/sse` beta endpoint was shut down on 2026-05-11.
- **[atlassian](https://github.com/atlassian/atlassian-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Atlassian's official remote MCP server (`https://mcp.atlassian.com/v2/mcp`): Jira, Confluence, Jira Service Management, Bitbucket, Compass, Loom. OAuth 2.1 or API tokens; the legacy `/sse` endpoint was retired after 2026-06-30.  
  <sub>★ 1.1k · last push 2026-10-29</sub>
- **[linear](https://linear.app/docs/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Linear's hosted MCP server (`https://mcp.linear.app/mcp`; read-only variant at `/mcp/readonly`): issues, projects, cycles, comments. OAuth 2.1 or API key.
- **[orbit](https://github.com/Noveum/orbit/blob/main/docs/mcp.md)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Open-source task manager (issues, boards, sprints, projects, docs) with an MCP server. The `orbit.write` scope creates and updates issues, comments, projects, and sprints. Hosted free at `https://orbit.noveum.ai/mcp` (OAuth), or self-host it (self-hosting is in preview). Apache-2.0.
- **[trello](https://support.atlassian.com/trello/docs/connect-trello-to-ai-assistants-with-trello-mcp/)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Atlassian's hosted Trello server (`https://mcp.trello.com/v1`, OAuth 2.0): read, search, create, update, move, and archive boards, lists, cards, checklists, labels, and comments. No permanent deletes. Works on all Trello plans.

## Communication

- **[agent-notifications](https://github.com/777genius/agent-notifications)** — 🆕 new 🏷️ community ⚠️ mutating 🔒 local  
  Desktop notifications for coding agents (Claude, Codex, OpenCode, Gemini CLI, Cursor CLI, Qoder, Pi) on macOS, Linux and Windows, mostly driven by lifecycle hooks. The bundled MCP server, installed by the Claude and Codex setup, adds two tools: `notify` sends an attention, blocker or progress alert mid-task through the delivery you configured, and `notification_status` reads the configuration without sending. The project also offers sounds, click-to-focus and optional Slack, Discord, Telegram, Lark/Feishu or custom webhooks. Local Go binary over stdio; no account or hosted service. GPL-3.0-or-later.
- **[autoposting](https://docs.autoposting.ai/mcp/overview)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Draft, schedule, and publish social posts (X, LinkedIn, Instagram, Threads, YouTube), carousels, and video clips. Hosted at `https://app.autoposting.ai/mcp` (OAuth 2.1, 70 tools); also a local stdio CLI (`ap mcp`) that calls the same API. The tools you see depend on the scopes you grant, and some are destructive. Needs a paid Autoposting plan. No public server source or licence.
- **[bulkpublish](https://github.com/azeemkafridi/bulkpublish-api/tree/main/mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Schedule and publish social posts to 15 platforms, upload media, and read analytics. 79 tools in the MIT stdio server (`@bulkpublish/mcp-server`); a 20-tool core set is hosted at `https://mcp.bulkpublish.com/mcp` (OAuth 2.1). There is a free plan.
- **[discord](https://github.com/SaseQ/discord-mcp)** — 🏷️ community ⚠️ mutating  
  Discord bot (needs a bot token): send, edit, read, and react to messages and DMs; manage channels, roles, webhooks, events, invites, and forums; kick, ban, and timeout members.  
  <sub>★ 581 · v1.0.0 (2026-03-16)</sub>
- **[google-workspace](https://github.com/taylorwilsdon/google_workspace_mcp)** — 🏷️ community ⚠️ mutating  
  Gmail, Calendar, Drive, Docs, Sheets, Chat, Forms, Tasks, Apps Script and more behind one server (120+ tools in core/extended/complete tiers; --read-only available). Uses your own Google OAuth client.  
  <sub>★ 3.5k · v2.3.0 (2026-10-30)</sub>
- **[google-workspace-official](https://developers.google.com/workspace/guides/configure-mcp-servers)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Google's official remote servers, one per product: Gmail (drafts only, no send), Drive, Docs, Sheets, Slides, Calendar, Chat, People. Developer Preview; needs a Google Cloud project and your own OAuth client.
- **[placecall](https://voygr.tech/placecall/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  VOYGR's PlaceCall lets an agent phone US businesses for bookings, inquiries and quotes. An AI voice agent places a real outbound call, gets through phone menus and hold, passes the business's questions back to you mid-call, and returns the outcome, transcript and recording; it can also suggest businesses to call. Calls are for businesses only, and none go to Indiana, Louisiana, Minnesota, Montana or Nebraska. The terms make you responsible for consent, call-recording and robocall law. Calls placed over MCP open with a recorded-line notice that names PlaceCall but does not say the caller is an AI; asked directly, the agent says it is a digital assistant. Hosted at `https://api.voygr.tech/mcp` (OAuth sign-in or API key). 250 free calls (up to 25 a day), then $0.10 per call that gets a result; calls that get nothing are free. The calling service is closed source; the plugin and skill repo is MIT.
- **[slack](https://docs.slack.dev/ai/slack-mcp-server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Slack's hosted MCP server (`https://mcp.slack.com/mcp`): search channels, send messages, manage canvases. OAuth with per-tool scopes; workspace admins approve and manage access.
- **[social-expert](https://socialexpert.app/tiktok-mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  TikTok content research and draft feedback from Social Expert (ForUsApps, LLC; not affiliated with TikTok): trending video formats and their sounds, posting times by audience market, keyword and hashtag suggestions, content ideas, and timestamped feedback on an uploaded MP4/MOV draft. Uploading and analysing a draft creates a saved report (kept 14 days) and uses up your allowance; it does not post, schedule or edit videos. Hosted at `https://api.socialexpert.app/functions/v1/mcp` (OAuth with a Social Expert account). Free: 10 research lookups and 3 video reviews, once; after that a paid monthly plan, with prices shown in your account. No public server source.
- **[synento](https://synento.com/docs/guides/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Synento's server for its live-video API, where every session is also its recording: a coding agent creates projects and sessions, mints short-lived connection tokens and restricted `rk_live_` server keys for your app, reads a session's manifest and checks that each participant's camera and mic tracks actually hold media (`verify_session`, and `run_media_check`, which runs a short synthetic call as real usage). 11 tools. Hosted at `https://api.synento.com/mcp`, OAuth 2.1 sign-in where you pick the projects and permissions (or a dashboard agent token for headless clients); it cannot see owner keys, change billing or delete anything. Free plan of 10,000 participant-minutes a month, then $0.003 a participant-minute. No public server source.
- **[telegram](https://github.com/chigwell/telegram-mcp)** — 🏷️ community ⚠️ mutating  
  Read and send Telegram messages, chats, contacts, and media as your own user account (Telethon session), not a bot.  
  <sub>★ 1.9k · v3.3.4 (2026-10-31)</sub>

## Relational Databases

- **[clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  ClickHouse's official server: `run_query`, `list_databases`, `list_tables` (plus chDB). Read-only by default; writes need `CLICKHOUSE_ALLOW_WRITE_ACCESS=true`, and destructive statements also need `CLICKHOUSE_ALLOW_DROP=true`. ClickHouse Cloud users can instead use the hosted remote MCP at `https://mcp.clickhouse.cloud/mcp` (OAuth, SELECT-only, enabled per service).  
  <sub>★ 900 · v0.7.0 (2026-09-21)</sub>
- **[mysql](https://github.com/benborla/mcp-server-mysql)** — 🏷️ community ⚠️ mutating  
  MySQL via one `mysql_query` tool: read-only by default; INSERT/UPDATE/DELETE each enabled by env flag. Multi-DB mode, SSH tunnelling, optional HTTP transport.  
  <sub>★ 2.2k · v2.0.9 (2026-06-19)</sub>
- **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** — 🏷️ community ⚠️ mutating  
  Postgres MCP Pro (Crystal DBA): index tuning, EXPLAIN plans with hypothetical indexes, health checks, and schema-aware SQL. Unrestricted read/write mode, or a restricted read-only mode with time limits. Last PyPI release is v0.3.0 (May 2025); main has newer fixes.  
  <sub>★ 3.4k · v0.3.0 (2025-05-16)</sub>
- **[supabase](https://github.com/supabase/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Supabase's official server (`https://mcp.supabase.com/mcp`): database, docs, and project tools. Scope it with `project_ref` and `read_only=true`.  
  <sub>★ 3k · mcp-server-supabase-v0.15.0 (2026-10-29)</sub>

## NoSQL & Document Databases

- **[mongodb](https://github.com/mongodb-js/mongodb-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  MongoDB's official server for databases and Atlas clusters: query, aggregation, CRUD, Atlas admin. Run it locally (`--readOnly` restricts it to read tools) or use the Atlas-managed hosted endpoint `https://mcp.mongodb.com` (OAuth; org-level read-only mode).  
  <sub>★ 1.2k · v3.2.1 (2026-10-28)</sub>
- **[neo4j](https://github.com/neo4j/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Neo4j's official local server: `read-cypher` and `write-cypher` tools against your graph; `NEO4J_MCP_READ_ONLY=true` disables writes. Aura users can instead use the hosted MCP for Aura (`https://<INSTANCE_ID>.mcp-instances.neo4j.io`, OAuth).  
  <sub>★ 304 · v2.0.0 (2026-10-28)</sub>

## Vector & Memory Stores

- **[brainattic](https://brainattic.ai/docs/connect)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Finite Software Systems' hosted team knowledge base for agents: hybrid keyword and semantic search (`kb_documents_search`, `kb_chunks_retrieve`) and document reads, and, where workspace permissions allow, creating, editing (staged edit sessions), archiving and restoring documents with version history, plus projects, groups, human-written rules, versioned skills, attachments and reminders. EU-hosted at `https://app.brainattic.ai/api/mcp` (OAuth 2.1 with dynamic client registration; Brainattic account required). Currently a free pilot. No public server source; the GitHub repo holds docs (CC-BY-4.0).
- **[brethof-brain](https://brethof.ai/brain/)** — 🆕 new 🏷️ brethof ⚠️ mutating ☁️ hosted  
  Persistent memory for AI agents across sessions, projects and machines. Every session opens with a brief — your standing rules, what each project is, where the last sessions stopped — and the records that bear on a prompt arrive with it. It curates itself into records per project, keeps the full chat history searchable, and adds notes, playbooks and an optional graph of decisions: each one dated, with its reason and what it replaced, returned alongside search results. Proven on twenty platforms, including Claude Code, Codex, Gemini CLI, GitHub Copilot CLI, OpenCode, OpenClaw and Hermes Agent on Linux and Windows, and Cline on Linux. Memory lives on your machine (local edition, Docker or Podman) or encrypted under a passphrase only you hold (hosted); each exchange is processed by our hub, which keeps none of it. Free tier; the client is source-available. Disclosure: maintained by us.
- **[chroma](https://github.com/chroma-core/chroma-mcp)** — 🏷️ official ⚠️ mutating 🔒 local  
  ChromaDB collections, similarity search, persistent embeddings (ephemeral, persistent, HTTP or Chroma Cloud client). Still the server in Chroma's docs, but unmaintained: no release since v0.2.6 (Aug 2025), a reported SQL-injection issue and 15 PRs sit unanswered, and it pins an MCP SDK version with published security advisories.  
  <sub>★ 601 · v0.2.6 (2025-08-14)</sub>
- **[claimidx](https://github.com/claimidx/claimidx)** — 🆕 new 🏷️ official ⚠️ mutating  
  Shared index of known software failures and their fixes, for coding agents: ask before retrying, then record the fix. Runs locally (PyPI `claimidx`, Apache-2.0) but connects to a public commons at home.claimidx.com by default and syncs with it at session start. Since v0.7.14, publishing a claim to the commons asks for confirmation (earlier versions shared automatically); `CLAIMIDX_COMMONS=0` turns the commons off.  
  <sub>★ 3 · v0.7.22 (2026-10-24)</sub>
- **[contextstream](https://github.com/contextstream/mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Persistent memory and code search for coding agents: saves decisions, lessons, and plans across sessions. Indexing sends your source code to ContextStream's hosted service, and transcript saving and Git metadata capture are on by default. The client is MIT; the hosted backend is closed. Free tier: 10,000 credits a month, no card.  
  <sub>★ 44 · v1.0.55 (2026-11-01)</sub>
- **[moss](https://www.npmjs.com/package/@moss-tools/mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating  
  Moss's server for its semantic search service (17 tools): semantic, keyword or hybrid search over your Moss indexes, run locally once an index has been downloaded into memory. It also creates, fills and deletes indexes and documents, builds indexes from local PDF or DOCX files (with OCR) and crawls websites into indexes. Runs locally over stdio (`npx -y @moss-tools/mcp-server`, currently a beta) and needs a Moss project ID and key; needs glibc Linux, macOS or Windows (no Alpine). Free Developer plan (1 project, 3 indexes), paid plans from $30 a month. The npm package is MIT and ships readable compiled JavaScript; its source repo is not public.
- **[pinecone](https://github.com/pinecone-io/pinecone-mcp)** — 🏷️ official ⚠️ mutating  
  Pinecone's Developer MCP: search Pinecone docs, list, describe and create indexes, upsert and search records or documents, and rerank. Runs with `npx @pinecone-database/mcp` and an API key (docs search works without one). Works with document indexes (full-text search and/or integrated embedding) and integrated-inference indexes; search with your own vectors is not supported. Separately, each Pinecone Assistant is a hosted MCP endpoint for retrieving context.  
  <sub>★ 72 · v0.4.0 (2026-10-29)</sub>
- **[qdrant](https://github.com/qdrant/mcp-server-qdrant)** — 🏷️ official ⚠️ mutating  
  Semantic memory on Qdrant: store text with metadata and search it (`qdrant-store`, `qdrant-find`); a missing collection is created automatically. Connects to a Qdrant URL or runs an embedded local database. Last release v0.8.1 (Dec 2025).  
  <sub>★ 1.6k · v0.8.1 (2025-12-10)</sub>
- **[weaviate](https://docs.weaviate.io/weaviate/configuration/mcp-server)** — 🏷️ official ⚠️ mutating  
  MCP server built into Weaviate (GA in v1.38; `MCP_SERVER_ENABLED=true`, served at `/v1/mcp`, always on in Weaviate Cloud): hybrid search, collection config, tenant listing, object upsert. Self-hosted defaults to read-only (`MCP_SERVER_WRITE_ACCESS_ENABLED=true` for writes); respects RBAC. Replaces the deprecated standalone server.

## Productivity & Notes

- **[airtable](https://support.airtable.com/articles/9897799762-using-the-airtable-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Airtable's hosted MCP server (`https://mcp.airtable.com/mcp`): bases, tables, records. OAuth or personal access token.
- **[apple-notes](https://github.com/sweetrb/apple-notes-mcp)** — 🏷️ community ⚠️ mutating 🔒 local  
  Read, search, create, edit, organise, and export Apple Notes on macOS via AppleScript, Shortcuts, and read-only access to the Notes database; no network requests.  
  <sub>★ 174 · v2.15.16 (2026-10-30)</sub>
- **[cloud-alter-ego](https://cloudalterego.cafeboon.com)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Cloud Alter Ego's hosted connector gives every AI chat your rules, profile, contexts, journals and playbooks, kept as plain Markdown files in your own OneDrive, Google Drive, Dropbox, GitHub or Azure DevOps (9 tools: `start`, `open_context`, `log`, `remember`, `new_context`, `list_files`, `read_file`, `write_file`, `choose_repo`). It writes to that storage (journal lines after answers, new rules and contexts; on GitHub and Azure DevOps every change is a commit), and the maker says it passes files through memory only while a tool runs and keeps no content. Endpoint `https://cloudalterego.cafeboon.com/mcp` (Streamable HTTP, OAuth). The site lists no price. The hosted connector is closed source; the MIT repo is a separate Git-synced template for Claude Code and Codex.
- **[google-calendar](https://github.com/nspady/google-calendar-mcp)** — 🏷️ community ⚠️ mutating  
  Read, create, update, delete and respond to events across multiple accounts and calendars, with free/busy lookup. Uses your own Google OAuth client. (Google's own Calendar server is listed separately as a Developer Preview.)  
  <sub>★ 1.2k · v2.8.1 (2026-10-29)</sub>
- **[notion](https://developers.notion.com/guides/mcp/overview)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Notion's hosted MCP server: search the workspace, read and edit pages in Markdown. OAuth, respects each user's existing permissions. (The self-hosted makenotion/notion-mcp-server is no longer maintained.)
- **[process-street](https://www.process.st/help/docs/mcp-server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Process Street's hosted server: workflows, workflow runs, tasks, users, data sets and reports. It can create and manage runs and assigned tasks within your Process Street permissions. `https://mcp.process.st/` (OAuth sign-in, including SAML SSO organisations, or an admin-generated API key). Needs a paid plan after a 14-day trial. No public source.
- **[screenpipe](https://github.com/screenpipe/screenpipe/tree/main/packages/screenpipe-mcp)** — 🆕 new 🏷️ official ⚠️ mutating  
  Search your recorded screen text, audio transcripts, meetings, and activity summaries; can also control recording, run pipes, and edit memories. Reads your full screen and audio history, so grant it with care. Source-available under the Screenpipe Commercial License (not an OSI open-source licence).
- **[tale](https://github.com/tale-project/tale)** — 🆕 new 🏷️ official ⚠️ mutating  
  Tale's own MCP endpoint (`/api/v1/mcp`) on a Tale team workspace: `get_knowledge` retrieves your organisation's knowledge passages, and agents can author, validate, save and run the workspace's automations (`run_automation` tests against mocks; `run_deployed` runs them live). Coding agents sign in through the browser (OAuth, on by default since v0.5.89), or a client sends a Bearer API key plus an `X-Organization-Slug` header; no public shared endpoint. MIT, free to self-host; managed Cloud instances come with the paid Enterprise plan.  
  <sub>★ 40 · v0.5.95 (2026-11-01)</sub>
- **[zapier](https://docs.zapier.com/mcp/home)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Zapier's hosted MCP server (`https://mcp.zapier.com/api/v1/connect`): 40,000+ actions across 9,000+ apps using the accounts you've connected in Zapier. OAuth or connection token (send it in a header, not the URL). Each successful call uses 2 tasks from your Zapier plan.

## Design & Creative

- **[cadre](https://github.com/ArthurBrioche/cadre-video-editor-plugin)** — 🆕 new 🏷️ official ⚠️ mutating 🔒 local  
  Bridge to Cadre, a screen recorder and non-destructive video editor for Apple Silicon Macs: start and stop recordings, then apply cuts, zooms, captions, and styling, preview, and export MP4 through the running app. The bridge is MIT; Cadre itself is proprietary, and export needs a Cadre Pro subscription.  
  <sub>★ 0 · mcpb-v1.2.3 (2026-09-30)</sub>
- **[figma](https://developers.figma.com/docs/figma-mcp-server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Figma's official server: design context, variables, screenshots and Code Connect for design-to-code; write tools create and edit native Figma/FigJam content (beta). Remote at `https://mcp.figma.com/mcp` (all plans; only clients in Figma's MCP Catalog may connect) or via the desktop app (paid Dev/Full seat). Rate limits by plan and seat.
- **[framethrower](https://github.com/framethrower-ai/framethrower-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted 💰 paid  
  FrameThrower's film-reference library: search stills from 5,489 films by concept, mood or colour or by cinematography attribute (lens, shot size, setting, time of day, director, year), find similar frames, and get a frame's metadata, full-resolution image and link. The same connector searches a commercials library (spots, shots, credits, brand and director profiles) and an animation library; 16 tools, all read-only. Hosted at `https://framethrower.ai/api/mcp` (OAuth 2.1 sign-in). Calls are metered in credits: a new account gets 200 free (a search costs 2), then $20 buys 20,000. Results are references that link back to FrameThrower, not licences to the imagery. No public server source; the MIT repo holds docs and client configs.
- **[inkroom](https://inkroom.ai/en/solutions/mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  InkRoom's image server: generate images from text with GPT Image, Gemini and other models, edit from reference images, batch-generate variants, upscale (2x, 4x, anime, face restoration) and fetch finished images (`generate_image`, `derive_image`, `batch_generate`, `upscale_image`, `wait_images`), with a credit estimate before each paid run. Without a token only three read-only tools answer: `help`, `list_models` (models and their credit prices) and `prompts` (published prompt examples). Hosted at `https://mcp.inkroom.ai`; generation and editing need an InkRoom account, a personal Bearer MCP token and paid credits, which the tools spend. No public server source; the GitHub repo holds the client, integration docs and skills, and its MIT grant covers only a few docs and example configs.
- **[mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)** — 🏷️ community ⚠️ mutating 🔒 local  
  Drive Blender via Python — modify scenes, objects and materials, render views, import Poly Haven/Sketchfab assets, generate 3D models. Formerly blender-mcp; the PyPI package is now `mcp-for-blender`. Sends anonymous usage telemetry by default (`DISABLE_TELEMETRY=true` to turn it off).  
  <sub>★ 33k · last push 2026-10-29</sub>
- **[orkas-video-studio](https://github.com/Orkas-AI/Orkas-VideoStudio)** — 🆕 new 🏷️ official ⚠️ mutating  
  Local-first video toolkit for coding agents: compose, edit, generate, and assemble videos from an editable `plan.json` timeline, through a CLI and an MCP server. Early development: install from source, since the npm packages aren't published yet. Optional generation calls providers with your own keys. MIT.  
  <sub>★ 339 · last push 2026-10-27</sub>
- **[pic2svg](https://pic2svg.com/mcp/)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Traces a raster image (PNG, JPG, WebP, GIF, BMP, TIFF) into an SVG of filled paths with pic2svg's vtracer-based engine; one tool, `trace_image_to_svg`. The image is uploaded and traced on pic2svg's server, not offline. Hosted at `https://pic2svg.com/api/mcp` (send the image as base64, get SVG text back), or a dependency-free stdio client from the GitHub repo `szj2ys/pic2svg-mcp` (Node 20+, install from source, not on npm) that reads a local file and writes the SVG to disk, overwriting any file already at that path. No account or key; free within a daily allowance (50 traces per client by default). pic2svg's free and Starter plans carry a personal-use licence; commercial use needs a paid plan. Client MIT; the tracing service is not open source.
- **[playable-gift](https://playablegift.com/agents)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Playable Gift's server (8 tools): makes a small browser game about one person from habits or inside jokes the sender supplies, returns a play link to share, and saves and revises self-written HTML games as private drafts. Hosted at `https://playablegift.com/mcp` with no sign-in; once the daily free pool for assistants is used up, it asks for an email-code sign-in or hands off to the website. Free within daily limits; optional subscription for more games. Its terms let it store and share, license or sell game content, including the names in it, after asking for consent. No public source.
- **[sfxmint](https://github.com/sfxmint/sfxmint-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  SFXMint's server (4 tools): finds sound effects for apps and games by interface event, by one of 18 sets or by description, and returns permanent download URLs. Hosted at `https://sfxmint.com/mcp`; no account or key needed. Free use is MP3 with limits (20 lookups and 5 downloads a day per network; a free account's API key gives 100 lookups and 20 downloads a month); a one-time download pack ($9.90 for 30 days, $69 for a year) lifts the limits and adds WAV. Sounds are AI-generated or procedurally synthesized and dedicated to the public domain under CC0 1.0; SFXMint no longer makes new sounds. No public server source; the repo (connection docs and an Agent Skill) is CC0.  
  <sub>★ 6 · last push 2026-10-31</sub>
- **[videogen](https://github.com/video-gen/videogen-mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  VideoGen's server (50 tools): generate and edit videos, images, voiceovers, music and avatars, upload assets, run workflows and export editable projects. Hosted at `https://mcp.videogen.io/mcp` (OAuth or API key) or `npx @videogen/mcp` locally, which still calls the VideoGen API: prompts and assets go to VideoGen and actions can spend credits. Free plan with limits (watermarked exports). MIT. [MCP setup and client configuration](https://videogen.io/videogen-mcp).  
  <sub>★ 4 · last push 2026-10-25</sub>

## Operations & Infrastructure

- **[aws](https://github.com/awslabs/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  AWS's official MCP servers: an open-source monorepo of local servers (docs, IaC, Bedrock, S3, and more), plus the AWS-hosted AWS MCP Server (`https://aws-mcp.us-east-1.api.aws/mcp`, part of Agent Toolkit for AWS since May 2026) that calls any AWS API and searches AWS docs. No extra charge; you pay for the AWS resources used.  
  <sub>★ 9.9k · 2026.10.20261030201955 (2026-10-30)</sub>
- **[azure](https://github.com/microsoft/mcp/tree/main/servers/Azure.Mcp.Server)** — 🆕 new 🏷️ official ⚠️ mutating  
  Microsoft's official Azure MCP Server (GA in 2.0): tools for 45+ Azure service areas (storage, databases, monitoring/KQL, deployments). Runs locally via `npx -y @azure/mcp@latest server start`, NuGet, PyPI or Docker, or self-hosted remotely. Entra ID via Azure Identity, respects RBAC; `--read-only` blocks writes. MIT.
- **[cloudflare](https://github.com/cloudflare/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Cloudflare's official API server (`https://mcp.cloudflare.com/mcp`): the whole Cloudflare API (~2,500 endpoints) through Code Mode `search`/`execute` tools. OAuth or API token. Cloudflare also runs product servers (docs, bindings, builds, observability, Radar, browser, logs) under `*.mcp.cloudflare.com`. Apache-2.0.  
  <sub>★ 1k · last push 2026-11-01</sub>
- **[datadog](https://docs.datadoghq.com/bits_ai/mcp_server/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Datadog's hosted MCP server (per-site endpoints, e.g. US1 `https://mcp.datadoghq.com/api/unstable/mcp-server/mcp`; not GovCloud): logs, metrics, monitors, dashboards, incidents, chosen via `?toolsets=`. OAuth, access token or API+app keys; write tools need the `mcp_write` permission.
- **[docker-mcp-gateway](https://github.com/docker/mcp-gateway)** — 🏷️ official ⚠️ mutating  
  Docker's MCP Toolkit CLI plugin (`docker mcp`): runs catalog MCP servers in isolated containers behind one gateway, with Docker Desktop secrets management.  
  <sub>★ 1.6k · last push 2026-10-26</sub>
- **[grafana](https://github.com/grafana/mcp-grafana)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Grafana's official server: dashboards, datasource queries, alerting, incidents, annotations. Can create and update dashboards, alerts and incidents; --disable-write makes it read-only. Grafana Cloud users can connect to the hosted https://mcp.grafana.com/mcp (OAuth) instead.  
  <sub>★ 3.6k · v2.1.1 (2026-10-20)</sub>
- **[helm](https://github.com/zekker6/mcp-helm)** — 🏷️ community 🛡️ read-only  
  Query Helm chart repositories and OCI registries: list charts and versions, read values, contents, dependencies and images. Cannot touch cluster releases. Public instance at https://mcp-helm.zekker.dev/mcp.  
  <sub>★ 28 · v1.4.3 (2026-10-23)</sub>
- **[kilobat](https://github.com/seifip/kilobat-cli)** — 🆕 new 🏷️ official ⚠️ mutating 🔒 local  
  macOS network diagnostics from the Kilobat CLI (`kilobat mcp`, local stdio): live per-app traffic, connection and DNS diagnosis, Wi-Fi signal and channels, speed and DNS benchmarks, traceroute, VPN leak checks, local devices, about 85 tools. Some tools change the Mac: set DNS servers, reconnect Wi-Fi, keep the Mac awake, AirDrop visibility, and (with the separate Kilobat Mac app) app and domain blocking, budgets and quotas; settings changes may ask for confirmation or admin rights. Network checks contact test endpoints; speed tests transfer data. Install with `brew install seifip/kilobat/kilobat` (macOS 14+, builds from source with Xcode 16+). No account. The CLI is free and GPL-3.0-only; the Mac app is a separate product with free and paid features.
- **[kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** — 🏷️ community ⚠️ mutating  
  kubectl-equivalent operations on the configured cluster.  
  <sub>★ 1.6k · v4.2.1 (2026-10-26)</sub>
- **[remotify-mcp](https://github.com/onlsol/relay.remotify.run/tree/main/mcp)** — 🆕 new 🏷️ official ⚠️ mutating 🔒 local  
  Run shell commands on a remote machine without SSH, three tools: `remote_exec`, `remote_session_info` and `remote_session_reset`. You paste a `curl ... | bash` one-liner on the remote; it polls a relay over HTTPS and runs each command after a y/N prompt (supervised) or without asking (auto mode). Runs locally over stdio (`npx -y remotify-mcp@latest`) and uses Online Solution's free public relay at relay.remotify.run by default, or your own (Docker, `REMOTIFY_URL`). Commands and output pass through the relay, anyone holding the 128-bit session key can queue commands, and the relay supplies the wording of the status messages the tool returns to the assistant. No account or key. Apache-2.0.
- **[saas-pro-max](https://saaspro.dev/docs/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  SaaS Pro Max's server for its analytics and monitoring console (44 tools): web and product analytics, funnels, retention, people, errors, metrics, incidents, revenue and Meta ads reports. With write or admin scope it also creates apps, funnels, feature flags and alert rules, updates people and error status, creates ingest keys and runs Management API operations; protected actions wait for a member's passkey approval. Hosted at `https://saaspro.dev/api/mcp` (OAuth with PKCE; you grant read, write or admin scope for one organization, and your role still applies); also a stdio package (`npx -y @saaspro/mcp` with an access token). Free plan (50,000 events a month), paid plans from $12 a month. No public server source; the npm package is MIT, but the repo it links to is not public.
- **[sentry](https://github.com/getsentry/toolkit)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Sentry's official server: issues, events, traces, logs, replays, releases, alerts and monitors; can update issues and projects, create teams and DSNs, and create or delete alert rules and monitors. Hosted at `https://mcp.sentry.dev/mcp` (OAuth) or stdio via `npx @sentry/mcp-server` for self-hosted Sentry; AI search tools need your own LLM key. Licence: FSL-1.1-Apache-2.0.  
  <sub>★ 952 · 0.42.0 (2026-09-25)</sub>
- **[shipvela](https://github.com/stefanautomateed/shipvela-codex)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Public beta. Create hosting projects, deploy a connected GitHub repo or a small static site, and read deployment status, build logs, and usage. Hosted at `https://shipvela.com/mcp` (OAuth with PKCE); free Hobby plan, and each publish counts against your plan's allowance. Plugin files are MIT per the README; the hosted service is proprietary.  
  <sub>★ 0 · last push 2026-10-05</sub>
- **[vercel](https://vercel.com/docs/agent-resources/vercel-mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Vercel's hosted MCP server (`https://mcp.vercel.com`): docs search, teams, projects, deployments and logs, Web Analytics; can deploy code and make purchases. OAuth; only Vercel-approved clients can connect. Acts with your full Vercel account access. All plans.

## AI & ML Platforms

- **[ai-model-watch](https://github.com/markksantos/ai-model-watch)** — 🆕 new 🏷️ official 🛡️ read-only  
  Lists the models each AI provider's API serves (OpenAI, Anthropic, Gemini, Mistral, xAI, DeepSeek, OpenRouter) and reports which model IDs are new since the last check. Two tools: `check_new_models` (IDs each provider started listing since the previous call, kept in a local state file under `~/.cache`) and `list_models` (what one provider lists now, with a substring filter). It only calls the providers' list-models endpoints, which spend no tokens, and changes nothing but its own state file. Runs locally over stdio (`npx -y github:markksantos/ai-model-watch --mcp`, or Homebrew); OpenRouter needs no key, the other providers use your own API key from the environment and are skipped without one. Free, MIT, no dependencies.
- **[aident-loadout](https://aident.ai)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Gateway that lets an agent use third-party apps and tools (Gmail, Slack, Linear, Notion, HubSpot, and more) through your connected accounts, with credentials in Aident's vault and an audit history, plus a catalogue of 400+ Aident-curated Skills (workflow guides that combine those actions). Hosted at `https://loadout.aident.ai/mcp` (OAuth); free to start, with top-ups for more usage. The [skill repo](https://github.com/Aident-AI/aident-skill) is MIT; the service is proprietary.
- **[api-market](https://api.market/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Gateway to the API.market catalogue of 600+ third-party APIs (3,810+ tools: image and video generation, search, scraping, maps, data). Hosted at `https://api.market/api/mcp/gateway` (OAuth or API key). Calls can spend free-tier quota or pay-as-you-go wallet funds. Proprietary; no public source.
- **[huggingface](https://github.com/huggingface/hf-mcp-server)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Hugging Face's official server: Hub search and details, docs search, Gradio Spaces as tools, plus optional repo creation, Jobs and Sandboxes. Hosted at https://huggingface.co/mcp or run locally.  
  <sub>★ 313 · v0.4.32 (2026-10-26)</sub>
- **[plugmcp-directory](https://github.com/plugmcp-ai/plugmcp-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  One MCP server that finds the rest: search 70,000+ MCP servers and agent skills, compare them, and get the exact install config for Cursor, Claude, VS Code, Codex, Grok Bot and more (9 read-only tools). Hosted at `https://plugmcp.ai/mcp-server` with no required login, or run locally with `npx -y plugmcp-mcp`. Optional free `pb_live_` API key raises rate limits. Official registry name `ai.plugmcp/directory`. MIT. Published by PlugMCP.
- **[runapi](https://github.com/runapi-ai/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Browse a catalog of image, video, music, and text-to-speech models, check current pricing, and create and poll generation jobs. Hosted at `https://mcp.runapi.ai/mcp` (OAuth or API key) or local via `npx @runapi.ai/mcp`, whose catalog tools work without an API key; jobs spend prepaid pay-as-you-go credits.  
  <sub>★ 56 · v0.17.0 (2026-10-29)</sub>

## Specialised / Vertical

- **[agent-payment-node](https://github.com/nuanu-ai/agent-payment-node)** — 🆕 new 🏷️ official ⚠️ mutating 🪙 crypto  
  Agent Payment Node (APN), a local payment runtime for AI agents: wallets on EVM networks, Solana and TRON, balances, direct transfers, x402 purchases, gasless USDC transfers, bridges and swaps, each kept as a durable operation with status, resume and receipt tools. It spends real money. The owner sets per-asset caps in an allowlist policy, and commands that sign (transfers, EVM x402, swaps, bridges) don't run over MCP: the server returns the exact command for the owner to approve in a terminal. The exception is Solana x402 (`x402 solana pay`), which pays unattended within the owner's policy. Stdio server (`apn mcp serve`) for Apple Silicon macOS only, installed with `brew install nuanu-ai/tap/apn` (Node 24); wallet keys are encrypted with a secret held in the macOS Keychain, and payments go out to the blockchains and providers. The software is free; network and provider fees apply. MIT.
- **[aiagentcycle](https://github.com/aiagentcycle/aiagentcycle-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Read-only server about AIAgentCycle, a Dutch company (trade name of Good Nature Vibe B.V.) that builds n8n automations and AI agents for small businesses: its services with indicative prices, the 190 systems it integrates, case studies, FAQ, contact details and full-text search over its website, in Dutch and English (10 tools). Covers only the company's own public content. Hosted at `https://mcp.aiagentcycle.com/mcp` (no login, free). MIT.
- **[blockvectra](https://github.com/blockvectra/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 🪙 crypto  
  BlockVectra's server for EVM chain access on 13 networks (Ethereum, Base, Arbitrum, BNB Chain, Polygon and others), 15 tools: search and read its docs, list chains with the JSON-RPC methods each allows, check live status, prices and cost estimates, and run read-only JSON-RPC calls. With an API key it also queries the Data API (balances, transfers, token holders, DEX swaps, NFTs) and broadcasts transactions signed elsewhere (`send_raw_transaction`); it does not sign or hold private keys. Hosted at `https://docs.blockvectra.com/mcp`; docs, chain lists, status and pricing need no key, and keyless RPC is limited to each chain's public methods. A key (sign up with GitHub, Google or an Ethereum wallet) includes 30 million free compute units per 30-day cycle; past that it is pay-as-you-go, funded only by sending USDC, USDT or USDG to your account's deposit address (eth_call works out to $1.50 per million calls). The MIT repo holds a stdio bridge and client configs; the hosted backend is not public.
- **[blossom-research](https://www.moreblossom.com/connect)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Search Blossom's catalogue of published psychedelic and mental-health research: papers, clinical-trial registrations, patent families, organization (stakeholder) profiles and editorial overviews, with source links. 20 read-only tools: search, read, count and summarize for each record type, plus a latest-research feed; it cannot change anything. Hosted at `https://www.moreblossom.com/mcp` (OAuth with a free Blossom account; 100 requests a day, 500 for supporters, 60 a minute). Research summaries, not medical advice. No public server source.
- **[careclinic](https://careclinic.io/careclinic-mcp/)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Your CareClinic health record in chat: today's medication schedule, recent symptoms and mood, and insights. A check-in tool logs entries after you confirm them. Hosted at `https://mcp.careclinic.io/mcp` (OAuth with your CareClinic account). Handles personal health data. No public source; the repo is all rights reserved.
- **[carejobs-now](https://github.com/yumaheymans/carejobs-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  CareJobs.Now's server for US healthcare jobs: search open jobs for nurses, CNAs, doctors, therapists, techs and other care roles, read daily from employers' own career sites plus Adzuna and USAJOBS, with the pay each posting states; also posted pay by kind of job, open jobs by state, and employer lookups (6 tools). Every result links to the job's page on CareJobs.Now, which links to the employer's application. Hosted at `https://carejobs.now/api/mcp`, free, no key or account. The site earns referral fees from some staffing agencies and AI-training programs it links, disclosed beside those links. The server source is private; the MIT repo holds docs, `server.json`, a Claude Code plugin and an Agent Skill.
- **[datacircle](https://datacircle.dev)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Datacircle's hosted MCP over its benchmark of GTM data APIs (people, email and phone, companies, social media, e-commerce, real estate, web): list the APIs it tracks, and search every provider's plans with price per 1,000 results, rate limits and Datacircle's own score, best first (2 tools). Read-only, open to anyone with no key. Endpoint `https://api.datacircle.dev/mcp`. Docs: https://datacircle.dev/SKILL.md. No public server source.
- **[dchub](https://github.com/azmartone67/dchub-mcp-server)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  DC Hub's server for data-center site selection: facilities and markets, grid and interconnection queues, power, gas and energy prices, fiber, permitting and M&A deals, with DC Hub's Data Center Power Index (DCPI), a daily score of where data centers can get grid power across 300+ markets (94 tools). Also saves sites and shortlists, sets email and webhook alerts, and sends capacity introduction requests to providers. Hosted at `https://dchub.cloud/mcp`; previews need no key, a free key adds two full answers per tool per day (more with an email), and full results need a paid plan or credit pack, or a per-call Stripe payment on some tools. Logs every tool call, with its parameters, to DC Hub (kept 90 days). The MCP gateway is MIT; the data backend it calls is not public.  
  <sub>★ 3 · v2.12.44 (2026-10-27)</sub>
- **[fincept](https://docs.fincept.in)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Fincept Terminal's hosted server (`https://enterprise.fincept.in/mcp`, OAuth 2.1): market quotes and candles, options and futures, fundamentals, economic series and SEC filings, news and sentiment, screeners, backtests, portfolio analytics and quant engines (about 440 tools). Trading tools reach only the Fincept Paper account, no real money; tools spend plan credits. Needs the paid Fincept Exclusive Pro plan. The server source is private; the public repo holds docs only.
- **[good-nature-vibe-catalog](https://github.com/aiagentcycle/gnv-catalog-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Read-only catalog for Good Nature Vibe, a Dutch web shop for natural wellness products, mainly CBD and CBG oils: product search, one product with its variants and price range, and the shop's pages and blog posts, in five store languages (6 tools). It cannot touch accounts, carts or checkout, and prices are catalog prices, not checkout quotes. Covers only this shop. Hosted at `https://catalog-mcp.goodnaturevibe.com/mcp` (no login, free). MIT. Run by Good Nature Vibe B.V., which also runs AIAgentCycle.
- **[google-ads-transparency-mcp](https://github.com/GeminiGeorge22/google-ads-transparency-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted 💰 paid  
  An advertiser's Google ads from Google's public Ads Transparency Center: give it website domains, advertiser IDs, Transparency Center links or exact advertiser names and get one row per ad with format, status (new, running or stopped within a window you set), first and last shown dates, days shown and the ad link, optionally filtered by country and with per-country stats. One read-only tool that runs the maker's Apify Actor `publicrecords/google-ads-transparency-scraper` (an unofficial scraper, not a Google API). Hosted by Apify at `https://mcp.apify.com?tools=publicrecords/google-ads-transparency-scraper` (Apify OAuth or your own Apify token), or a small MIT stdio proxy (`uvx google-ads-transparency-mcp-server` or `npx -y github:GeminiGeorge22/google-ads-transparency-mcp`) that lists the tool without a token and forwards calls to that endpoint. Billed to your Apify account: $1 per 1,000 ads plus $0.002 per run; Apify's free plan includes $5 of usage a month. The Actor's source is not public.
- **[holos33](https://github.com/aiagentcycle/holos33-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Read-only server about Holos33, a wellbeing app (stress, sleep, breathing, hypnosis, nutrition, movement) currently in free, waitlisted Early Access: its modules, knowledge-base articles, site pages, FAQ, access and pricing, privacy and data handling, and partner information (11 tools). Covers only Holos33's own public content; Holos33 states it is not medical care. Hosted at `https://mcp.holos33.com/mcp` (no login, free). MIT. Run by Good Nature Vibe B.V., which also runs AIAgentCycle.
- **[hubspot](https://developers.hubspot.com/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  HubSpot's hosted MCP server (`https://mcp.hubspot.com`): read and write CRM records, activities, content, campaigns and pipelines. OAuth with PKCE via an MCP connector you create in HubSpot. A local developer MCP server ships with the HubSpot CLI (`hs mcp setup`).
- **[invokely](https://invokely.ai/docs)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Official statistics with their sources: search indicators and places, get values and time series, compare and rank places (U.S. states and counties, EU countries and NUTS 2 regions, Spanish municipalities, World Bank data for every country). Hosted at `https://invokely.ai/mcp` (OAuth or API key; free plan of 500 calls a month) plus a no-account trial endpoint at `https://invokely.ai/mcp/trial` (25 calls a day). Proprietary; no public source.
- **[invompt](https://github.com/Invompt/invompt-mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  Create, revise, archive, and email invoices, quotes, estimates, and pro formas from chat. Hosted at `https://mcp.invompt.com/mcp` (OAuth); you can start without an account, but emailing documents needs a registered one. The MIT repo also has a local-beta CLI.  
  <sub>★ 0 · last push 2026-11-01</sub>
- **[jobspipe](https://github.com/jobspipe/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  JobsPipe's hosted MCP for live job postings from 30+ ATS feeds and job boards, normalized into one schema: search and read jobs, look up hiring companies and their tech stacks, search US WARN Act layoff notices, plus docs and pricing tools. Signed in, it can also save a search as a signal that alerts you by email, Slack or webhook (the one tool that writes, to your own account). Endpoint `https://mcp.jobspipe.dev/mcp` (OAuth or API key; free account with credits at jobspipe.dev/signup); a no-key demo at `https://jobspipe.dev/mcp` has three read-only tools, with job search capped at 3 rows a call. Docs: https://docs.jobspipe.dev/ai-agents/mcp. MIT repo with server card and client configs; the hosted backend is not public.
- **[kleap](https://github.com/kleaphq/cli)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  No-code website builder: create, edit, and publish sites, manage files, site databases, and custom domains (including a `buy_domain` tool). Hosted at `https://kleap.co/api/mcp` (OAuth) or a local stdio server from the MIT CLI; read-only API keys are available. AI edits use Kleap credits; there is a free plan.  
  <sub>★ 1 · last push 2026-10-18</sub>
- **[lifeverse](https://github.com/lifeversegu/lifeverse-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  LifeVerse's public catalogue of its own AI products and interactive experiences (11 listed, such as a parallel-life story simulator, a sales-practice coach and A-share stock screening and backtest tools): four tools list, search, show and recommend products, returning descriptions and links to the LifeVerse site. Product content and tool descriptions are in Chinese. Some listed products are paid one-time purchases on LifeVerse (Alipay); the server only reads the public catalogue and has no access to accounts or orders. Hosted at `https://lifeverse.gufreelancer.com/api/mcp` (no account or key, free). No public server source; the MIT repo holds docs and client configs.
- **[llm-pulse](https://llmpulse.ai/features/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  AI-search visibility analytics: brand mentions, citations, sentiment, and share of voice. With the write scope it can add prompts, competitors, tags, and annotations, generate content briefs, and launch audits. Hosted at `https://api.llmpulse.ai/api/v1/mcp` (OAuth 2.1; API key on Scale plan and above). Needs a paid LLM Pulse plan after a 14-day trial. The server source is private; the repo holds an MIT stdio wrapper.
- **[looot](https://github.com/loootai/looot-mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Pay-per-call gateway to about 2,400 runnable endpoints from about 80 third-party data providers (Hunter, People Data Labs, Lusha, Apify, DataForSEO, TikHub and others): work-email and phone finding and verification, people and company enrichment, LinkedIn and social profiles, SERP and SEO data, web scraping. It resells the providers' data, including contact details of named people. Catalog search and price checks are free; `run` spends prepaid credit, `top_up` returns a Stripe checkout link, and some endpoints act on accounts you connect (Gmail, Instantly). Hosted at `https://api.looot.ai/mcp` (OAuth or bearer token). No free tier or trial. Service source is private; the stdio bridge repo is MIT.  
  <sub>★ 3 · v1.0.3 (2026-10-11)</sub>
- **[madeonsol](https://github.com/MadeOnSol/mcp-server-madeonsol)** — 🆕 new 🏷️ official ⚠️ mutating 🪙 crypto  
  MadeOnSol's Solana trading-data server: KOL wallet trades and leaderboards, Pump.fun deployer reputation, token risk, holders and buyer quality, wallet PnL and holdings, and DEX trade data. Also creates and deletes webhooks, price and coordination alerts, copy-trade signal rules and watchlists on your MadeOnSol account; it does not place trades. Runs locally over stdio (`npm install -g mcp-server-madeonsol`) and calls the MadeOnSol API. Use a MadeOnSol API key (free tier 200 requests a day with delayed live feeds; some tools need a paid plan), or keyless x402: you put a Solana wallet's private key in an env var and the server signs USDC payments of $0.005 to $0.02 per call, within per-call and total caps you must set. MIT.  
  <sub>★ 2 · v0.2.0 (2026-04-03)</sub>
- **[mcp-probe-kit](https://github.com/mybolide/mcp-probe-kit)** — 🆕 new 🏷️ community ⚠️ mutating 🔒 local  
  Spec-driven development workflow for coding agents, 29 tools by default: `start_feature`, `start_bugfix` and other orchestrations, specs and estimates, `code_insight` (through an optional GitNexus code graph), `code_review`, `gentest`, `gencommit`, UI design-system helpers, and History Session tools that archive chat handoffs under `docs/history-session/`. It writes spec, plan and history files into your project; six optional Memory tools read and write a shared pool in a Qdrant instance and embedding service you run yourself. Local stdio (`npx -y mcp-probe-kit@latest`, Node 20+), no account or key. MIT.
- **[melso](https://melso.ai/en/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Melso's own server for its Spanish tax and bookkeeping service (gestoría): read invoices, customers, expenses, income, bank data, returns and the tax calendar; record, correct or delete expenses and income, save customers, draft invoices and, when the owner asks through their own connection, issue the saved version (Verifactu/TicketBAI), mark invoices paid and open cases for Melso's professionals. It cannot approve, file or pay a tax return; that stays in the Melso app. Hosted at `https://mcp.melso.ai/mcp` (OAuth, one company per connection); needs a Melso account on a plan with tool access (Pro for the self-employed: €49 a month), and the tools listed depend on plan and role. Run by Melso, not by Spain's tax agency. No public server source.
- **[neverapply](https://github.com/kasovy/neverapply-mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  NeverApply's hosted MCP for job search: search and read jobs without signing in; signed in (OAuth 2.1 with PKCE, no API key), match roles to your profile, tailor resumes, save screening answers, prepare for interviews, and submit applications to jobs you approve (15 tools). Endpoint `https://neverapply.co/mcp` (Streamable HTTP). Free to start, with paid tiers for higher volume. Docs: https://neverapply.co/features/mcp. Official registry `co.neverapply/neverapply`. The MIT repo holds only plugin manifests and skills; the server source is not public.
- **[Ormas Outcomes](https://ormas.ai/docs/first-task)** — 🆕 new 🏷️ official ⚠️ mutating 💰 paid  
  Ormas's local stdio MCP server hands bounded GitHub coding work to outside providers (miners on Bittensor subnet 76) with agreed automated acceptance checks, a spending limit you authorize, job tracking, and a returned branch and receipt. Its installer sets up the Python client and configures Codex or Claude Code on macOS 14+ and Linux x86_64 (Windows through WSL2). Early alpha and US-only; paid work needs an account, an Ormas key and credit. Assigned providers, Ormas-operated checkers and provider AI services can read the code you submit; private repositories need your consent. No public client source.
- **[pocket-drives](https://github.com/RevList/pocket-drives-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Search, quote, and check availability for peer-to-peer luxury, exotic, and EV car rentals from independent hosts (five US markets at listing time). Hosted at `https://pocketdrives.ai/mcp`, no auth; it does not book, which happens in the iOS app or on pocketdrives.ai. No public source or licence.  
  <sub>★ 0 · last push 2026-08-21</sub>
- **[robot-speed](https://www.robot-speed.com/mcp)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted  
  SEO tools: 12 free audit tools with no account at `https://www.robot-speed.com/api/mcp/free`; the full 39-tool server at `/api/mcp` (OAuth) also manages content, Search Console data, and reports, and needs a Robot Speed subscription after its trial. No public server source.
- **[sitepatent](https://sitepatent.com/mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Search the SitePatent directory of startups, SaaS and AI tools, seven tools: keyword search with category and pricing filters, a listing's full profile, alternatives to a named product, category browsing, the category tree, trending and the Site of the Day. Listings are submitted by their makers; paid ("verified") listings rank first in results, and outbound links carry SitePatent UTM tags. Hosted at `https://sitepatent.com/api/mcp` (no account or key, free to use). No public server source; the GitHub repo holds only a README.
- **[sports-odds-mcp](https://github.com/GeminiGeorge22/sports-odds-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted 💰 paid  
  Sportsbook odds from Kambi-powered books (BetRivers, Unibet, Paf, Svenska Spel, ATG and others; the maker counts 24): one row per game with each book's price and the best price per outcome, headline markets or the full board including props, pre-game or live. One read-only tool that runs the maker's Apify Actor `publicrecords/sports-odds-api`, which reads Kambi's odds feeds and switches Apify Proxy IPs when Kambi rate-limits it. Hosted by Apify at `https://mcp.apify.com?tools=publicrecords/sports-odds-api` (Apify OAuth or your own Apify token), or a small MIT stdio proxy (`uvx sports-odds-mcp` or `npx -y github:GeminiGeorge22/sports-odds-mcp`) that lists the tool without a token and forwards calls to that endpoint. Billed to your Apify account: $0.01 per game for headline markets or $0.03 with all markets, plus $0.005 per run; Apify's free plan includes $5 of usage a month. The Actor's source is not public.
- **[spotify](https://github.com/jamiew/spotify-mcp)** — 🏷️ community ⚠️ mutating 💰 paid  
  Spotify Web API: search, playback and queue control, playlists, and library, including podcasts and audiobooks (48 tools); updated for Spotify's February 2026 API changes. Needs your own Spotify developer app, and Premium for playback. Maintained fork of the now-inactive varunneal/spotify-mcp. Spotify's own connector is currently Claude-only.  
  <sub>★ 12 · v0.8.1 (2026-11-02)</sub>
- **[spotify-play-count-mcp](https://github.com/GeminiGeorge22/spotify-play-count-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted 💰 paid  
  Spotify play counts for every track behind a track, album, artist or playlist link, plus artist monthly listeners and followers, and streams per day for tracks the maker already tracks. One read-only tool that runs the maker's Apify Actor `publicrecords/spotify-play-count-scraper`, which scrapes Spotify's public web pages (no Spotify login; not affiliated with Spotify). Hosted by Apify at `https://mcp.apify.com?tools=publicrecords/spotify-play-count-scraper` (Apify OAuth or your own Apify token), or a small MIT stdio proxy (`uvx spotify-play-count-mcp` or `npx -y github:GeminiGeorge22/spotify-play-count-mcp`) that lists the tool without a token and forwards calls to that endpoint. Billed to your Apify account: $2 per 1,000 tracks, $5 per 1,000 artists, plus $0.002 per run; Apify's free plan includes $5 of usage a month. The Actor's source is not public.
- **[statsnet](https://github.com/usenetstate/statsnet-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Company background checks worldwide: registration, executives, government contracts, courts, and finances (`search_companies`, `get_company`). Hosted at `https://statsnet.co/mcp` with no auth; it returns the public company card only, while contacts, relations, and exports need a Statsnet subscription through its separate REST API. No public server source.  
  <sub>★ 0 · last push 2026-09-16</sub>
- **[stripe](https://docs.stripe.com/mcp)** — 🏷️ official ⚠️ mutating ☁️ hosted  
  Stripe's hosted MCP server (`https://mcp.stripe.com`): payments, customers, subscriptions, refunds via OAuth or agent API keys. Refunds and outbound payments need human confirmation. From 2026-10-31 it accepts only Agent-tagged keys or OAuth.
- **[synci](https://github.com/synciio/synci-mcp)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted 💰 paid  
  Read-only access to bank, brokerage, and crypto accounts connected through Synci: connection health, accounts, balance snapshots, transactions, and holdings (5 tools). Hosted at `https://api.synci.io/mcp` (OAuth; you pick which accounts the assistant sees); it cannot move money or trade. Needs an active Synci subscription. The repo holds docs and setup examples; no public server source or licence.  
  <sub>★ 0 · last push 2026-10-05</sub>
- **[trends-mcp](https://github.com/trendsmcp-ai/Trends-MCP)** — 🆕 new 🏷️ official 🛡️ read-only ☁️ hosted  
  Live trend data from Google Search, YouTube, TikTok, Reddit, Amazon, Wikipedia, news, app stores, npm, Steam, and more (`get_time_series`, `get_growth`, `get_top_trends`). Hosted at `https://api.trendsmcp.ai/mcp` or through the repo's MIT stdio adapter. Needs an API key, which comes with a free monthly quota.  
  <sub>★ 44 · last push 2026-08-29</sub>
- **[wine-labs](https://winelabs.ai/agents)** — 🆕 new 🏷️ official ⚠️ mutating ☁️ hosted 💰 paid  
  Fine-wine market data: wine and LWIN matching, retail and auction prices, exchange order books, merchants, and critic data, plus cellar CSV/Excel processing jobs. Hosted at `https://chat.wine-labs.com/mcp` (browser OAuth). Billed in credits: existing API allowance, monthly from $25, or pay-as-you-go from $5. No public server source.

## Frameworks & SDKs for Building MCP Servers

- **[fastmcp](https://github.com/PrefectHQ/fastmcp)** — 🏷️ community  
  Python framework for MCP servers and clients, now under PrefectHQ. FastMCP 1.0 was incorporated into the official Python SDK in 2024; this is the actively maintained standalone project.  
  <sub>★ 28.3k · v4.1.5 (2026-11-01)</sub>
- **[mcp-go](https://github.com/modelcontextprotocol/go-sdk)** — 🏷️ official  
  Official Go SDK for MCP servers and clients, maintained with Google. Single-binary deployment friendly. Apache-2.0 for new code, MIT for existing code.  
  <sub>★ 5.3k · v1.8.0 (2026-09-14)</sub>
- **[mcp-python](https://github.com/modelcontextprotocol/python-sdk)** — 🏷️ official  
  Reference Python SDK (PyPI `mcp`). v2 renamed the decorator-based `FastMCP` class to `MCPServer`; standalone FastMCP is a separate project.  
  <sub>★ 24.7k · v2.3.0 (2026-10-02)</sub>
- **[mcp-typescript](https://github.com/modelcontextprotocol/typescript-sdk)** — 🏷️ official  
  Reference TypeScript / Node SDK. v2 ships as `@modelcontextprotocol/server` and `@modelcontextprotocol/client`; v1 `@modelcontextprotocol/sdk` is maintained on the `v1.x` branch.  
  <sub>★ 13.7k · v2.4.0 (2026-10-23)</sub>
- **[xmcp](https://github.com/basementstudio/xmcp)** — 🆕 new 🏷️ community  
  basement.studio's TypeScript framework for building and deploying MCP servers: tools, prompts and resources are picked up from files, with hot reload, middleware, HTTP and stdio transports, MCP Apps (React UI), auth integrations, and adapters for Next.js, Express, NestJS, Hono and other web frameworks. Start with `npx create-xmcp-app@latest`. The CLI sends anonymous build telemetry by default (turn it off with `XMCP_TELEMETRY_DISABLED=true`). Its docs are also searchable through a free, keyless, read-only server at `https://xmcp.dev/mcp`. MIT.

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
