# server.py
from fastmcp import FastMCP
import sys
import logging

logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True
)
logger = logging.getLogger('Calculator')

# Fix UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stderr.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

import math
import random

# Create an MCP server
mcp = FastMCP("Calculator")

# Add calculation tool
@mcp.tool()
def calculator(python_expression: str) -> dict:
    """For mathematical calculation, always use this tool to calculate the result of a python expression. You can use 'math' or 'random' directly, without 'import'."""
    try:
        allowed_globals = {
            "math": math,
            "random": random,
            "__builtins__": {
                "abs": abs,
                "round": round,
                "min": min,
                "max": max,
                "sum": sum,
                "pow": pow,
                "len": len,
                "int": int,
                "float": float,
                "str": str,
                "bool": bool,
                "list": list,
                "dict": dict,
                "set": set,
                "tuple": tuple,
                "range": range,
            },
        }
        result = eval(python_expression, allowed_globals)
        logger.info(f"Calculating formula: {python_expression}, result: {result}")
        return {"success": True, "result": result}
    except Exception as e:
        logger.error(f"Error calculating formula: {python_expression}, error: {e}")
        return {"success": False, "error": str(e)}

# Start the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
