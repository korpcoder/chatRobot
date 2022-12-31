save_path = 'pa_qa.txt'

with open('train_crawl_qa.txt', 'r', encoding='utf-8') as f:
    contents = f.readlines()

with open(save_path, 'w', encoding='utf-8') as f:
    for line in contents:
        if len(line) > 1:
            sep_index = line.find('[sep]')
            question = line[:sep_index]
            answer = line[sep_index + 5:].strip()
            f.write(question + '\n')
            f.write(answer + '\n')
            f.write('\n')
