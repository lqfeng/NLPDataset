开放域问答数据集.zip
zip (20.1MB)
https://pan.baidu.com/s/1SaMpi6OUCehAcumK3i0rvA
kdpa
数据描述

该任务来自NLPCC 2017评测任务，开放域问答评价任务主要包括三项子任务，基于知识库的问答（kbqa），基于文档的问答（dbqa），和基于表的问答（tbqa）。kbqa的任务是基于知识库的中文问题回答。dbqa的任务是通过选择一个或多个句子从一个给定的文档，作为答案回答中文问题。tbqa的任务是一个全新的QA任务，旨在通过从收集的表格中抽取一个或多个表回答英语问题。
对于kbqa任务，我们将提供一个训练集和测试集。在训练集中，每个问题和它的答案都会被提供。如果存在多个答案，它们将被符号“\t”分隔开。在测试集中，只提供问题。 对于dbqa任务，我们将提供一个训练集和测试集。在训练集中，将问题在第一列、文档及其句子在第二列、答案注释在第三列。如果一个句子是问题的正确答案，那么它的答案注释将为“1”，否则它的答案注释将为“0”。这三列将被符号“\t”分隔开。在测试集中，只提供问题和文档。
对于tbqa任务，我们将提供一个训练集和测试集。在训练集中，将答案注释在第一列、问题在第二列、带标题的表格在第三列、属性在第四列、单元格在第五列。如果一个表格包含问题的正确答案，那么它的答案注释将为“1”，否则它的答案注释将为“0”。这五列将被符号“\t”分隔开。在第四列中，多个属性值被用符号’_|_’分隔。在第五列中，不同行被用符号‘_||_’隔开，而同行中的多个单元格被用‘_|_’隔开。在测试集中，只提供问题和候选表格。 有关该任务和数据集详细描述请见http://tcci.ccf.org.cn/conference/2017/taskdata.php

数据提供

提供方：微软亚洲研究院段楠主管研究员

主页地址：https://www.microsoft.com/en-us/research/people/nanduan/

联系方式：nanduan@microsoft.com

相关论文：Duan N., Tang D. (2018) Overview of the NLPCC 2017 Shared Task: Open Domain Chinese Question Answering. In: Huang X., Jiang J., Zhao D., Feng Y., Hong Y. (eds) Natural Language Processing and Chinese Computing. NLPCC 2017. Lecture Notes in Computer Science, vol 10619. Springer, Cham


