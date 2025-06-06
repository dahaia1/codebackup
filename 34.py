import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置参数
BASE_URL = "https://cdn.hlxy.db9x.com/hlxy_20220117/assets/resource/map/{dir_num}/{img_num}.jpg?ver=1.0.2"
DIR_RANGE = (1, 1000)     # 目录范围
IMG_RANGE = (1, 1000)     # 图片范围
THREADS = 20             # 并发线程数
RETRY_MAX = 2            # 单文件重试次数
DELAY = 0.1              # 基础请求间隔
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def download_directory(dir_num):
    """下载单个目录的所有图片"""
    dir_path = os.path.join('map', str(dir_num))
    os.makedirs(dir_path, exist_ok=True)
    
    # 首图检测
    first_img = BASE_URL.format(dir_num=dir_num, img_num=1)
    try:
        if requests.head(first_img, headers=HEADERS, timeout=5).status_code != 200:
            return f"🚫 目录 {dir_num:03d} 首图缺失"
    except Exception as e:
        return f"⏩ 目录 {dir_num:03d} 连接失败 ({str(e)})"
    
    # 顺序下载图片
    error_count = 0
    for img_num in range(IMG_RANGE[0], IMG_RANGE[1] + 1):
        img_url = BASE_URL.format(dir_num=dir_num, img_num=img_num)
        file_path = os.path.join(dir_path, f"{img_num}.jpg")
        
        if os.path.exists(file_path):
            continue
        
        for attempt in range(RETRY_MAX + 1):
            try:
                response = requests.get(img_url, headers=HEADERS, stream=True, timeout=10)
                if response.status_code == 404:
                    return f"⏹ 目录 {dir_num:03d} 终止于 {img_num}"
                if response.ok:
                    with open(file_path, 'wb') as f:
                        for chunk in response.iter_content(8192):
                            f.write(chunk)
                    break
                else:
                    error_count += 1
            except Exception as e:
                if attempt == RETRY_MAX:
                    error_count += 1
                time.sleep(1)
            finally:
                time.sleep(DELAY)
        
        if error_count >= 3:
            return f"⏹ 目录 {dir_num:03d} 错误过多"
    
    return f"✅ 目录 {dir_num:03d} 下载完成"

def main():
    start_time = time.time()
    total_dirs = DIR_RANGE[1] - DIR_RANGE[0] + 1
    completed = 0
    os.makedirs('map', exist_ok=True)
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = {executor.submit(download_directory, dir_num): dir_num 
                  for dir_num in range(DIR_RANGE[0], DIR_RANGE[1] + 1)}
        
        for future in as_completed(futures):
            dir_num = futures[future]
            try:
                result = future.result()
            except Exception as e:
                result = f"❌ 目录 {dir_num:03d} 异常: {str(e)}"
            
            # 进度统计
            completed += 1
            elapsed = time.time() - start_time
            progress_percent = (completed / total_dirs) * 100
            remaining = (elapsed / completed) * (total_dirs - completed) if completed > 0 else 0
            
            # 实时进度输出
            print(f"{result.ljust(35)} | 进度: {completed}/{total_dirs} ({progress_percent:.1f}%) | 已用: {elapsed:.0f}s | 剩余: {remaining:.0f}s")

    # 最终统计
    total_time = time.time() - start_time
    print(f"\n所有任务完成！总耗时: {total_time//3600:.0f}h {total_time%3600//60:.0f}m {total_time%60:.0f}s")

if __name__ == "__main__":
    main()
