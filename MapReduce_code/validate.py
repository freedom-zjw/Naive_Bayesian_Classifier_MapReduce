f1 = open("../data/test.txt", "r", encoding="utf-8")
lines = f1.readlines()
f1.close()

N = len(lines)
GroundTrue = []
for i in range(N):
    lines[i] = lines[i].strip()
    label, title = lines[i].split('\t\t')
    GroundTrue.append(label)

f1 = open("predict_result.txt", "r", encoding="utf-8")
lines = f1.readlines()
f1.close()
r1 = 0
r5 = 0
total = 0
predict = dict()
for row in lines:
    row = row.strip()
    # <<test_ID>,  <label1, label2, label3, label4, label5>>
    test_ID, predict_label = row.split('\t\t')
    test_ID = test_ID.split()[1]
    predict_label  = predict_label.strip()
    total += 1
    test_ID = int(test_ID)
    predict[test_ID] = predict_label

predict = sorted(predict.items(), key=lambda d:d[0], reverse=False)

f1 = open("final_result.txt", "w", encoding="utf-8")
final_result = []

for i in range(total):
    predict_label = predict[i][1].split()
    for j in range(5):
        if j == 0:
            if predict_label[j] == GroundTrue[i]:
                r1 += 1
        if predict_label[j] == GroundTrue[i]:
            r5 += 1
            break
    final_result.append("textid: {}   predict_label: {}\n".format(i, predict_label))
    final_result.append("\n")

print("Total test title: {}".format(total))
final_result.append("Total test title: {}\n".format(total))
print("Number of rank1 correct prediction: {}".format(r1))
final_result.append("Number of rank1 correct prediction: {}\n".format(r1))
print("Number of rank5 correct prediction: {}".format(r5))
final_result.append("Number of rank5 correct prediction: {}\n".format(r5))
print("Rank1 Accuracy: {}".format(float(r1) / total))
final_result.append("Rank1 Accuracy: {}\n".format(float(r1) / total))
print("Rank5 Accuracy: {}".format(float(r5) / total))
final_result.append("Rank5 Accuracy: {}\n".format(float(r5) / total))
f1.writelines(final_result)
f1.close()
