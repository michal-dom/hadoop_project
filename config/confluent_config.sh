#Download file from https://www.confluent.io/download/?_ga=2.256640015.522527075.1576097616-762707822.1575878328
#e.g. file name is confluent-5.3.1-2.12.tar.gz
tar xvzf confluent-5.3.1-2.12.tar.gz
sudo mkdir /usr/local/confluent/
sudo cp -r confluent-5.3.1-2.12/* /usr/local/confluent/
rm -r confluent-5.3.1-2.12
rm confluent-5.3.1-2.12.tar.gz

#Configuration
curl -L https://cnfl.io/cli | sh -s -- -b /usr/local/confluent/bin
/usr/local/confluent/bin/confluent-hub install --no-prompt confluentinc/kafka-connect-datagen:latest

export PATH=$PATH:/usr/local/confluent/bin

#Starting Confuent
confluent local start

#Output:

# Starting zookeeper
# zookeeper is [UP]
# Starting kafka
# kafka is [UP]
# Starting schema-registry
# schema-registry is [UP]
# Starting kafka-rest
# kafka-rest is [UP]
# Starting connect
# connect is [UP]
# Starting ksql-server
# ksql-server is [UP]
# Starting control-center
# control-center is [UP]

#Stoping Confuent
confluent local stop