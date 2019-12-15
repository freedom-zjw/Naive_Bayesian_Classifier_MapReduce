import sys
"""
输入：
<<label, Nei, word>, 1>
输出：
<<label>, <0, Nei, word, numofword>>
"""
Hash = dict()
for row in sys.stdin:
    key, value = row.split('\t\t')
    if key not in Hash:
        Hash[key] = int(value)
    else:
        Hash[key] += int(value)

for k,v in Hash.items():
    k = k.split(' ')
    key = k[0]
    value = str(0) + ' ' + k[1] + ' ' + k[2] + ' ' + str(v)
    print(key + "\t\t" + value)
