import requests
from tqdm import tqdm

def download_video(url: str, filename: str):
    headers = {
        'Host': 'lms-datamites.s3.ap-southeast-1.amazonaws.com',
        'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'Accept-Encoding': 'gzip, deflate',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'video',
        'Referer': 'https://learn.datamites.com/',
        'Accept-Language': 'en-US,en;q=0.9',
        'Range': 'bytes=0-',
        'Connection': 'close'
    }

    try:
        with requests.get(url, headers=headers, stream=True) as response:
            response.raise_for_status()

            # Get total file size from headers if available
            total_size = int(response.headers.get('content-length', 0))
            chunk_size = 1024 * 1024  # 1 MB

            # Setup tqdm progress bar
            progress_bar = tqdm(
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
                desc=f"Downloading {filename}",
                ncols=80,
                colour="cyan"
            )
            if filename.endswith('.mp4'):
                pass
            else:
                filename += '.mp4'
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        progress_bar.update(len(chunk))
            progress_bar.close()

            if total_size != 0 and progress_bar.n != total_size:
                print("\n⚠️ WARNING: Downloaded size mismatch! File may be corrupted.")

            print(f"\n✅ Download completed. File saved as: {filename}")

    except Exception as e:
        print(f"❌ Download failed for {filename}: {e}")