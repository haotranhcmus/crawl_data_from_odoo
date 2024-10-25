from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# Khởi tạo ChromeDriver
driver = webdriver.Chrome()  # Đảm bảo đường dẫn đến ChromeDriver đã được thêm vào PATH

# URL của trang quiz
url = input("Nhap url: ")
path = url
# Đường dẫn đầu vào

# Bước 1: Tìm vị trí của 'slide/' và cắt bỏ phần đầu đến đó
if 'slide/' in path:
    path = path.split('slide/')[1]  # Giữ lại phần sau 'slide/'

# Bước 2: Loại bỏ 4 số cuối cùng và phần sau đó
path = re.sub(r'-\d{4}.*', '', path)

# Bước 3: Thay dấu '-' bằng dấu cách
path = path.replace('-', ' ')

# Bước 4: Viết hoa toàn bộ chữ cái
path = path.upper()

driver.get(url)

# Chờ để trang tải xong nội dung quiz (tăng thời gian nếu trang tải chậm)
time.sleep(15)

# Tìm các phần tử chứa văn bản của câu hỏi và câu trả lời
# Bạn cần xác định các class hoặc tag cụ thể trong HTML của trang này.
questions = driver.find_elements(By.TAG_NAME, 'span')

success = 0
# Mở file để lưu toàn bộ văn bản
with open("quiz_text.txt", "w", encoding="utf-8") as file:
    # Ghi các câu hỏi vào file
    for i, question in enumerate(questions):
        if re.match(r"^\d+\s*$", question.text):
            success = 1
        file.write(f"{question.text}\n")

if success:
    print("Success!!!")
else:
    print("Failure!!!")
# Đóng trình duyệt
driver.quit()
