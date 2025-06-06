import pandas as pd

# 设置中文字体对齐显示
pd.set_option('display.unicode.east_asian_width', True)

# 初始化体检数据
data = [
    [175, 70, 5.0, 120],
    [168, 65, 4.8, 115],
    [180, 80, 4.5, 130],
    [172, 68, 4.9, 125]
]
names = ['张三', '李四', '王五', '赵六']
columns = ['身高(cm)', '体重(kg)', '视力', '血压(mmHg)']

df = pd.DataFrame(data=data, index=names, columns=columns)
print("初始体检表：")
print(df)

# 添加何七行数据
df.loc['何七'] = [169, 72, 4.7, 118]
print("\n添加何七后：")
print(df)

# 添加血型列
df['血型'] = ['A', 'B', 'O', 'AB', 'A']
print("\n添加血型列后：")
print(df)

# 删除张三行
df.drop(index='张三', inplace=True)
print("\n删除张三后：")
print(df)

# 删除血压列
df.drop(columns='血压(mmHg)', inplace=True)
print("\n删除血压列后：")
print(df)