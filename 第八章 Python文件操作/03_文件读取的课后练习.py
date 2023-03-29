with open("C:/Users/xxpg/Desktop/word.txt", 'r', encoding="UTF-8") as f:
    f = f.read()
print(f"每行数据:{f}")
num = None
for itheima in f:
    if itheima == "itheima":
        num += 1
print(num)

