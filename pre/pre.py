import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('table_data.csv')

# 保留换行符之前的数据
df['场均KDA'] = df['场均KDA'].apply(lambda x: x.split('\n')[0].strip())

# 将处理后的数据写回 CSV 文件
df.to_csv('output_file.csv', index=False, encoding='utf-8')

print('Data has been processed and saved to output_file.csv')
