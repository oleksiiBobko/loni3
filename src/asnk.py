import asyncio
import time
import aiohttp

headers={"Content-Type":"text",
        "x-ts-uuid": "PATSFCP-REALTIME",
        "x-ts-applicationid": "localTest",
        "x-ts-requestid": "localTest_66fc1c92-8f7f-4265-a7b7-44cb8df77181",
        "x-ts-productid": "historical pricing"}


async def download_site(session, url):
    async with session.get(url = url, headers = headers, ssl = False) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    
    my_file = open("mrsp_events_rics.txt", 'r')
    rics = my_file.readlines()
    rics = [ric.rstrip() for ric in rics]

    sites = []

    for r in rics:
        url = "http://localhost"
        sites.append(url)

    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
