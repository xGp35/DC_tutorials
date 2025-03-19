import aiohttp
import asyncio
import os
from tqdm.asyncio import tqdm
from PIL import Image
from io import BytesIO

fill_n = 3

async def download_image(base_url, formatted_number, output_folder, progress_bar):
    url = base_url.format(formatted_number)
    file_name = f"{output_folder}/image_{formatted_number}.jpg"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                image_data = await response.read()
                
                # Convert WebP to JPG
                image = Image.open(BytesIO(image_data)).convert("RGB")
                image.save(file_name, "JPEG")
        
        progress_bar.update(1)  # Update the progress bar for a successful download
    except Exception as e:
        progress_bar.update(1)  # Update the progress bar even if a download fails
        print(f"Failed to download {url}: {e}")

async def download_images_async(base_url, start, end, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    total_images = end - start + 1

    # Create a progress bar
    with tqdm(total=total_images, desc="Downloading images", unit="file") as progress_bar:
        tasks = [
            download_image(base_url, str(i).zfill(fill_n), output_folder, progress_bar)
            for i in range(start, end + 1)
        ]
        await asyncio.gather(*tasks)

output_f = "webc"
base_url = "https://imagertq.com/image{}.webp"
asyncio.run(download_images_async(base_url, start=125, end=255, output_folder=output_f))
