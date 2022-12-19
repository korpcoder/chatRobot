import insuranceqa_data as insuranceqa

# 使用时需要安装 `insuranceqa_data`
# 如果下载不下来，可以手动下载数据集，存储到本地， 不含corpus目录解压到`insuranceqa_data`包的文件夹下
# 链接: https://pan.baidu.com/s/1GTML6qJuqpK_gT4-ShQPKw 提取码: q3u3

test_data_path = './data/corpus_test_data.txt'
valid_data_path = './data/corpus_valid_data.txt'
train_data_path = './data/corpus_train_data.txt'
vocab_data = insuranceqa.load_pairs_vocab()

def get_real_words(id_array):

    sentence = ''
    for word_id in id_array:
        sentence += vocab_data['id2word'][str(word_id)]
    return sentence


if __name__ == '__main__':
    train_data = insuranceqa.load_pairs_train()
    test_data = insuranceqa.load_pairs_test()
    valid_data = insuranceqa.load_pairs_valid()
    vocab_data = insuranceqa.load_pairs_vocab()
    # test data
    with open(test_data_path, 'a', encoding='utf-8') as f:
        for x in test_data:
            if x['label'][0] == 1:
                question = get_real_words(x['question'])
                utterance = get_real_words(x['utterance'])
                f.write(question + '\n')
                f.write(utterance + '\n')
                f.write('\n')

    # train data
    with open(train_data_path, 'a', encoding='utf-8') as f:
        for x in train_data:
            if x['label'][0] == 1:
                question = get_real_words(x['question'])
                utterance = get_real_words(x['utterance'])
                f.write(question + '\n')
                f.write(utterance + '\n')
                f.write('\n')
    # valid data
    with open(valid_data_path, 'a', encoding='utf-8') as f:
        for x in valid_data:
            if x['label'][0] == 1:
                question = get_real_words(x['question'])
                utterance = get_real_words(x['utterance'])
                f.write(question + '\n')
                f.write(utterance + '\n')
                f.write('\n')
