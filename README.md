# Naive_Bayesian_Classifier_MapReduce
A naive bayesian classifier for bug label classification in github issues written in python3 used MapReduce model.

#### Dependence

```shell
1. Vmware and Ubuntu (optional):
				https://pan.baidu.com/s/1X29KTBNUx71GcqLc9aGB1Q    提取码：a9d5
2. jdk1.8: 
				https://pan.baidu.com/s/1X29KTBNUx71GcqLc9aGB1Q    提取码：a9d5
3. hadoop2.6.0:
				https://pan.baidu.com/s/1ug00xUXIIvN_zyrXsRVnSw    提取码：64kb				
```

Our code run on three virtual machine as an example, if you don't have enough real meachine or you don't know how to install hadoop, you can follow our [environment setting](./Environment%20Setting)



#### Dataset

The data are crawled from the [Microsoft vscode project issues](https://github.com/microsoft/vscode/issues) .The original data can be found at [ori_data](./ori_data). 

We aim to predict the label (bug tag) of the issues' titles.

Then we change it into MapReduce's input format as follow:

```shell
label \t\t title
```

We removed some data whose label appeared less than 10 times. Then we got 1935 titles for train and 850 titles for validate.



#### Run

* Clone the git to your ${Hadoop home}
* Add ${Hadoop home}/hadoop/bin to your environment path.
* Modify the path in MapReduce_code/train.sh、predict.sh
* `cd MapReduce_code`
* `sh run.sh` 
* The result can be seen in `final_result.txt`
* Attention：you may need to create the sh file by yourself  due to the permission problem 



#### Result

| Evaluation method | Result |
| :---------------: | :----: |
|  rank1-Accuracy   | 31.8%  |
|  rank5-Accuracy   | 73.6%  |

