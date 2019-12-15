hdfs dfs -rm -r /input
hdfs dfs -rm -r /output
hdfs dfs -mkdir /input
hdfs dfs -put /usr/local/hadoop/Naive_Bayesian_Classifier_MapReduce/data/train.txt /input
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-mapper 'python3 train_mapper.py' -file /usr/local/hadoop/Naive_Bayesian_Classifier_MapReduce/MapReduce_code/train_mapper.py \
-reducer 'python3 train_reducer.py' -file /usr/local/hadoop/Naive_Bayesian_Classifier_MapReduce/MapReduce_code/train_reducer.py \
-input /input \
-output /output
rm -rf trainoutput.txt
hdfs dfs -cat /output/* >> trainoutput.txt
