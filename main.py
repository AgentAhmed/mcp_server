# main.py
from mcp.server.fastmcp import FastMCP

# Create shared MCP instance
mcp = FastMCP("SmartToolbox")

# Import register functions from tools
from tools.maths import register as register_maths
from tools.text import register as register_text
from tools.time import register as register_time

# Register tools
register_maths(mcp)
register_text(mcp)
register_time(mcp)

if __name__ == "__main__":
    mcp.run()
