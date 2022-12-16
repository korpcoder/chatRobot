import os

import openpyxl

baike_path = r"保险百科-表格.xlsx"
ketang_path = r"保险小课堂-表格.xlsx"
train_txt_path = r"../data/train1.txt"


def read_excel(path):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    mr = sheet.max_row
    with open(train_txt_path, 'a', encoding='utf-8') as f:
        for i in range(2, mr):
            # 参考preprocess里面添加隔断
            question = sheet.cell(i, 2).value.strip() + '\r\n'
            answer = sheet.cell(i, 3).value.strip() + '\r\n'
            f.write(question)
            f.write(answer)
            f.write('\r\n\r\n')
    pass


if __name__ == '__main__':
    if os.path.exists(train_txt_path):
        os.remove(train_txt_path)
    read_excel(baike_path)
    read_excel(ketang_path)
    pass
