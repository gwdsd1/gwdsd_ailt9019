"""Probe the local date MCP server and print the real tool output."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def send(stream, payload: dict) -> None:
    data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    stream.write(f"Content-Length: {len(data)}\r\n\r\n".encode("ascii") + data)
    stream.flush()


def receive(stream) -> dict:
    headers = {}
    while True:
        line = stream.readline()
        if line in (b"\r\n", b"\n"):
            break
        key, _, value = line.decode("ascii").partition(":")
        headers[key.lower()] = value.strip()
    length = int(headers["content-length"])
    return json.loads(stream.read(length).decode("utf-8"))


def main() -> None:
    server = Path(__file__).with_name("date_server.py")
    process = subprocess.Popen(
        [sys.executable, str(server)], stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    assert process.stdin is not None and process.stdout is not None
    send(process.stdin, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
    initialize = receive(process.stdout)
    send(process.stdin, {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})
    send(process.stdin, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    tools = receive(process.stdout)
    send(
        process.stdin,
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {"name": "current_date", "arguments": {}},
        },
    )
    result = receive(process.stdout)
    process.terminate()
    print(json.dumps({"initialize": initialize, "tools": tools, "call": result}, indent=2))


if __name__ == "__main__":
    main()

