import sys
"""
输入：
label  title
输出：
<<label, Nei, word>, 1>
Nei[label]: 标签为label的title数
"""
Nei = dict()
titles = []
for row in sys.stdin: # 先计算Nei
    titles.append(row)
    label, title = row.split('\t\t')
    if label not in Nei:
        Nei[label] = 0
    Nei[label] += 1

for row in titles: # 得到输出格式
    label, title = row.split('\t\t')
    title = title.split()
    for word in title:
        key_value = "{}\t\t{}".format(label + ' ' + str(Nei[label]) + ' ' + word, str(1))
        print(key_value)