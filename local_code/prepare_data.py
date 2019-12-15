import csv
import os
import random
from os.path import join


def Generate_Data(datafile, store_dir):

    label_dict = dict()
    train_txt = join(store_dir, "train.txt")
    text_txt = join(store_dir, "test.txt")
    f1 = open(train_txt, 'w', encoding="utf-8")
    f2 = open(text_txt, 'w', encoding="utf-8")
    train = []
    test = []

    with open(datafile, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            text = row[0].lower() # 变成全小写
            text = ''.join([x for x in text if x.isalpha() or x == ' ']).strip() #只保留字母和空格并去掉开头和结尾的空格
            label = eval(row[1])[0].strip()
            label = label.split()
            label = '-'.join([x for x in label])
            if label not in label_dict:
                label_dict[label] = list()
            label_dict[label].append(text)
    
    for k, v in label_dict.items():
        if len(v) < 10:
            continue
        for i in range(1, len(v) + 1):  # 每种类别的30%做测试集，70%做训练集
            if i / len(v) < 0.3:
                continue
            random.shuffle(v)
            for j in range(0, i):
                test.append(k + '\t\t' + v[j] + '\n')
            for j in range(i, len(v)):
                train.append(k + '\t\t' + v[j] + '\n')
            break
    f1.writelines(train)
    f2.writelines(test)
    f1.close()
    f2.close()
            

if __name__ == "__main__":
    crruent_path = os.getcwd()
    parent_path = os.path.dirname(crruent_path)
    datafile = join(join(parent_path, "ori_data"), "dataset.csv")
    store_dir = join(parent_path, "data")
    if not os.path.exists(store_dir):
        os.makedirs(store_dir)
    Generate_Data(datafile, store_dir)