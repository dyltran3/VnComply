import asyncio
import time

async def download_file(file_name: str, size_mb: int):
    """
    Giả lập download file
    
    Arguments:
        file_name
        size_mb: Kích thước mỗi mb sẽ mất 0.5s
        
    """
    download_time = size_mb * 0.5
    
    print(f"Bắt đầu tải {file_name} ({size_mb}MB)...")
    await asyncio.sleep(download_time)
    print(f"Tải xong {file_name}!")
    
    return f"{file_name} ({size_mb}MB)"

async def download_all_files():
    """
    Tải 3 file tuần tự
    
    Files:
    - video.mp4 (10MB)
    - music.mp3 (5MB)
    - document.pdf (2MB)
    
    Tính thời gian tải tổng cộng
    """
    print("Bắt đầu tải tất cả file...")
    start_time = time.time()
    
    #Your code here

    task1 = await download_file("video.mp4", 1)
    task2 = await download_file("soundclound.mp3", 5) 
    task3 = await download_file("document.pdf", 2)
    
    end_time = time.time()
    print(f"Tải tất cả file xong trong {end_time - start_time:.1f} giây.")
    
async def download_all_async():
    """
    Tải 3 file đồng thời (nhanh)

    Hint: Dùng asyncio.create_task() và await
    """
    
    print("Bắt đầu tải tất cả file (bất đồng bộ)...")
    start_time = time.time()
    
    #Your code here
    
    end_time = time.time()
    print(f"Tải tất cả file xong trong {end_time - start_time:.1f} giây.\n")
    
#Test
async def main():
    await download_all_files()
    await download_all_async()
    
asyncio.run(main())