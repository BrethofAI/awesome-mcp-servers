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
