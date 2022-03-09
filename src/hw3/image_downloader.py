import re
import asyncio
from aiohttp import ClientSession
from aiofile import async_open
from bs4 import BeautifulSoup


async def get_link():
    async with ClientSession() as session:
        url = "https://www.thisfuckeduphomerdoesnotexist.com/"
        async with session.get(url) as resp:
            html_doc = await resp.text()
            document = BeautifulSoup(html_doc, "html.parser")
            images = document.find_all("img")
            for image in images:
                if image.get("class") == ["image-payload"]:
                    return image.get("src")


async def get_image_by_link():
    image_link = await get_link()
    if type(image_link) != str:
        raise ValueError("Image link missed")

    image_key = re.search(r"(?<=images/).*(?=\.jpg)", image_link)[0]

    async with ClientSession() as session:
        async with session.get(image_link) as resp:
            with open(f"images/{image_key}.jpg", mode='wb') as fp:
                async with async_open(fp) as image:
                    await image.write(await resp.read())


def download_some_images(cli: int):
    if cli < 0:
        raise ValueError("Downloading images number must be non-negative")
    loop = asyncio.get_event_loop()
    group = asyncio.gather(*[loop.create_task(get_image_by_link()) for _ in range(cli)])
    loop.run_until_complete(group)
