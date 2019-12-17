运行方法：
1. 安装好hadoop环境后clone 该项目到hadoop安装目录
2. 保证${Hadoop home}/hadoop/bin 添加到了你的环境变量里
3. 修改MapReduce_code文件夹中的 train.sh 和 predict.sh里跟你本机不同的路径
4. sh MapReduce_code/run.sh
5. 结果存于MapReduce_code/final_result.txt
6. 注意了，因为权限问题，所以sh文件可能要自己新建，要我拷贝我提供的sh文件里的命令进去即可
