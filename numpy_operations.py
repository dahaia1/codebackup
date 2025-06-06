import numpy as np

# 第一部分：一维数组数学运算
data = np.array([1.5, 3.44, -3.1])

# 1.向上取整
ceil_result = np.ceil(data)
print('向上取整结果：', ceil_result)

# 2.向下取整
floor_result = np.floor(data)
print('\n向下取整结果：', floor_result)

# 3.取倒数（自动处理0值异常）
reciprocal_result = np.reciprocal(data)
print('\n倒数计算结果：', reciprocal_result)

# 第二部分：二维数组运算
# 创建4x4二维数组
arr_2d = np.array([[i*4+j for j in range(4)] for i in range(4)])
# 创建4元素一维数组
arr_1d = np.array([10, 20, 30, 40])

print('\n二维数组：\n', arr_2d)
print('\n一维数组：', arr_1d)

# 广播机制运算演示
print('\n数组相加：\n', arr_2d + arr_1d)
print('\n数组相减：\n', arr_2d - arr_1d)
print('\n数组相乘：\n', arr_2d * arr_1d)
print('\n数组相除（浮点结果）：\n', arr_2d / arr_1d)