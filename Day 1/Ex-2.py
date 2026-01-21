"""
Tạo async function chỉ cho phép chạy tối đa 3 tasks đồng thời

Example:
- Có 10 URLs cần fetch
- Nhưng chỉ fetch 3 URLs cùng lúc
- Khi 1 URL xong, fetch URL tiếp theo
"""

import asyncio

async def rate_limited_fetch(urls: list, max_concurrent: int = 3):
    # YOUR CODE HERE
    # Hint: Dùng asyncio.Semaphore
    pass