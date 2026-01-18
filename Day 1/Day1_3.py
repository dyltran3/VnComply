import asyncio

async def fetch_user(user_id: int):
    """Giả lập lấy thông tin user từ database"""
    await asyncio.sleep(1)  # Giả lập query database
    return {
        'id': user_id,
        'name': f'User_{user_id}',
        'email': f'user{user_id}@example.com'
    }

async def fetch_multiple_users_v1():
    """
    Cách 1: Dùng create_task (dài dòng)
    """
    print("=== CÁCH 1: create_task ===")
    
    task1 = asyncio.create_task(fetch_user(1))
    task2 = asyncio.create_task(fetch_user(2))
    task3 = asyncio.create_task(fetch_user(3))
    
    user1 = await task1
    user2 = await task2
    user3 = await task3
    
    print(f"User 1: {user1}")
    print(f"User 2: {user2}")
    print(f"User 3: {user3}\n")

async def fetch_multiple_users_v2():
    """
    TODO: Cách 2: Dùng asyncio.gather (ngắn gọn)
    
    Hint: results = await asyncio.gather(
              fetch_user(1),
              fetch_user(2),
              fetch_user(3)
          )
    
    results sẽ là list: [user1, user2, user3]
    """
    print("=== CÁCH 2: gather ===")
    
    # YOUR CODE HERE
    results = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3)
    )
    user1, user2, user3 = results

    
    pass

# Test
async def main():
    import time
    
    start = time.time()
    await fetch_multiple_users_v1()
    end = time.time()
    print(f"⏱️  Thời gian cách 1: {end - start:.1f}s\n")
    
    start = time.time()
    await fetch_multiple_users_v2()
    end = time.time()
    print(f"⏱️  Thời gian cách 2: {end - start:.1f}s")

asyncio.run(main())