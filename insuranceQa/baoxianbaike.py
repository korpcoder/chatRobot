import csv

# 打开 CSV 文件
with open('baoxianzhidao_filter.csv', 'r',encoding='utf-8') as f:
  with open('baoxianzhidao_filter.txt', 'w', encoding='utf-8') as f2:
    # 创建 CSV 阅读器
    reader = csv.reader(f)
    # 读取 CSV 文件中的每一行
    for row in reader:
      # 第三列为 1 的数据
      if row[3] == '1':
        print(row)
        f2.write(row[0].strip() + '\n')
        f2.write(row[2].strip() + '\n')
        f2.write('\n')