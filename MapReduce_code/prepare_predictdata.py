
f1 = open("../data/train.txt", "r", encoding = "utf-8")
lines = f1.readlines()
f1.close()
N = len(lines)
labelset = set()
for row in lines:
    label, title = row.split('\t\t')
    labelset.add(label)

newData = []
f1 = open("trainoutput.txt", "r", encoding="utf-8")
lines = f1.readlines()
f1.close()

for row in lines:
    row = row.strip()
    label, title = row.split('\t\t')
    title1 = [title.split()[0] + ' ' + str(N)]
    title2 = title.split()[1:]
    newTitle = title1 + title2
    newTitle = ' '.join(newTitle)
    line = label + '\t\t' + newTitle + '\n'
    newData.append(line)
    

f1 = open("../data/test.txt", "r", encoding = "utf-8")
lines = f1.readlines()
f1.close()


testID = 0
for row in lines:
    row = row.strip()
    label, title = row.split('\t\t')
    for x in labelset:
        newData.append(x + '\t\t' + str(1) + ' ' + str(testID) + ' ' + title + '\n')
    testID += 1

f1 = open("test.txt", "w", encoding="utf-8")
f1.writelines(newData)
f1.close()

