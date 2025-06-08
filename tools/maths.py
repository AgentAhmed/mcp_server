from mcp.server.fastmcp import FastMCP

def register(mcp: FastMCP):

    @mcp.tool()
    def add(a: int, b: int) -> int:
        return a + b

    @mcp.tool()
    def multiply(a: int, b: int) -> int:
        return a * b

    @mcp.tool()
    def power(base: int, exponent: int) -> int:
        return base ** exponent

    @mcp.tool()
    def fibonacci(n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a