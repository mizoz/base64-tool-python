#!/usr/bin/env python3
"""Base64 encode/decode tool."""
import sys, base64

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: base64_tool.py <string> [--decode]"); sys.exit(1)
    d = '--decode' in sys.argv
    t = ' '.join([a for a in sys.argv[1:] if not a.startswith('--')])
    print(base64.b64decode(t).decode() if d else base64.b64encode(t.encode()).decode())
