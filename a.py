import datetime

# 1. 打开文件 a.txt 并写入班级、学号和姓名
with open('a.txt', 'w', encoding='utf-8') as file:
    class_info = '班级：示例班级'
    student_id = '学号：20250001'
    name = '姓名：张三'
    file.write(class_info + '\n')
    file.write(student_id + '\n')
    file.write(name + '\n')

# 2. 读取文件的字符数量
with open('a.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    char_count = len(content)
    print(f"文件中的字符数量: {char_count}")

# 3. 读取当前日期时间并追加到文件 a.txt 中
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('a.txt', 'a', encoding='utf-8') as file:
    file.write(f"当前日期时间: {current_datetime}\n")

# 4. 读取并显示文件 a.txt 中的所有内容
with open('a.txt', 'r', encoding='utf-8') as file:
    all_content = file.read()
    print("文件中的所有内容:")
    print(all_content)

# 5. 由于使用了 with 语句，文件会自动关闭，无需手动关闭
