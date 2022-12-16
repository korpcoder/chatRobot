# 任务型对话机器人笔记

## TOPK TOPP
在自然语言生成（NLG）中，"topk"和"topp"通常用于指从给定集合中选择前k或前p项的技术。例如，top-k选择涉及从集合中选择具有最高分数或值的k个项目，而top-p选择涉及从具有发生概率最高的p个项目中选择。这些技术在NLG中常用于从大型数据集中选择最相关或重要的信息，并生成概括或传达该信息给用户的自然语言文本。

## 进行测试
python interact.py --no_cuda --model_path model/pytorch_model.bin
python preprocess.py --train_path data/train1.txt --save_path data/train1.pkl