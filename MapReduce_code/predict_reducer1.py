import sys
"""
NWei: dict 套 dict, NWei[label][xi] 表示训练集中标签为label的title中单词xi出现了几次（不去重） 
NW：a dict， NW[label] 表示训练集中标签为label的title中包含了几个单词（不去重）
Nei: a dict, Nei[label] 表示训练集中标签为label的title总数
N： 训练集title总数
wordset: a set 记录训练集中出现过的单词

输入：
<<label>, <0, N, Nei, word, numofword>>
<<label>, <1, testID, testtitle>>
输出：
<<testID>, <label, p>> 第testID条测试数据的标签是label的概率为p
"""

wordset = set()
testtitle = []
N = 0
Nei = dict()
NWei = dict()
NW = dict()
alpha = 1.0
for row in sys.stdin:
    row = row.strip()
    key, value = row.split('\t')
    value = value.split()
    value[0] = int(value[0])
    if value[0] == 1:
        testtitle.append(row)  # 先保存好测试数据，后续再预测
    elif value[0] == 0:
        N = int(value[1])
        word = value[3]
        wordset.add(word)    # 更新word集合
        if key not in Nei:
            Nei[key] = 0
            NW[key] = 0
            NWei[key] = dict()
        Nei[key] = int(value[2])    # 更新Nei、NW、NWei
        NW[key] += int(value[4])
        if word not in NWei[key]:
            NWei[key][word] = 0
        NWei[key][word] += int(value[4])

# 注意这一步，由于不是每种label的title都包含了wordset的所有单词，所以这里要将没出现的单词次数设为0，因为测试title有可能有这些词   
for label in Nei:
    for word in wordset:
        if word not in NWei[label]:
            NWei[label][word] = 0   


# 计算第testID条title 属于 label的概率
for row in testtitle:
    label, value = row.split('\t')
    value = value.split()
    testID = int(value[1])
    title = value[2:]
    px = 1.0
    pe = float(Nei[label]) / N  # 计算p(ei)
    for word in title:
        if word not in wordset:
            continue
        px *= (float(NWei[label][word]) + alpha) / float((NW[label] + alpha * N))  #计算p(x|ei)
    p = px * pe #当前title属于label的概率
    output = "{}\t\t{} {}".format(str(testID), label, str(p))
    print(output)
