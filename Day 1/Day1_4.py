import asyncio

async def risky_operation(task_id: int, will_fail: bool = False):
    """
    Giả lập operation có thể thất bại
    """
    await asyncio.sleep(1)
    
    if will_fail:
        raise ValueError(f"Task {task_id} failed!")
    
    return f"Task {task_id} succeeded"

async def run_with_individual_handling():
    """
    TODO: Chạy 3 tasks, handle lỗi cho TỪNG task
    
    Tasks:
    - Task 1: Thành công
    - Task 2: Thất bại
    - Task 3: Thành công
    
    Requirement: In kết quả của task thành công,
                 in lỗi của task thất bại
    """
    print("=== INDIVIDUAL ERROR HANDLING ===")
    
    # YOUR CODE HERE
    # Hint: Dùng try-except cho TỪNG await
    
    pass

async def run_with_gather_handling():
    """
    TODO: Chạy với gather, handle lỗi tập trung
    
    Hint: gather có parameter return_exceptions=True
    """
    print("\n=== GATHER ERROR HANDLING ===")
    
    # YOUR CODE HERE
    # Hint: results = await asyncio.gather(
    #           risky_operation(1, False),
    #           risky_operation(2, True),
    #           risky_operation(3, False),
    #           return_exceptions=True
    #       )
    # Hint: Kiểm tra từng result xem có phải Exception không
    
    pass

# Test
asyncio.run(run_with_individual_handling())
asyncio.run(run_with_gather_handling())