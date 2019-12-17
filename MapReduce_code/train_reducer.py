import sys
"""
输入：
<label, <word, 1>>
<label, 1> 
输出：
<<label>, <0, Nei, word, numofword>>
统计标签为label的title中 单词word的出现次数
"""
wordHash = dict()  
# 键值为（label, word）的字典，统计标签为label的title中单词word出现的次数
titleHash = dict()
# 键值为label的字典，统计标签为label的title个数
for row in sys.stdin:
    key, value = row.split('\t\t')
    value = value.split()
    if len(value) == 1:
        if key not in titleHash:
            titleHash[key] = 0
        titleHash[key] += int(value[0])
    elif len(value) == 2:
        newkey = key + ' ' + value[0]
        if newkey not in wordHash:
            wordHash[newkey] = 0
        wordHash[newkey] += int(value[1])

for k,v in wordHash.items(): # 得到输出格式
    k = k.split(' ')
    key = k[0]
    value = str(0) + ' ' + str(titleHash[key]) + ' ' + k[1] + ' ' + str(v)
    print(key + "\t\t" + value)
