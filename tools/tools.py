"""
tools 폴더: 에이전트가 사용할 모든 도구 목록 
"""

#검색 api
import os
from langchain_community.tools.tavily_search import TavilySearchResults

TAVILY_API_KEY=os.environ["TAVILY_API_KEY"]  # 올바른 API 키 입력


def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]
