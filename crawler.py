import asyncio
from playwright.async_api import async_playwright
from markdownify import markdownify as md
from fake_useragent import UserAgent
from crawl4ai import AsyncWebCrawler


def create_user_agent():
    try:
        ua = UserAgent(platforms='desktop')
        random_ua = ua.random
        return random_ua
    
    except Exception as e:
        print(f"Error Generating User Agent: {e}")
        return ""

def extract_data_from_markdown(text: str)->list:
    try:
        data = text.split('|')[6:-1][2::3]
        int_data = [int(num.strip()) for num in data]
        return int_data

    except Exception as e:
        print(f"Error extrating data from markdown: {e}")
        return []

async def crawl_trends(search_query: str)->list:
    #Launch Playwright
    async with async_playwright() as p:
        # Launch Browser (Google Chrome)
        browser = await p.chromium.launch(headless=False, channel="chrome")

        # Try running the script
        try: 
            # Create a new incognito session
            ua = create_user_agent()
            session = await browser.new_context(ignore_https_errors=True, user_agent=ua, java_script_enabled=True)

            # Start a new tab
            tab = await session.new_page()

            # Go to Trends Home Page 
            await tab.goto("https://trends.google.co.in")
            await tab.wait_for_load_state("networkidle")

            # Now go to Explore Page of trends and extract data
            url = f"https://trends.google.co.in/trends/explore?date=all&geo=IN&q={search_query.replace(' ', '%20')}&hl=en-IN"

            await tab.goto(url)
            await tab.wait_for_selector(".widget-container-wrapper", timeout=1000000)
            await tab.wait_for_load_state("networkidle")
            await tab.wait_for_timeout(1000)


            page_html = await tab.content()
            markdown = md(page_html)
            data = extract_data_from_markdown(markdown)

            return data

        except Exception as e:
            print(f"Error trying to crawl Google Trends: {e}")
            return None

        finally:
            await browser.close()

async def crawl_G_search(query: str)->int:
    # Using Crawl4AI instead of Playwright

    # Try Crawling Google Search
    try:
        query = query.replace(" ", "%20")
        url = r"https://www.google.com/search?q=" + query

        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url)
    except Exception as e:
        print(f"Error Crawling G-Search using Crawl4AI: {e}")
        return 0

    # Extract total pages form raw html
    try:
        markdown = result.markdown
        start = "About"
        end = "results"
        start_index = markdown.find(start)
        end_index = markdown.find(end)

        return int(markdown[start_index+5:end_index].strip().replace(',', ''))
    except Exception as e:
        print(f"Error extracting pages from html G-Search: {e}")
        return 0
    





