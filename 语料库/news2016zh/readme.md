
2.新闻语料json版(news2016zh)
-------------------------------------------------------------------------

#### 250万篇新闻( 原始数据9G，压缩文件3.6G；新闻内容跨度：2014-2016年)

<a href='https://drive.google.com/file/d/1TMKu1FpTr6kcjWXWlQHX7YJsMfhhcVKp/view?usp=sharing'>Google Drive下载</a>或 <a href='https://pan.baidu.com/s/1MLLM-CdM6BhJkj8D0u3atA'>百度云盘下载</a>，密码:k265

#### 数据描述

包含了250万篇新闻。新闻来源涵盖了6.3万个媒体，含标题、关键词、描述、正文。

数据集划分：数据去重并分成三个部分。训练集：243万；验证集：7.7万；测试集，数万，不提供下载。

#### 可能的用途：

    可以做为【通用中文语料】，训练【词向量】或做为【预训练】的语料；
   
    也可以用于训练【标题生成】模型，或训练【关键词生成】模型（选关键词内容不同于标题的数据）；

    亦可以通过新闻渠道区分出新闻的类型。

#### 结构：

    {'news_id': <news_id>,'title':<title>,'content':<content>,'source': <source>,'time':<time>,'keywords': <keywords>,'desc': <desc>, 'desc': <desc>}

    其中，title是新闻标题，content是正文，keywords是关键词，desc是描述，source是新闻的来源，time是发布时间

#### 例子：
    
    {"news_id": "610130831", "keywords": "导游，门票","title": "故宫淡季门票40元 “黑导游”卖外地客140元", "desc": "近日有网友微博爆料称，故宫午门广场售票处出现“黑导游”，专门向外地游客出售高价门票。昨日，记者实地探访故宫，发现“黑导游”确实存在。窗口出售", "source": "新华网", "time": "03-22 12:00", "content": "近日有网友微博爆料称，故宫午门广场售票处出现“黑导游”，专门向外地游客出售高价门票。昨日，记者实地探访故宫，发现“黑导游”确实存在。窗口出售40元的门票，被“黑导游”加价出售，最高加到140元。故宫方面表示，请游客务必通过正规渠道购买门票，避免上当受骗遭受损失。目前单笔门票购买流程不过几秒钟，耐心排队购票也不会等待太长时间。....再反弹”的态势，打击黑导游需要游客配合，通过正规渠道购买门票。"}
  

<img src="https://github.com/brightmart/nlp_chinese_corpus/blob/master/resources/img/news2016zh.png"  width="100%" height="100%" />

<br>
