import os
from os.path import join

def count(inputfile, result_file):
    f1 = open(inputfile, "r", encoding="utf-8")
    f2 = open(result_file, "w", encoding='utf-8')

    lines = f1.readlines()
    cnt = dict()

    for row in lines:
        label = row.split('\t')[0]
        if label not in cnt:
            cnt[label] = 0
        cnt[label] += 1

    result = []
    for k,v in cnt.items():
        result.append(k + '\t\t' + str(v) + '\n')
    f2.writelines(result) 

    f1.close()
    f2.close()


if __name__ == "__main__":
    crruent_path = os.getcwd()
    parent_path = os.path.dirname(crruent_path)

    trainfile = join(join(parent_path, "data"), "train.txt")
    testfile = join(join(parent_path, "data"), "test.txt")
    
    count(trainfile, "result_train.txt")
    count(testfile, "result_test.txt")