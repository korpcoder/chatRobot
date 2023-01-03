# 读取训练数据集
import re

from tqdm import tqdm


def f_write(f, question, answer):
    f.write(question + '\n')
    f.write(answer + '\n')
    f.write('\n')


# 同义词组替换
def same_meaning_repalce(f, question, answer, words):
    exist_word = None
    for word in words:
        if word in question:
            exist_word = word
            break

    if exist_word:
        for word in words:
            # 如果该词不在问句中 则替换
            if not word in question:
                f_write(f, question.replace(exist_word, word), answer)


def re_replace():
    with open('all_train_data.txt', 'r', encoding='utf-8') as f:
        data = f.read()

    # 需要区分linux和windows环境下的换行符
    if "\r\n" in data:
        train_data = data.split("\r\n\r\n")
    else:
        train_data = data.split("\n\n")

    # 开始进行tokenize
    # 保存所有的对话数据,每条数据的格式为："[CLS]utterance1[SEP]utterance2[SEP]utterance3[SEP]"
    dialogue_len = []  # 记录所有对话tokenize之后的长度，用于统计中位数与均值
    dialogue_list = []
    with open('all_train_data_extend.txt', "w", encoding="utf-8") as f:
        for index, dialogue in enumerate(tqdm(train_data)):
            if "\r\n" in data:
                utterances = dialogue.split("\r\n")
            else:
                utterances = dialogue.split("\n")
            question = utterances[0].strip()
            answer = utterances[1].strip()
            f_write(f, question, answer)
            # 同义词替换
            same_meaning_repalce(f, question, answer, ['如何', '怎么', '怎样'])
            same_meaning_repalce(f, question, answer, ['的好处', '有哪些好处'])
            same_meaning_repalce(f, question, answer, ['为什么', '为何'])
            # 什么是（开头）  是什么（结尾）
            wi_question = question.rstrip('?').rstrip('？')
            if wi_question.startswith('什么是'):
                f_write(f, wi_question[3:] + '是什么', answer)
            elif wi_question.endswith('是什么'):
                f_write(f, '什么是' + wi_question[:-3], answer)


if __name__ == '__main__':
    re_replace()
    # print('1234'.replace('1','x'))
    # wi_question = '什么是速度'
    # if wi_question.startswith('什么是'):
    #     print( wi_question[3:] + '是什么')
    # elif wi_question.endswith('是什么'):
    #     print('什么是' + wi_question[:-3])
    pass
