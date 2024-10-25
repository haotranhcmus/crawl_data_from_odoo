import re
path = input("Nhap url: ")
if 'slide/' in path:
    path = path.split('slide/')[1]  # Giữ lại phần sau 'slide/'

# Bước 2: Loại bỏ 4 số cuối cùng và phần sau đó
path = re.sub(r'-\d{4}.*', '', path)

# Bước 3: Thay dấu '-' bằng dấu cách
path = path.replace('-', ' ')

# Bước 4: Viết hoa toàn bộ chữ cái
path = path.upper()

with open("quiz_text.txt", "r", encoding="utf-8") as file:
    # Biến lưu trữ các câu hỏi đã lọc
    question = path + "\n"
    answer = ""
    test = 0
    checkfirst = 0
    # Đọc từng dòng trong file
    for line in file:
        if test == 1:   
            if re.match(r"^\d+\s*$", line) or line == "\n":
                continue
            question += line
            answer += "\n"
            test = 2
        elif(test >= 2 and line != "\n"):
            answer += line
            test += 1
        else:
            test = 0
        if re.match(r"^\d+\s*$", line):
            test = 1

# Ghi các câu hỏi đã lọc vào file list_question.txt
with open("list_question.txt", "w", encoding="utf-8") as file:
        file.write(question)
with open("answer.txt", "w", encoding="utf-8") as file:
        file.write(answer)

list = []
dapan = input("nhap dap an: ")
for i in dapan:
    if(i == 'a'):
        list.append(0)
    elif(i == 'b'):
        list.append(1)
    elif(i == 'c'):
        list.append(2)
    else:
        list.append(3)

num = 0
list_answer = ["\n"]
with open("answer.txt", "r", encoding="utf-8") as file:
    # Biến lưu trữ các câu hỏi đã lọc
    answer = "\n"
    index = -1
    for line in file:
        if(line == "\n"):
            num = 0
            index += 1
            continue
        if list[index] == num:
            answer += line
            list_answer.append(line)
        num += 1
with open("list_answer.txt", "w", encoding="utf-8") as file:
        file.write(answer)

import csv

# Đọc dữ liệu từ file list_question.txt
with open("list_question.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Tạo một file CSV để ghi kết quả
with open("data.csv", "a", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    # Biến lưu trữ tiêu đề của mỗi phần (dòng đầu tiên)
    title = None
    i = 0
    # Duyệt qua từng dòng và phân loại theo tiêu đề và nội dung
    for line in lines:
        line = line.strip()  # Xóa khoảng trắng ở đầu và cuối dòng
        text_answer = list_answer[i]
        i += 1
        # Nếu dòng không rỗng và title chưa được gán giá trị thì gán title
        if line and title is None:
            title = line
            writer.writerow([title])  # Ghi dòng đầu vào cột A
        elif line:
            # Nếu có nội dung và đã có tiêu đề, ghi vào cột B của dòng tiếp theo
            writer.writerow(["", line, text_answer])
        else:
            # Nếu gặp dòng trống, đặt lại title về None để xử lý phần tiếp theo
            title = None



import pandas as pd

# Đọc nội dung file list_question.txt
with open('list_question.txt', 'r', encoding='utf-8') as f:
    output_lines = [line.strip() for line in f if line.strip()]  # Bỏ qua dòng trống

# Đọc nội dung file list_answer.txt và bỏ qua dòng đầu tiên
with open('list_answer.txt', 'r', encoding='utf-8') as f:
    listanswer_lines = [line.strip() for line in f.readlines()[1:] if line.strip()]  # Bỏ qua dòng trống

# Lấy dòng đầu tiên của list_question.txt cho cột A, các dòng còn lại cho cột B
col_a = output_lines[0] if output_lines else ''
col_b = output_lines[1:]
col_c = listanswer_lines

# Xác định số dòng lớn nhất cần ghi vào bảng
max_rows = max(len(col_b), len(col_c))

# Độ dài tối đa của nội dung trong mỗi cột (ví dụ: 70 ký tự)
max_length = 65

# Hàm rút gọn nội dung quá dài
def truncate_text(text, max_len):
    return (text[:max_len - 3] + '...') if len(text) > max_len else text

# Mở file data.txt để ghi
with open('data.txt', 'a', encoding='utf-8') as f:    
    # Ghi dòng đầu tiên (chỉ có giá trị ở cột A)
    if col_a:
        f.write("|{:^65}|{:^65}|{:^65}|\n".format(truncate_text(col_a, max_length), '', ''))
    # Ghi các dòng tiếp theo, cột B và cột C
    for i in range(max_rows):
        b_value = col_b[i] if i < len(col_b) else ''
        c_value = col_c[i] if i < len(col_c) else ''
        
        # Rút gọn nội dung nếu vượt quá số ký tự quy định
        b_value = truncate_text(b_value, max_length)
        c_value = truncate_text(c_value, max_length)
        
        # Chỉ ghi dòng nếu cột B hoặc C có nội dung
        if b_value or c_value:
            f.write("|{:^65}|{:^65}|{:^65}|\n".format('', b_value, c_value))
