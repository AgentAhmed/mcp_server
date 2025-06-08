from mcp.server.fastmcp import FastMCP
from datetime import datetime

def register(mcp: FastMCP):

    @mcp.resource("greeting://{name}")
    def get_greeting(name: str) -> str:
        return f"Hello, {name}!"

    @mcp.resource("smartgreet://{name}")
    def smart_greeting(name: str) -> str:
        hour = datetime.now().hour
        if hour < 12:
            return f"Good morning, {name}!"
        elif hour < 18:
            return f"Good afternoon, {name}!"
        else:
            return f"Good evening, {name}!"

    @mcp.tool()
    def get_day_from_date(date_str: str) -> str:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%A")