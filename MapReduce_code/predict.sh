rm -rf test.txt
python3 prepare_predictdata.py
hdfs dfs -rm -r /predict_input
hdfs dfs -rm -r /middle_output
hdfs dfs -mkdir /predict_input
hdfs dfs -put /usr/local/hadoop/Naive_Bayesian_Classifier_MapReduce/MapReduce_code/test.txt /predict_input
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-mapper 'python3 predict_mapper1.py' -file /usr/local/hadoop/Naive_Bayesian_Classifier_MapReduce/MapReduce_code/predict_mapper1.py \
-reducer 'python3 predict_reducer1.py' -file /usr/local/hadoop/Naive_Bayesian_Classifier_MapReduce/MapReduce_code/predict_reducer1.py \
-input /predict_input \
-output /middle_output

rm -rf middle_output.txt
hdfs dfs -cat /middle_output/* >> middle_output.txt
hdfs dfs -rm -r /predict_input2
hdfs dfs -rm -r /predict_result
hdfs dfs -mkdir /predict_input2
hdfs dfs -put /usr/local/hadoop/Naive_Bayesian_Classifier_MapReduce/MapReduce_code/middle_output.txt /predict_input2
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-mapper 'python3 predict_mapper2.py' -file /usr/local/hadoop/Naive_Bayesian_Classifier_MapReduce/MapReduce_code/predict_mapper2.py \
-reducer 'python3 predict_reducer2.py' -file /usr/local/hadoop/Naive_Bayesian_Classifier_MapReduce/MapReduce_code/predict_reducer2.py \
-input /predict_input2 \
-output /predict_result
rm -rf result.txt
rm -rf predict_result.txt
hdfs dfs -cat /predict_result/* >> predict_result.txt

