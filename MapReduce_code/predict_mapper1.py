import sys
"""
输入：
<<label>, <0, N, Nei, word, numofword>>
<<label>, <1, testID, testtitle>>
输出 = 输入，目的是理由shuffle先排个序

"""
for row in sys.stdin:
    row = row.strip()
    key, value = row.split('\t\t')
    key_value = "{}\t{}".format(key, value)
    print(key_value)
