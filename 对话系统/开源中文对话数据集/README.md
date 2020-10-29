# 数据集

1.闲聊对话相关数据：华为的微博数据 [1] ，北航和微软的豆瓣多轮对话 [2]，清华的LCCC数据集[3]。
2.知识对话相关数据：百度的DuConv [4]，清华的KdConv [5]，腾讯的检索辅助生成对话数据集 [6]
3.推荐对话相关数据：百度的DuRecDial [7]

# Paper

[1] Lifeng Shang, Zhengdong Lu, Hang Li. 2015. Neural Responding Machine for Short-Text Conversation. In ACL.
[2] Yu Wu, Wei Wu, Chen Xing, Ming Zhou, Zhoujun Li. 2017. Sequential Matching Network: A New Archtechture for Multi-turn Response Selection in Retrieval-based Chatbots. In ACL.
[3] Yida Wang, Pei Ke, Yinhe Zheng, Kaili Huang, Yong Jiang, Xiaoyan Zhu, Minlie Huang. 2020. A Large-Scale Chinese Short-Text Conversation Dataset. In NLPCC
[4] Wenquan Wu, Zhen Guo, Xiangyang Zhou, Hua Wu, Xiyuan Zhang, Rongzhong Lian, and Haifeng Wang. 2019. Proactive human-machine conversation with explicit conversation goal. In ACL.
[5] Hao Zhou, Chujie Zheng, Kaili Huang, Minlie Huang, Xiaoyan Zhu. 2020. KdConv: A Chinese Multi-domain Dialogue Dataset Towards Multi-turn Knowledge-driven Conversation. In ACL.
[6] Deng Cai, Yan Wang, Wei Bi, Zhaopeng Tu, Xiaojiang Liu, Shuming Shi. 2019. Retrieval-guided Dialogue Response Generation via a Matching-to-Generation Framework. In EMNLP.
[7] Zeming Liu, Haifeng Wang, Zheng-Yu Niu, Hua Wu, Wanxiang Che, Ting Liu. 2020. Towards Conversational Recommendation over Multi-Type Dialogs. In ACL.

# 数据来源

https://www.datafountain.cn/competitions/470/datasets

# 官方基线模型

#### **基线模型地址：**

https://github.com/PaddlePaddle/Knover/tree/luge-dialogue/luge-dialogue

#### **基线模型结果：**

score: 0.24

F1: 15.44

BLEU1/BLEU2: 0.059/0.027

DISTINCT1/DISTINCT2: 0.044/0.217

# 数据说明

[给出用于竞赛训练数据集文件的格式说明, 说明包含文件的名称说明、文件编码说明、文件中的数据格式说明以及各个数据字段的详细说明]
文件名称：train.txt
文件的编码:UTF-8
文件格式如下：
{
“subtrack”: “recommend”, # knowledge/chitchat/recommend
“profile”: {“profile key 1”: “profile value 1”, “profile key 2”: “profile value 2”, …, “profile key m-1”: [“profile value m-1 element 1”, “profile value m-1 element 2”, …, “profile value m-1 element n”], “profile key m”: [“profile value m element 1”, “profile value m element 2”, …, “profile value m element n”]},
“situation”: “xxxx”,
“goal”: [[“goal 1 element 1”, “goal 1 element 2”, …, “goal 1 element m”], [“goal 2 element 1”, “goal 2 element 2”, …, “goal 2 element m”], …, [“goal n element 1”, “goal n element 2”, …, “goal n element m”]],
“knowlege”: [[“knowlege 1 element 1”, “knowlege 1 element 2”, …, “knowlege 1 element m”], [“knowlege 2 element 1”, “knowlege 2 element 2”, …, “knowlege 2 element m”], …, [“knowlege n element 1”, “knowlege n element 2”, …,gg “knowlege n element m”]],
“history”: [“utterance 1”, “utterance 2”, …, “utterance n”]
}
数据字段说明：
subtrack：任务标识符，用来区分不同子任务。
profile：用户画像，包含用户的基本属性和领域偏好、实体偏好等。个别任务可能为空。
situation：对话场景，包括对话时间、对话主题等。个别任务可能为空。
goal：对话目标或目标序列。个别任务可能为空。
knowledge：对话所需的背景知识。个别任务可能为空。
history：对话历史。只要不是预测首轮回复，就不为空。



# 提交要求

本次比赛的测评分两阶段进行，我们会准备两个测试集，测试集A和测试集B：
测试集A中的对话是从下述对话数据集中采样得到，属于公开数据：
1.闲聊对话：华为的微博数据 [1] ，北航和微软的豆瓣多轮对话 [2]，清华的LCCC数据集[3]，
2.知识对话：百度的DuConv [4]，清华的KdConv [5]，腾讯的检索辅助生成对话数据集 [6]，
3.推荐对话：百度的DuRecDial [7]。

测试集B中的对话均为未公开数据：
1.闲聊对话：未出现在现有公开数据集中的微博对话；
2.知识对话：百度Duconv数据集的测试部分；
3.推荐对话：百度durecdial数据集的测试部分。

第一阶段为初赛阶段（自动指标评测）
参赛队报名后即可获得测试集A，并可以在测试集A上开发自己的模型。初赛阶段每天有一次提交机会，参赛队需要将模型在测试集A上所生成的回复整理成相应的格式后提交。我们拿到所提交的文件后会计算各个自动指标，并将结果更新在A榜上。
在初赛结束前一天，我们会开放测试集B的下载，参赛队需要在24小时内提交模型在测试集B上的生成结果。基于这一结果的自动指标测评分数将更新在B榜。B榜上的排名将作为初赛阶段的最终成绩。
初赛阶段我们会使用各自动指标上的平均值作为排名依据。我们会选取排名前10的队伍进入复赛阶段
初赛阶段提交结果格式如下：
分别预测以上7个数据集的所有回复，并按给定数据集的顺序合并预测的回复。最终结果文件共43582行，每行一个回复句子，是根据输入数据预测的回复，注意保留分词信息，示例如下：
**这种 天气 适合 吃 糖醋排骨 了 呢 。**
注意：结果提交文件是一个文本文件。

