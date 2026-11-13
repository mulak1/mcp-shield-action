#!/usr/bin/env python3
import hashlib, json, pathlib, re, sys

INJECTION_PATTERNS = [
    re.compile(r'ignore\s+(?:all\s+)?previous\s+instructions', re.I),
    re.compile(r'system\s*prompt|<\|im_start\|>|exfiltrate|curl\s+https?://', re.I),
]

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
fail_flag = (sys.argv[2].lower() == 'true') if len(sys.argv) > 2 else True
findings, pinned = [], 0
for p in root.rglob('*.json'):
    if '.git' in p.parts or 'node_modules' in p.parts:
        continue
    try:
        txt = p.read_text(encoding='utf-8')
        if 'mcpServers' in txt or 'inputSchema' in txt:
            digest = hashlib.sha256(txt.encode('utf-8')).hexdigest()[:16]
            pinned += 1
            print(f'[MCP-Shield] Pinned {p} -> sha256:{digest}')
            for rx in INJECTION_PATTERNS:
                if rx.search(txt):
                    findings.append(f'{p}: matched {rx.pattern}')
    except Exception:
        continue
print(f'[MCP-Shield] Audited {pinned} MCP schema file(s); findings={len(findings)}')
if findings:
    for f in findings:
        print(f'::error ::MCP-Shield Prompt-Injection Alert: {f}')
    if fail_flag:
        sys.exit(1)
