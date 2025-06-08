from mcp.server.fastmcp import FastMCP

def register(mcp: FastMCP):

    @mcp.tool()
    def word_count(text: str) -> int:
        return len(text.split())

    @mcp.tool()
    def is_palindrome(word: str) -> bool:
        return word.lower() == word[::-1].lower()
