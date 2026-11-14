# MCP-Shield GitHub Action (`mcp-shield-action`)

Deterministic **SHA-256 MCP Tool-Pinning** and **Regex Heuristic Linter** for Model Context Protocol config files in developer CI pipelines.

> **Important Notice (`AS-IS` MIT Developer Utility)**: Provided strictly `AS-IS` without warranty of any kind. This utility performs static regex/hash linting only and is **not** a security certification, audit seal, or guarantee against vulnerabilities.

## Quickstart
```yaml
- uses: mulak1/mcp-shield-action@v1
  with:
    target-path: '.'
    fail-on-injection: 'true'
```
