import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, BertTokenizer, GPT2Config

# # Initialize the tokenizer
# tokenizer = BertTokenizer.from_pretrained('pytorch_model.bin')
#
# # Tokenize some text
# text = "This is a sample sentence to be tokenized."
# tokens = tokenizer.tokenize(text)
#
# # Print the tokens
# print(tokens)

# 加载 GPT-2 模型
config = GPT2Config.from_json_file('model/config.json')
model = GPT2LMHeadModel.from_pretrained('model/pytorch_model.bin', config=config)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('using device:', device)
model.eval()
model.to(device)
# BertTokenizer
tokenizer = BertTokenizer.from_pretrained('model/pytorch_model.bin', vocab_file="vocab.txt")

input_text = "肯德基疯狂星期"
x = tokenizer.tokenize(input_text)
print(x)
y = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(input_text))
print(y)
generated_text = model.generate(x, max_length=100)
print(generated_text)
