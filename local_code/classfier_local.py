import os
from os.path import join

def train(inputfile):
    """
    NWei: dict 套 dict, NWei[ei][xi] 表示训练集中标签为ei的文章中单词xi出现了几次（不去重） 
    NW：a dict， NW[ei] 表示训练集中标签为ei的文章中包含了几个单词（不去重）
    Nei: a dict, Nei[ei] 表示训练集中标签为ei的文章总数
    N： 训练集文章总数
    words: a set 记录训练集中出现过的单词
    """
    NWei, NW, Nei, words, N = dict(), dict(), dict(), set(), 0
    f1 = open(inputfile, "r", encoding="utf-8")
    lines = f1.readlines()

    for row in lines:
        ei, text = row.split('\t\t')
        text = text.split()
        N += 1  # 文章计数加1
        if ei not in Nei:
            Nei[ei] = 0
        if ei not in NW:
            NW[ei] = 0
        if ei not in NWei:
            NWei[ei] = dict()
        Nei[ei] += 1 # 标签为ei的文章总数
        for word in text:
            words.add(word) # 将单词扔进单词集合
            NW[ei] += 1 # 标签为ei的文章中包含了几个单词
            if word not in NWei[ei]:
                NWei[ei][word] = 0
            NWei[ei][word] += 1 # 标签为ei的文章中单词word的出现次数
    
    for ei in Nei:
        for word in words:
            if word not in NWei[ei]:
                NWei[ei][word] = 0

    f1.close()
    return NWei, NW, Nei, words, N

def test(inputfile, model):
    NWei, NW, Nei, words, N = model
    alpha = 1
    f1 = open(inputfile, "r", encoding="utf-8")
    lines = f1.readlines()
    r1_correct, r5_correct, total = 0, 0, 0
    f1= open("local_predict_result.txt", "w", encoding="utf-8")
    result = []
    for row in lines:
        ei, text = row.split('\t\t')
        text = text.split()
        total += 1
        predict = dict()
        psum = 0.0

        for label in Nei: # 枚举标签
            px = 1.0
            pe = float(Nei[label]) / N  # 计算p(ei)
            for word in text:
                if word not in words:
                    continue
                px *= (float(NWei[label][word]) + alpha) / float((NW[label] + alpha * N))  #计算p(x|ei)
            p = px * pe #当前文章属于label的概率
            predict[label] = p
            psum += p
        for k in predict:
            predict[k] /= psum  # 将概率归一化，保证概率和为1
        predict = sorted(predict.items(), key=lambda d:d[1], reverse=True)
        
        rank5_label = []
        for i in range(5):
            rank5_label.append(predict[i][0])
            if len(rank5_label) == 1:
                if rank5_label[0] == ei:
                    r1_correct += 1
            if len(rank5_label) == 5:
                break
        for x in rank5_label:
            if x == ei:
                r5_correct += 1
                break
            
        result.append("textid: {}   predict_label: {}\n".format(total - 1, rank5_label))
    result.append("\n")
    print("Total test title: {}".format(total))
    result.append("Total test title: {}\n".format(total))
    print("Number of rank1 correct prediction: {}".format(r1_correct))
    result.append("Number of rank1 correct prediction: {}\n".format(r1_correct))
    print("Number of rank5 correct prediction: {}".format(r5_correct))
    result.append("Number of rank5 correct prediction: {}\n".format(r5_correct))
    print("Rank1 Accuracy: {}".format(float(r1_correct) / total))
    result.append("Rank1 Accuracy: {}\n".format(float(r1_correct) / total))
    print("Rank5 Accuracy: {}".format(float(r5_correct) / total))
    result.append("Rank5 Accuracy: {}\n".format(float(r5_correct) / total))
    f1.writelines(result)
    f1.close()


if __name__ == "__main__":
    crruent_path = os.getcwd()
    parent_path = os.path.dirname(crruent_path)

    trainfile = join(join(parent_path, "data"), "train.txt")
    testfile = join(join(parent_path, "data"), "test.txt")

    model = train(trainfile)
    test(testfile, model)
