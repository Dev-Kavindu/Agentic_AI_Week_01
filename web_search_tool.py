from ddgs import DDGS
from agents import function_tool

class FreeWebSearch:
    """
    ඕනෑම project එකක පාවිච්චි කළ හැකි Free Web Search Class එක.
    """
    def __init__(self, max_results: int = 5, region: str = "wt-wt"):
        self.max_results = max_results
        self.region = region  # 'wt-wt' කියන්නේ Worldwide

    def search(self, query: str) -> str:
        """සාමාන්‍ය Python code එකකින් කෙලින්ම search කරන්න."""
        try:
            with DDGS(timeout=15) as ddgs:
                results = list(ddgs.text(
                    query,
                    region=self.region,
                    max_results=self.max_results
                ))
            if not results:
                return "No results found."

            formatted = []
            for i, r in enumerate(results, 1):
                formatted.append(
                    f"[{i}] Title: {r.get('title', 'N/A')}\n"
                    f"Snippet: {r.get('body', '')}\n"
                    f"URL: {r.get('href', '')}\n"
                )
            return "\n---\n".join(formatted)
        except Exception as e:
            return f"Search failed: {e}"

    def as_agent_tool(self):
        """OpenAI Agents SDK එකට ගැලපෙන @function_tool එකක් විදිහට return කරන්න."""
        @function_tool
        def web_search(query: str) -> str:
            """Search the web for up-to-date information on a given query."""
            return self.search(query)

        return web_search