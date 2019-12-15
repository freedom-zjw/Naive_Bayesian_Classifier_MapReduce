import sys
"""
<<0, label, word>, cnt>   表示训练集中标签为label的title中单词xi出现了cnt次（不去重） 
<<1, label>, cnt>   表示训练集中标签为label的title总数
"""
for row in sys.stdin:
    label, title = row.split('\t\t')
    title = title.split()
    for word in title:
        # <<0, label, word>, cnt> 
        key = str(0) + ' ' + label + ' ' + word
        value = str(1)
        key_value = key + "\t\t" + value
        print(key_value)
    # <<1, label>, cnt>
    key = str(1) + ' ' + label
    value = str(1)
    key_value = key + "\t\t" + value
    print(key_value)