提交注意事项
1.在线评估提交限制：每个队伍每天最多提交5次结果进行在线评测，如新提交结果好于之前提交结果，排行榜中的成绩将自动覆盖。
2.测试集A：供参赛队伍自助验证模型效果，提交结果后将在排行榜中显示成绩和排名。该成绩和排名不作为晋级复赛阶段的参考依据。
3.测试集B：测试参赛队伍所提交模型的效果，提交结果后将在排行榜中显示成绩和排名。该成绩和排名作为晋级复赛阶段的参考依据。

第二阶段为复赛阶段（人工指标测评）
我们要求进入复赛的参赛队在复赛阶段提供一个可供调用的http接口，这一接口可以接接收对话上下文作为输入，并返回模型所生成的对话回复。复赛测评阶段，我们会调用该接口，并聘请评测人员对模型所生成的对话的质量进行打分。评测人员会与模型开展多轮对话，并根据人工指标中所给出的维度对模型进行打分评价。
人工评估阶段会为评测人员和对话模型提供包含1-2句话的对话历史，要求评测人员在该对话历史上展开对话。
最终比赛排名将以人工评测结果为准。
复赛阶段，每个参赛团队最终人工评估只能提交1个系统API。API的输入输出数据结构如下：

a. 输入数据结构：
{
“subtrack”: “recommend”, # knowledge/chitchat/recommend

“profile”: {“profile key 1”: “profile value 1”, “profile key 2”: “profile value 2”, …, “profile key m-1”: [“profile value m-1 element 1”, “profile value m-1 element 2”, …, “profile value m-1 element n”], “profile key m”: [“profile value m element 1”, “profile value m element 2”, …, “profile value m element n”]},

“situation”: “xxxx”,

“goal”: [[“goal 1 element 1”, “goal 1 element 2”, …, “goal 1 element m”], [“goal 2 element 1”, “goal 2 element 2”, …, “goal 2 element m”], …, [“goal n element 1”, “goal n element 2”, …, “goal n element m”]],

“knowlege”: [[“knowlege 1 element 1”, “knowlege 1 element 2”, …, “knowlege 1 element m”], [“knowlege 2 element 1”, “knowlege 2 element 2”, …, “knowlege 2 element m”], …, [“knowlege n element 1”, “knowlege n element 2”, …,gg “knowlege n element m”]],

“history”: [“utterance 1”, “utterance 2”, …, “utterance n”]
}
b. 输出数据结构：
{
“error code”: 0, # 0 is success
“response”: “response”
}

提交注意事项：
1.不需要的字段为空，但是要保持数据结构一致。比如，闲聊中profile、situation、goal、knowledge为空；知识对话中profile、situation、goal可能为空。
2.因为评估时间短、任务繁重等原因，所提交的系统API，输入、输出必须跟规定一致，否则取消人工评估成绩。

# 提交示例

[对于参赛者的提交文件格式要求做出具体的说明. 提交文件的命名, 提交文件的编码以及提交文件内容的格式要求等]

提交文件的命名：ccf_baidu_dialog_result.txt
提交文件的编码:UTF-8
初赛阶段提交文件内容的格式如下：
分别预测以上7个数据集的所有回复，并按给定数据集的顺序合并预测的回复。最终结果文件共43582行，每行一个回复句子，是根据输入数据预测的回复，注意保留分词信息，示例如下：
**这种 天气 适合 吃 糖醋排骨 了 呢 。**

注意：结果提交文件是一个文本文件。

# 评测标准

上述三个子任务分别使用如下自动指标进行评测。
1.子任务1闲聊对话：F1, BLEU1-2, DISTINCT1-2；
2.子任务2知识对话：F1, BLEU1-2, DISTINCT1-2；
3.子任务3推荐对话：F1, BLEU1-2, DISTINCT1-2.
F1是汉字级别的打分，BLEU1－2是中文词级别的打分，DISTINCT1－2是中文词级别的对话内容多样性的自动指标。
自动评估阶段的总得分通过计算以上子任务下的F1/BLEU1/BLEU2的分数平均值得到。

我们同时在复赛阶段还会使用如下人工指标：
子任务1闲聊对话：

1. 丰富度(0-2)：评价回复句子本身的信息丰富程度
2. 话题一致性(0-2)：评价输出回复句子回复输入上文的合适程度，是否话题契合、逻辑正确等

子任务2知识对话：

1. 丰富度(0-2)：评价回复句子本身的信息丰富程度
2. 话题一致性(0-2)：评价输出回复句子回复输入上文的合适程度，是否话题契合、逻辑正确等
3. 知识准确率(0-2)：评价回复句子所用知识的准确率

子任务3推荐对话：

1. 丰富度(0-2)：评价回复句子本身的信息丰富程度
2. 话题一致性(0-2)：评价输出回复句子回复输入上文的合适程度，是否话题契合、逻辑正确等
3. 知识准确率(0-2)：评价回复句子所用知识的准确率
4. 推荐成功率(0-2)：评价最终推荐目标完成的程度

人工评估阶段的总得分通过计算以上子任务下的指标分数平均值得到。
