#Prerequisites - installed ssh, wget, java

#Config ssh:
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys

#Install Hadoop
# shellcheck disable=SC2164
cd ~
mkidr hadoop_tmp
cd hadoop_tmp/
wget http://apache.mirrors.tworzy.net/hadoop/common/hadoop-2.10.0/hadoop-2.10.0.tar.gz
tar xvzf hadoop-2.10.0.tar.gz
rm hadoop-2.10.0.tar.gz

sudo cp -r hadoop-2.10.0 /usr/local/
export PATH=$PATH:/usr/local/hadoop-2.10.0/bin
export PATH=$PATH:/usr/local/hadoop-2.10.0/sbin


#Config Hadoop
sudo cp files/hadoop/ /usr/local/hadoop-2.10.0/etc/hadoop/

hdfs namenode -format

#Starting Hadoop
start-dfs.sh
start-yarn.sh
mr-jobhistory-daemon.sh start historyserver

#Stoping Hadoop
mr-jobhistory-daemon.sh stop historyserver
stop-yarn.sh
stop-dfs.sh


hadoop jar /usr/local/hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar -mapper "python /home/michal/PycharmProjects/hadoop_project/src/term_frequency/mapper.py" -reducer "python /home/michal/PycharmProjects/hadoop_project/src/term_frequency/reducer.py" -input "/topics/corpora_test/partition=0/" -output "/outputs/test/"

hadoop jar /usr/local/hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar \
  -libjars ~/avro-mapred-1.9.1.jar \
  -mapper "python3.7 /home/michal/PycharmProjects/hadoop_project/src/term_frequency/mapper.py" \
  -reducer "python3.7 /home/michal/PycharmProjects/hadoop_project/src/term_frequency/reducer.py" \
  -input "/topics/corpuses/partition=0/" \
  -output "/outputs/test29/" \
  -inputformat org.apache.avro.mapred.AvroAsTextInputFormat