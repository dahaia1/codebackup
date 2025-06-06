import requests
import os
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import time


def download_file(url, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.content
        except Exception as e:
            print(f'下载失败第{attempt+1}次: {str(e)}')
            time.sleep(2)
    return None


def parse_images(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    
    image_urls = set()
    for img in img_tags:
        src = img.get('src') or img.get('data-src')
        if src:
            full_url = urljoin(base_url, src)
            if urlparse(full_url).scheme in ('http', 'https'):
                image_urls.add(full_url)
    return list(image_urls)


def download_image(img_url, save_path):
    try:
        content = download_file(img_url)
        if content:
            # 去除URL参数保持原始文件名
            clean_path = urlparse(img_url).path.split('?')[0]
            filename = os.path.join(save_path, os.path.basename(clean_path))
            with open(filename, 'wb') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f'图片下载失败: {str(e)}')
    return False


def main():
    base_url = 'https://cdn.hlxy.db9x.com/hlxy_20220117/assets/resource/map/5014/'
    save_dir = Path('images/5014')
    save_dir.mkdir(exist_ok=True, parents=True)

    # 生成1-290的图片URL列表
    image_urls = [f'{base_url}{i}.jpg?ver=1.0.2' for i in range(1, 500)]
    print(f'找到 {len(image_urls)} 张图片')

    print('开始多线程下载...')
    success = 0
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(lambda url: download_image(url, save_dir), image_urls)
        success = sum(results)

    print(f'\n下载完成！成功下载 {success}/{len(image_urls)} 张图片')


if __name__ == '__main__':
    main()
