# Part C - MCP acceptance

The local stdio MCP server is `mcp/date_server.py`. `mcp/probe.py` discovered
the `current_date` tool and called it through JSON-RPC. The `call.result.content`
text is the real value returned by the server; it is not hard-coded in the
probe.

Run:

```powershell
python mcp/probe.py
```

Captured output (2026-09-08):

```json
{
  "tool": "current_date",
  "server": "week2-date-server",
  "returned_text": "2026-09-08",
  "isError": false
}
```

