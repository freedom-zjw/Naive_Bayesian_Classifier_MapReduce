### Code Instructions

train_mapper.py + train_reducer.py:  

```
 <label title> -> <<label, Nei, word>, 1>  Nei is the number of titles whose bug tag is label
```

prepare_predictdata.py:  

```
change test data into correct format
```

predict_mapper1 + predict_reducer1:  

```
Input:		
	<<label>, <0, N, Nei, word, numofword>>  N is the total number of train titles
	<<label>, <1, testID, testtitle>>
Output:
	<<testID>, <label, p>>
```

predict_mapper2 + predict_reducer2:

```
Input:
	<<testID>, <label, p>>
Output:
	<<test_ID>,  <label1, label2, label3, label4, label5>> The top5 possible label
```

​				

