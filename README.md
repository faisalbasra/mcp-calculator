# MCP Calculator Server | MCP 计算器服务

A Model Context Protocol (MCP) server providing mathematical calculation tools for AI assistants, deployable to **Prefect Horizon** as a hosted MCP app, or runnable locally and with Xiaozhi (ESP32) / Claude Desktop / Cursor.

---

## 🚀 Quick Start (Local Development)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Inspect the Server
```bash
fastmcp inspect fastmcp.json
```
or:
```bash
fastmcp inspect calculator.py:mcp
```

### 3. Run Locally with FastMCP
```bash
# Run server
fastmcp run fastmcp.json

# Or run interactive development mode / web inspector
fastmcp dev calculator.py
```

### 4. Test a Tool Call
```bash
fastmcp call calculator.py calculator python_expression="math.sqrt(144) + 10"
```

---

## 🌐 Deploy to Prefect Horizon (`horizon.prefect.io`)

[Prefect Horizon](https://horizon.prefect.io) provides zero-config, autoscaling managed hosting with OAuth 2.1 for FastMCP servers.

### Step 1: Push to GitHub
Ensure your repository is pushed to GitHub:
```bash
git add .
git commit -m "Configure FastMCP server for Prefect Horizon deployment"
git push -u origin main
```
Your repo: `https://github.com/faisalbasra/mcp-calculator`

### Step 2: Connect to Prefect Horizon
1. Log in to [horizon.prefect.io](https://horizon.prefect.io) with your GitHub account.
2. Click **Create Project** / **Add Server**.
3. Select your repository: `faisalbasra/mcp-calculator`.

### Step 3: Configure Entrypoint & Environment
- **Source / Entrypoint:** `calculator.py:mcp` (or FastMCP will automatically detect `fastmcp.json`)
- **Python Version:** `3.10+` (FastMCP 3.x)
- **Dependencies:** Picked up automatically from `requirements.txt` or `fastmcp.json`.

### Step 4: Deploy & Connect
- Horizon will automatically build, containerize, and deploy your server.
- You will receive a hosted endpoint URL (e.g., `https://<your-app>.horizon.prefect.io/mcp` or SSE endpoint).
- Connect this URL directly to Claude Desktop, Cursor, ChatGPT, or your AI client.

---

## 🔌 Connecting to Xiaozhi (ESP32) via `mcp_pipe.py`

If you are using this server with the Xiaozhi AI assistant:

1. Set your WebSocket endpoint:
```bash
export MCP_ENDPOINT=<your_xiaozhi_mcp_endpoint>
```

2. Start the communication pipe:
```bash
python mcp_pipe.py calculator.py
# Or run all enabled servers from mcp_config.json:
python mcp_pipe.py
```

---

## 📁 Project Structure

- `calculator.py`: FastMCP calculator server implementation.
- `fastmcp.json`: Canonical FastMCP configuration manifest for local tooling and Prefect Horizon.
- `mcp_config.json`: Multi-server config for `mcp_pipe.py` (stdio / sse / http).
- `mcp_pipe.py`: WebSocket pipe bridge for Xiaozhi / remote agents.
- `requirements.txt`: Python package dependencies.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
