### Using `edge-ai` MCP server with Claude Desktop
1. Install `mcp-proxy` for Claude: `npx -y @smithery/cli install mcp-proxy --client claude`
1. Open `claude_desktop_config.json` in the Claude subdirectory
1. Add the following MCP descriptor for `edge-ai` running locally on your computer.
   ```
   "edge-ai": {
      "command": "{path-to-mcp}/.local/bin/mcp-proxy",
      "args": ["http://localhost:8005/mcp"]
    }
    ```
1. Got to the `edge-ai` directory and run `uv run fastapi dev src/edge_ai/main.py --port 8005`
1. Open Claude Desktop