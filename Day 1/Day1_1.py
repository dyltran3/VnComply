import asyncio

#TODO Viết hàm async đầu tiên
async def say_hello(name: str,delay:int):
    """
    In ra lời chào sau khi đợi {delay} giây
    
    Arguments:
    name : str : Tên người nhận lời chào
    delay : int : Thời gian chờ trước khi in lời chào
    
    
    Example:
        await say_hello("Tuan Anh", 3)
        
    """
    #Your code here
    # Hint: Sử dụng await asyncio.sleep(delay) 
    #duckien
async def say_hello(name, delay):
    print(f"\nHello {name}")
    await asyncio.sleep(delay)
    print(f"\nReady for {name} after {delay} second!")
    
#Test Function
async def test_say_hello():
    print("Bắt đầu test...")
    await say_hello("Tuan Anh", 3)
    await say_hello("Nguyen Van A", 1)
    print("Kết thúc test.")
    
#Chạy hàm test
asyncio.run(test_say_hello())