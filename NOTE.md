# 任务型对话机器人笔记

## TOPK TOPP
在自然语言生成（NLG）中，"topk"和"topp"通常用于指从给定集合中选择前k或前p项的技术。例如，top-k选择涉及从集合中选择具有最高分数或值的k个项目，而top-p选择涉及从具有发生概率最高的p个项目中选择。这些技术在NLG中常用于从大型数据集中选择最相关或重要的信息，并生成概括或传达该信息给用户的自然语言文本。

## 进行测试
python interact.py --no_cuda --model_path model/pytorch_model.bin  
python preprocess.py --train_path data/train1.txt --save_path data/train1.pkl  
//注意--val_num 必须大于等于一个batch_size的大小  
python train.py --epochs 40 --no_cuda --batch_size 8 --train_path data/train1.pkl --pretrained_model model/pytorch_model.bin --model_config model/config.json  
//测试一下
python interact.py --no_cuda --model_path model/epoch40/pytorch_model.bin --config_path model/epoch40/config.json

## warmup
num_warmup_steps 是一个参数，用于在使用 get_linear_schedule_with_warmup 函数时指定预热期的训练步数。预热期是训练开始时的一段时间，在这段时间内，学习率逐渐从初始值增加到指定的最大学习率。这可以帮助模型更快地收敛，并提高其性能。
num_warmup_steps 的值应根据训练数据集的大小和模型的复杂度来选择。作为一般准则，训练数据集越大，模型越复杂，就需要越多的预热步骤。
对于确定特定用例的 num_warmup_steps 的值，可以使用几种不同的方法：
实证试验：可以尝试几个不同的 num_warmup_steps 值，并查看模型的表现。然后，可以选择表现最佳的值。
准则：可以使用通用准则来设置 num_warmup_steps。例如，可以选择等于总训练步数的 10％ 的值。
专家建议：可以向该领域的专家或研究论文咨询，看看其他研究人员在类似情况下为 num_warmup_steps 使用了什么值。
最终，num_warmup_steps 的最佳值将取决于训练数据集和模型的具体特征，因此可能需要一些实验来确定最优值。
总的来说，num_warmup_steps 是一个重要的参数，可以帮助在训练深度学习模型时更好地控制学习率。它的值可以通过试验、通用准则或专家建议确定，并应根据训练数据集和模型的特征进行调整。

num_training_steps = num_epochs * (size_of_training_dataset / batch_size)
如果正在训练一个 10 个周期、批量大小为 32 和训练数据集大小为 10,000 样本的模型，则总训练步数将是：
num_training_steps = 10 * (10000 / 32) = 3125
目前的训练数据 40*800
40 * (12954/32)
