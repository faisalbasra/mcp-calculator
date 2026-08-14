# MCP Calculator Server | MCP 计算器服务

A Model Context Protocol (MCP) server providing mathematical calculation tools for AI assistants, deployable to **Prefect Horizon** as a hosted MCP app, and connectable to **Xiaozhi (小智 / ESP32 / M5Stack Core3)**, **Claude Desktop**, and **Cursor**.

---

## 🏗️ Architecture Overview

There are two primary ways to run and deploy this MCP server:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Hosted Cloud Server (Prefect Horizon)                    │
│                                                             │
│  [FastMCP / calculator.py] ──> Hosted on horizon.prefect.io │
│                                   ▲                         │
│                                   │ (HTTPS / SSE / OAuth)   │
│                      [Claude / Cursor / ChatGPT]            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 2. Xiaozhi AI Assistant Integration (WebSocket Tunnel)      │
│                                                             │
│  [calculator.py] <── (stdio) ──> [mcp_pipe.py]              │
│                                       │ (Outbound WSS)      │
│                                       ▼                     │
│                           [wss://api.xiaozhi.me/mcp]        │
│                                       │                     │
│                        [Xiaozhi Agent / M5Stack Core3]      │
└─────────────────────────────────────────────────────────────┘
```

---

## 🌐 1. Deploying to Prefect Horizon (`horizon.prefect.io`)

Prefect Horizon provides managed, auto-scaling hosting for FastMCP servers.

1. Push this repo to GitHub: `https://github.com/faisalbasra/mcp-calculator`.
2. Go to **[horizon.prefect.io](https://horizon.prefect.io)** and log in with GitHub.
3. Click **Add Server** / **Create Project** and select `faisalbasra/mcp-calculator`.
4. FastMCP will automatically use [`fastmcp.json`](fastmcp.json) with entrypoint `calculator.py:mcp`.
5. Deploy to receive your hosted MCP URL (e.g., `https://<app>.horizon.prefect.io/mcp` or `/sse`).

---

## 🤖 2. Connecting to Xiaozhi Console (`https://xiaozhi.me/console/agents`)

Xiaozhi uses a reverse WebSocket connection (`wss://api.xiaozhi.me/mcp/?token=...`) handled by `mcp_pipe.py`.

### Option A: Run Locally
1. Get your MCP Endpoint from [xiaozhi.me/console/agents](https://xiaozhi.me/console/agents) (Agent Settings -> MCP).
2. Set your environment variable:
   ```bash
   cp .env.example .env
   # Edit .env and set MCP_ENDPOINT=wss://api.xiaozhi.me/mcp/?token=YOUR_TOKEN
   ```
3. Run the pipe:
   ```bash
   python mcp_pipe.py calculator.py
   ```

### Option B: Run 24/7 in Cloud Container (Docker / VPS / Railway / Render)
To keep Xiaozhi connected 24/7 without keeping your computer awake:
```bash
# Build Docker container
docker build -t mcp-calculator .

# Run with your Xiaozhi token
docker run -d --name mcp-calculator \
  -e MCP_ENDPOINT="wss://api.xiaozhi.me/mcp/?token=YOUR_TOKEN" \
  --restart unless-stopped \
  mcp-calculator
```

### Option C: Bridge Xiaozhi to Your Horizon Deployed Server
If you deployed to Horizon and want Xiaozhi to route to the Horizon SSE URL:
1. In `mcp_config.json`, set:
   ```json
   {
     "mcpServers": {
       "horizon-calculator": {
         "type": "sse",
         "url": "https://<your-horizon-app>.horizon.prefect.io/sse"
       }
     }
   }
   ```
2. Run:
   ```bash
   python mcp_pipe.py
   ```

---

## 📁 Project Structure

- `calculator.py`: FastMCP calculator server implementation.
- `fastmcp.json`: Canonical FastMCP configuration manifest for Prefect Horizon.
- `mcp_pipe.py`: WebSocket pipe bridge for Xiaozhi AI.
- `mcp_config.json`: Multi-server routing configuration.
- `Dockerfile`: Container configuration for 24/7 cloud deployment.
- `requirements.txt`: Python package dependencies.

---

## 📄 License

MIT License
