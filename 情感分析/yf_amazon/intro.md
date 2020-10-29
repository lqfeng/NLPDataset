# yf_amazon 说明
0. **下载地址：** [百度网盘](https://pan.baidu.com/s/1SbfpZb5cm-g2LmnYV_af8Q)
1. **数据概览：** 52 万件商品，1100 多个类目，142 万用户，720 万条评论/评分数据
2. **推荐实验：** 推荐系统、情感/观点/评论 倾向性分析
2. **数据来源：** [亚马逊](https://www.amazon.cn/)
3. **原数据集：** [JD.com E-Commerce Data](http://yongfeng.me/dataset/)，Yongfeng Zhang 教授为 WWW 2015 会议论文而搜集的数据
4. **加工处理：**
    1. 将全角字符转换为半角字符，并采用 UTF-8 编码
    2. 整理成与 [MovieLens](https://grouplens.org/datasets/movielens/) 兼容的格式
    3. 进行脱敏操作，以保护用户隐私


```python
import pandas as pd
```


```python
path = 'yf_amazon_文件夹_所在_路径'
```

# 1. products.csv

## 加载数据


```python
products = pd.read_csv(path + 'products.csv')

print('产品数目：%d' % products.shape[0])
```

    产品数目：525619


## 字段说明

| 字段 | 说明 |
| ---- | ---- |
| productId | 产品 id (从 0 开始，连续编号) |
| name | 产品名称 |
| catIds | 类别 id（从 0 开始，连续编号，从左到右依次表示一级类目、二级类目、三级类目） |


```python
products.sample(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>productId</th>
      <th>name</th>
      <th>catIds</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>331420</th>
      <td>331420</td>
      <td>欧意金狐狸 女式 皮手套 QT602</td>
      <td>802,143,996</td>
    </tr>
    <tr>
      <th>130945</th>
      <td>130945</td>
      <td>YESO TOT 中性 单肩包/斜挎包 均码 9411</td>
      <td>1111,864,781</td>
    </tr>
    <tr>
      <th>179886</th>
      <td>179886</td>
      <td>李斯特论柏辽兹与舒曼</td>
      <td>832,552,337</td>
    </tr>
    <tr>
      <th>504123</th>
      <td>504123</td>
      <td>Tuscarora 途斯卡洛拉 中性 烈焰驰骋无缝头巾 PSU3083</td>
      <td>1111,522,720</td>
    </tr>
    <tr>
      <th>387785</th>
      <td>387785</td>
      <td>我们的故事:一百个北大荒老知青的人生形态</td>
      <td>832,519,599</td>
    </tr>
    <tr>
      <th>406231</th>
      <td>406231</td>
      <td>图读周易</td>
      <td>832,723,724</td>
    </tr>
    <tr>
      <th>199072</th>
      <td>199072</td>
      <td>Barbie 芭比 女童 运动休闲鞋 A22993</td>
      <td>802,777,601</td>
    </tr>
    <tr>
      <th>518528</th>
      <td>518528</td>
      <td>HiVi 惠威 多媒体音箱 D1080MKII 2.0声道 棕色</td>
      <td>1057,439,1064</td>
    </tr>
    <tr>
      <th>446621</th>
      <td>446621</td>
      <td>HALTI 男式 JUOVAJACKET 芬兰国家队系列 羽绒滑雪服 H0591922</td>
      <td>1111,651,693</td>
    </tr>
    <tr>
      <th>379960</th>
      <td>379960</td>
      <td>塑料回收再生术:百工百技</td>
      <td>832,1096,509</td>
    </tr>
  </tbody>
</table>
</div>



# 2. categories.csv

## 加载数据


```python
categories = pd.read_csv(path + 'categories.csv')

print('类别数目：%d' % categories.shape[0])
```

    类别数目：1175


## 字段说明

| 字段 | 说明 |
| ---- | ---- |
| catId | 类别 id (从 0 开始，连续编号) |
| category | 类别名称 |


```python
categories.sample(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>catId</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>947</th>
      <td>947</td>
      <td>理发器</td>
    </tr>
    <tr>
      <th>818</th>
      <td>818</td>
      <td>电脑硬件</td>
    </tr>
    <tr>
      <th>212</th>
      <td>212</td>
      <td>帐篷</td>
    </tr>
    <tr>
      <th>815</th>
      <td>815</td>
      <td>路由器/中继器</td>
    </tr>
    <tr>
      <th>829</th>
      <td>829</td>
      <td>拉杆箱/包</td>
    </tr>
    <tr>
      <th>391</th>
      <td>391</td>
      <td>女鞋</td>
    </tr>
    <tr>
      <th>756</th>
      <td>756</td>
      <td>大型健身器械</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>其他运动器材</td>
    </tr>
    <tr>
      <th>633</th>
      <td>633</td>
      <td>垂钓用品</td>
    </tr>
    <tr>
      <th>115</th>
      <td>115</td>
      <td>卡通</td>
    </tr>
  </tbody>
</table>
</div>



# 3. ratings.csv

## 加载数据


```python
pd_ratings = pd.read_csv(path+'ratings.csv')

print('用户 数目：%d' % pd_ratings.userId.unique().shape[0])
print('评分/评论 数目（总计）：%d\n' % pd_ratings.shape[0])
```

    用户 数目：1424596
    评分/评论 数目（总计）：7202921
    


## 字段说明

| 字段 | 说明 |
| ---- | ---- |
| userId | 用户 id (从 0 开始，连续编号) |
| productId | 即 products.csv 中的 productId |
| rating | 评分，[1,5] 之间的整数 |
| timestamp | 评分时间戳 |
| title | 评论的标题 |
| comment |  评论的内容 |


```python
pd_ratings.sample(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>productId</th>
      <th>rating</th>
      <th>timestamp</th>
      <th>title</th>
      <th>comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4287636</th>
      <td>230944.0</td>
      <td>394505</td>
      <td>5.0</td>
      <td>1393084800</td>
      <td>赞!</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3940838</th>
      <td>16628.0</td>
      <td>84789</td>
      <td>5.0</td>
      <td>1389715200</td>
      <td>喜欢</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4064284</th>
      <td>325829.0</td>
      <td>94108</td>
      <td>3.0</td>
      <td>1384531200</td>
      <td>磨脚</td>
      <td>右脚小脚趾磨掉一块皮</td>
    </tr>
    <tr>
      <th>4802616</th>
      <td>586385.0</td>
      <td>254002</td>
      <td>5.0</td>
      <td>1383408000</td>
      <td>哦~</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>292946</th>
      <td>842028.0</td>
      <td>231449</td>
      <td>5.0</td>
      <td>1369324800</td>
      <td>致我们终将逝去的青春</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2306551</th>
      <td>933226.0</td>
      <td>219015</td>
      <td>4.0</td>
      <td>1341763200</td>
      <td>有点大 不过很漂亮</td>
      <td>外观很精致的说 就是外形有点偏大</td>
    </tr>
    <tr>
      <th>1707442</th>
      <td>402851.0</td>
      <td>228321</td>
      <td>5.0</td>
      <td>1374076800</td>
      <td>给宝宝讲讲挺好的,内容简单,便于宝宝理解。</td>
      <td>给宝宝讲讲挺好的,内容简单,便于宝宝理解。</td>
    </tr>
    <tr>
      <th>3641724</th>
      <td>123473.0</td>
      <td>515623</td>
      <td>4.0</td>
      <td>1305475200</td>
      <td>书很好,但居然没有包装!?!?!?</td>
      <td>书很好,但居然没有包装!?!?!?这么好的书却没有包装!?!?!?</td>
    </tr>
    <tr>
      <th>1921912</th>
      <td>435946.0</td>
      <td>63238</td>
      <td>4.0</td>
      <td>1357228800</td>
      <td>嗯</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1475151</th>
      <td>1612.0</td>
      <td>139044</td>
      <td>4.0</td>
      <td>1316102400</td>
      <td>一般</td>
      <td>香味没有前面评价那么香,就是普通的爽肤水,有点黏黏的</td>
    </tr>
  </tbody>
</table>
</div>



# 4. links.csv

## 加载数据


```python
links = pd.read_csv(path + 'links.csv')
```

## 字段说明

| 字段 | 说明 |
| ---- | ---- |
| productId | 即 products.csv 和 ratings.csv 中的 productId |
| amazonId | 亚马逊的产品编号 |


```python
links.sample(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>productId</th>
      <th>amazonId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>436251</th>
      <td>436251</td>
      <td>B00F91KYGK</td>
    </tr>
    <tr>
      <th>194578</th>
      <td>194578</td>
      <td>B00GICSVUK</td>
    </tr>
    <tr>
      <th>336998</th>
      <td>336998</td>
      <td>B00GMKUNBI</td>
    </tr>
    <tr>
      <th>371924</th>
      <td>371924</td>
      <td>B008RIA4AS</td>
    </tr>
    <tr>
      <th>433617</th>
      <td>433617</td>
      <td>B00332FJ7Q</td>
    </tr>
    <tr>
      <th>236918</th>
      <td>236918</td>
      <td>060614479X</td>
    </tr>
    <tr>
      <th>388158</th>
      <td>388158</td>
      <td>B008TI5V2C</td>
    </tr>
    <tr>
      <th>479855</th>
      <td>479855</td>
      <td>B002NSML6I</td>
    </tr>
    <tr>
      <th>311842</th>
      <td>311842</td>
      <td>B001DTWV2C</td>
    </tr>
    <tr>
      <th>445227</th>
      <td>445227</td>
      <td>B0055PT83U</td>
    </tr>
    <tr>
      <th>360465</th>
      <td>360465</td>
      <td>B005UTT2QY</td>
    </tr>
    <tr>
      <th>258363</th>
      <td>258363</td>
      <td>0805092919</td>
    </tr>
    <tr>
      <th>308642</th>
      <td>308642</td>
      <td>B0079WMXT8</td>
    </tr>
    <tr>
      <th>232740</th>
      <td>232740</td>
      <td>B0018HKRAW</td>
    </tr>
    <tr>
      <th>335318</th>
      <td>335318</td>
      <td>B00840LWKU</td>
    </tr>
    <tr>
      <th>497048</th>
      <td>497048</td>
      <td>B003ZI61RA</td>
    </tr>
    <tr>
      <th>388969</th>
      <td>388969</td>
      <td>B00BIUYL06</td>
    </tr>
    <tr>
      <th>10448</th>
      <td>10448</td>
      <td>B00GMZ9DKK</td>
    </tr>
    <tr>
      <th>75752</th>
      <td>75752</td>
      <td>B002R0DNB4</td>
    </tr>
    <tr>
      <th>392345</th>
      <td>392345</td>
      <td>B0041IY7CE</td>
    </tr>
  </tbody>
</table>
</div>


