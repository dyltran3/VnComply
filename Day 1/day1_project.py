"""
MINI PROJECT: Async URL Checker

Tạo tool kiểm tra xem nhiều URLs có hoạt động không

Requirements:
1. Check 10 URLs đồng thời
2. In status code của mỗi URL
3. Tính tổng thời gian
4. Handle errors (URL không tồn tại, timeout)
"""

import asyncio
import aiohttp  # Cần install: pip install aiohttp
import time

# Danh sách URLs cần check
URLS = [
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com",
    "https://python.org",
    "https://fastapi.tiangolo.com",
    "https://this-url-does-not-exist-12345.com",  # URL lỗi
    "https://playwright.dev",
    "https://docker.com",
    "https://postgresql.org",
    "https://redis.io",
]

async def check_url(session, url: str):

    """
    TODO: Kiểm tra 1 URL
    
    Args:
        session: aiohttp.ClientSession
        url: URL cần check
    
    Returns:
        Dict với 'url', 'status', 'response_time'
    
    Hints:
    - Dùng session.get(url, timeout=5)
    - Bắt exceptions (timeout, invalid URL)
    - Tính thời gian response
    """
    # YOUR CODE HERE
    start =time.time()
    try:
        # (1) mở request bất đồng bộ tới url, timeout 5s
        async with session.get(url,timeout=5) as response:
            # (2) lấy status code từ response
            status=response.status
            # (3) tính thời gian phản hồi
            response_time = time.time() - start
               # (4) trả về kết quả THÀNH CÔNG
            return {
                "url": url,
                "status": status,
                "response_time": response_time,
                "error": None
            }
    except Exception as e:
        # (5) tính thời gian phản hồi khi lỗi
        response_time = time.time() - start
         # (6) trả về kết quả LỖI (không raise)
        return {
            "url": url,
            "status": None,
            "response_time": response_time,
            "error": str(e)
        }
    pass


async def check_all_urls():
    """
    TODO: Check tất cả URLs đồng thời
    
    Hints:
    - Tạo aiohttp.ClientSession
    - Dùng asyncio.gather để check tất cả URLs
    - In kết quả đẹp
    """
    print("🔍 Bắt đầu kiểm tra URLs...\n")
    start = time.time()
    
    # YOUR CODE HERE
    
    #  Tạo ClientSession
    async with aiohttp.ClientSession() as session:
         # Tạo list coroutine
         tasks = [check_url(session, url) for url in URLS]
        # Chạy đồng thời
         results= await asyncio.gather(*tasks)
          # In kết quả
    for result in results:
            if result["error"] is None:
                print(f"{result['url']} Status: {result['status']} | Time : {result['response_time']:.2f}s")
            else:
                print(f"{result['url']} | Error: {result['error']} | Time : {result['response_time']:.2f}s")
    end = time.time()
    print(f"\n⏱️  Tổng thời gian: {end - start:.2f}s")

# Run
if __name__ == "__main__":
    asyncio.run(check_all_urls())