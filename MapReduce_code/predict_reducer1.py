import sys
"""
NWei: dict 套 dict, NWei[label][xi] 表示训练集中标签为ei的文章中单词xi出现了几次（不去重） 
NW：a dict， NW[label] 表示训练集中标签为label的文章中包含了几个单词（不去重）
Nei: a dict, Nei[label] 表示训练集中标签为label的文章总数
N： 训练集文章总数
words: a set 记录训练集中出现过的单词

输入：
<<label>, <0, N, Nei, word, numofword>>
<<label>, <1, testID, testtitle>>
输出：
<<testID>, <label, p>>

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
        testtitle.append(row)
    elif value[0] == 0:
        N = int(value[1])
        word = value[3]
        wordset.add(word)
        if key not in Nei:
            Nei[key] = 0
            NW[key] = 0
            NWei[key] = dict()
        Nei[key] += int(value[2])
        NW[key] += int(value[4])
        if word not in NWei[key]:
            NWei[key][word] = 0
        NWei[key][word] += int(value[4])

    
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
