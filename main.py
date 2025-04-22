import crawler
import asyncio

async def run_concurently(qurey: str):
    results = await asyncio.gather(crawler.crawl_G_search(qurey), crawler.crawl_trends(qurey))
    print("Event Loop Completed")
    return results

async def main(qurey: str)->int:
    # Make Event loop and run both Co-routines 
    try:
        page_count, list_data = await run_concurently(qurey)
    except Exception as e:
        print(f"Error running the browser Concurently: {e}")


    # Now calculate the Search Volume
    try:
        search_volume = (list_data[-1]/sum(list_data))*page_count
        print(len(list_data))
        return int(search_volume)
    except Exception as e:
        print(f"No data shown fetched : {e}")
        return int((1/256)*page_count)
    
        
    


if __name__=="__main__":
    qurey = input("Enter your Qurey: ")
    result = asyncio.run(main(qurey))
    
    print(f"\n\n{100*"-"}\nSearch Volume: {result}\n{100*"-"}")