import sys
"""
输入：
<<testID>, <label, p>>
输出：每个title 概率最高的5个类别
<<test_ID>,  <label1, label2, label3, label4, label5>>
"""
total = 0
predict = dict()
for row in sys.stdin:
    testID, value = row.split('\t\t')
    value = value.split()
    if testID not in predict:
        predict[testID] = dict()
    predict[testID][value[0]] = float(value[1])

for testID in predict:
    p = sorted(predict[testID].items(), key=lambda d:d[1], reverse=True)
    output = "textid: {}\t\t{} {} {} {} {}".format(testID, p[0][0], p[1][0], p[2][0], p[3][0], p[4][0])
    print(output)