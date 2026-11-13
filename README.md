# MCP-Shield GitHub Action (`mcp-shield-action`)

Deterministic **SHA-256 MCP Tool-Pinning** and **Prompt-Injection CI Gate** for Model Context Protocol servers and agent repos.

## Quickstart
```yaml
- uses: mulak1/mcp-shield-action@v1
  with:
    target-path: '.'
    fail-on-injection: 'true'
```

## Live Cloud Deep-Audit & Hosted Proxy
- **Per-Call x402 Base USDC API (`$0.01`–`$0.02`/call)**: `https://api.exactbaseline.com/x402/v1/mcp-audit` ([Bazaar Catalog](https://api.exactbaseline.com/x402/v1/bazaar))
- **Managed Continuous Monitoring**: [Subscribe on Polar.sh](https://buy.polar.sh/polar_cl_rwOjs5Ghm1rAH1sckIFzKoEgvcD7Iwz7hjajA0hQuGX)
