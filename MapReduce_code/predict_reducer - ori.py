import sys
"""
    NWei: dict 套 dict, NWei[ei][xi] 表示训练集中标签为ei的文章中单词xi出现了几次（不去重） 
    NW：a dict， NW[ei] 表示训练集中标签为ei的文章中包含了几个单词（不去重）
    Nei: a dict, Nei[ei] 表示训练集中标签为ei的文章总数
    N： 训练集文章总数
    words: a set 记录训练集中出现过的单词

输入：
<<testID>, <label, p>>
输出：每个title 概率最高的5个类别
<<test_ID>,  <label1, label2, label3, label4, label5>>
"""
total = 0
predict = dict()
for row in sys.stdin:
    testID, value = row.split("\t\t")
    value = value.split()
    if testID not in predict:
        predict[testID] = dict()
    predict[testID][value[0]] = float(value[1])

for testID in predict:
    p = sorted(predict[testID].items(), key=lambda d:d[1], reverse=True)
    output = "{}\t\t{} {} {} {} {}".format(testID, p[0], p[1], p[2], p[3], p[4])
    print(output)





