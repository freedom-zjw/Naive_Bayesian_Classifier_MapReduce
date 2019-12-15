import sys
"""
输入：
<<testID>, <label, p>>
输出 = 输入，目的是利用shuffle先排个序

"""
for row in sys.stdin:
    row = row.strip()
    key, value = row.split('\t\t')
    key_value = "{}\t\t{}".format(key, value)
    print(key_value)
