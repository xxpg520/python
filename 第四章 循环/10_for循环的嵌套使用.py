"""
演示嵌套应用for循环
"""

# 坚持表白100天，每天都送10朵花
i = None
for i in range(1, 101):
    print(f"今天是地{i}天，准备表白。")
    for j in range(1, 11):
        print(f"送出第{j}朵玫瑰。")
    print(f"小美我喜欢你，第{i}天表白完成。")

print(f"表白{i}天，表白成功")
