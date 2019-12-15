import sys
"""
<<0, label, word>, cnt>   表示训练集中标签为label的title中单词xi出现了cnt次（不去重） 
<<1, label>, cnt>   表示训练集中标签为label的title总数

reducer 中使用 Hash字典来统计每一个key 的出现总数
"""
Hash = dict()
for row in sys.stdin:
    key, value = row.split('\t\t')
    if key not in Hash:
        Hash[key] = int(value)
    else:
        Hash[key] += int(value)

for key in Hash:
    key_value = key + "\t\t" + str(Hash[key])
    print(key_value)