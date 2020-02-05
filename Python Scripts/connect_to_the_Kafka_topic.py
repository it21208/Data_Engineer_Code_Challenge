# !/usr/bin/python
# -*- coding:utf-8 -*-
# author = Alexandros Ioannidis

import math, random
import argparse
import logging
import time
import sys
import os
from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka import TopicPartition
import json


def create_producer(bootstrap_servers, topicName):
    # try to create kafka producer
    try:
        # setting configuration to create a kafka producer.
        producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
        producer = KafkaProducer()

        #  start sending messages to this topic
        ack = producer.send(topicName, b'Hey there!')
        metadata = ack.get()
        print(metadata.topic)
        print(metadata.partition)

        # in case I need to change its serialization format  
        #producer = KafkaProducer(bootstrap_servers = bootstrap_servers, retries = 5,value_serializer=lambda m: json.dumps(m).encode('ascii'))

        '''
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        producer.send(topicName, b'Hey There!')
        producer.send(topicName, key=b'message-two', value=b'This is the producer')
        '''
    except Exception as e:
        print(e)

    return(None)



def create_consumer(bootstrap_servers, topicName, json_files_dir):

    list_of_Classifieds_ids = []

    # method that checks for duplicate records
    def check_for_duplicates(id, list_of_Classifieds_ids):
        if id in list_of_Classifieds_ids:
            print('Duplicate record')
            temp_boolean = True
        else:
            list_of_Classifieds_ids.append(id)
            temp_boolean = False
        return(temp_boolean)


    def writeJson(data, classified_id_str, json_files_dir):
        with open(json_files_dir+classified_id_str+'.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    try:
        consumer = KafkaConsumer(topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')
        '''
        > My understanding of the group1 variable is that this will instruct the code to continue from the place it stopped
        because it will just fetch the stored offset from the offset storage.
        > The earliest option automatically resets the offset to the earliest offset from what I understood in a previous version it used 
        to be called smallest.
        '''
        try:
            for message in consumer:
                #print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key,message.value))
                #print(
                # type(message.value), message.value)
                temp_decoded = (message.value).decode("utf-8")
                #print(type(temp_decoded), temp_decoded)
                ''' convert json string into dictionary '''
                temp_json_dict = json.loads(temp_decoded)
                #print(type(temp_json_dict), temp_json_dict)
                
                ''' check if classified received is duplicate'''
                flag = check_for_duplicates(temp_json_dict['id'], list_of_Classifieds_ids)

                ''' if it's not duplicate it proceeds with saving the json file - the name of the file saved is the classified id string '''
                if flag == False:
                    writeJson(temp_json_dict, temp_json_dict['id'], json_files_dir)
                    print('Saved '+ temp_json_dict['id'] +'.json file')

            
            '''
            #manually assign the partition list for the consumer
            consumer.assign([TopicPartition('data', 1)])
            msg = next(consumer)
            '''
            
            # close the consumer and commit the offset if needed
            #consumer.close()

        except KeyboardInterrupt:
            sys.exit()

    except Exception as e:

        print(e)
    
    return(None)



def main(json_files_dir):
    bootstrap_servers = ['15.188.227.171:9092']
    topicName = 'data'
    ''' call the producer ''' 
    #create_producer(bootstrap_servers, topicName)
    ''' call the consumer '''
    create_consumer(bootstrap_servers, topicName, json_files_dir)


if __name__== "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S ')
    start_time = time.time()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--projDir", '-p', type=str, help='directory path to project', required=True)

    # argument parse
    args = parser.parse_args()
    projDir = args.projDir
    
    # concatenate certain strings to form the right directory paths
    json_files_dir = os.path.join(projDir, 'json_files/')

    main(json_files_dir)

    logging.info(f'Run finished in {time.time() - start_time} seconds')
