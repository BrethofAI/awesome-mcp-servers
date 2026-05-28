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
