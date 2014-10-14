#Source: http://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
#TODO: first check whether there's a hadoop program running
#TODO: decouple the start scripts, stop scripts, and test-case scripts

rm -Rf /tmp/hadoop-tianyin*
rm -Rf /tmp/yarn-tianyin*
rm -Rf /tmp/logs
rm -Rf /tmp/output

bin/hdfs namenode -format

#sleep 5

sbin/start-dfs.sh

sleep 15

bin/hdfs dfs -mkdir /user
bin/hdfs dfs -mkdir /user/tianyin

#sleep 5

bin/hdfs dfs -put etc/hadoop input

bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.4.1.jar grep input output 'dfs[a-z.]+'

sleep 10

bin/hdfs dfs -get output output
cat output/*

sbin/stop-dfs.sh
