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
    star_time = time.time()
    try:
        async with session.get(url, timeout=5) as e:
            status = e.status
            end_time = time.time()
            e_time = end_time - star_time
            return {
                'url': url,
                'status': status,
                'response_time': e_time
            }
    except asyncio.TimeoutError:
        end_time = time.time()
        e_time = end_time - star_time
        status = 'Timeout'
        return {
                'url': url,
                'status': status,
                'response_time': e_time
            }
    except aiohttp.ClientError:
        end_time = time.time()
        e_time = end_time - star_time
        status = 'Client Error'
        return {
                'url': url,
                'status': status,
                'response_time': e_time
            }
    except Exception as e:
        return {
                'url': url,
                'status': status,
                'response_time': e_time
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
    async with aiohttp.ClientSession() as session:
        tasks = [check_url(session, url) for url in URLS]
        results = await asyncio.gather(*tasks)
        for result in results:  
            print(f"URL: {result['url']}")
            print(f"Status: {result['status']}")
            print(f"Response Time: {result['response_time']:.2f}s")
            print("-----")
    end = time.time()
    print(f"\n⏱️  Tổng thời gian: {end - start:.2f}s")
# Run
if __name__ == "__main__":
    asyncio.run(check_all_urls())