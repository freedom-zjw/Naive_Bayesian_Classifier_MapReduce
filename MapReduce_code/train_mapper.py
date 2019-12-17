import sys
"""
输入：
label  title
输出：
<label, <word, 1>>
<label, 1> 
Nei[label]: 标签为label的title数
"""
for row in sys.stdin:
    label, title = row.split('\t\t')
    title = title.split()
    flag = False
    for word in title:
        key_value = "{}\t\t{}".format(label, word + ' ' + str(1))
        print(key_value)
    print("{}\t\t{}".format(label, str(1)))
