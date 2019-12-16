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

Our code run on three virtual machine as an example, if you don't have enough real meachine or you don't know how to install hadoop, you can follow our [environment setting](./Environment Setting)



#### Dataset

The data are crawled from the [Microsoft vscode project issues](https://github.com/microsoft/vscode/issues) .The original data can be found at [ori_data](./ori_data). Then we change it into MapReduce input format as follow:

```shell
label \t\t title
```





#### Run

* Clone the git to your ${Hadoop home}
* Add ${Hadoop home}/hadoop/bin to your environment path.
* Modify the path in MapReduce_code/train.sh、predict.sh
* `cd MapReduce`
* `sh run.sh`
* The result can be seen in `final_result.txt`

