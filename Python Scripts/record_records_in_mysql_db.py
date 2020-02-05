# !/usr/bin/python
# -*- coding:utf-8 -*-
# author = Alexandros Ioannidis

import math, random
import argparse
import logging
import time
import sys
import os
import json
import mysql.connector
from mysql.connector import Error


def connectToMySQL():
    try:
        connection = mysql.connector.connect(host='aidataengineer.cg2t1fioak49.eu-west-3.rds.amazonaws.com',
                                         database='aidataengineer',
                                         user='root',
                                         password='XCZwFkMqcYpRtJnRQ4k2566hm3fU8Cn9')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    return(connection, cursor)
    

def close_MySQL_connection(connection, cursor):       
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    return(None)



def main(json_files_dir):
    # start MySQL connection to host
    connection, cursor = connectToMySQL()

    for file in os.listdir(json_files_dir):
        with open(json_files_dir+file,'r') as fi:
            dict_tmp = json.load(fi)
            
            try:
                cursor = connection.cursor()
                # check if the ad_type is Free or not Free because depending on this the mysql query needs to change for a different data insertion
                if dict_tmp['ad_type'] != "Free":
                    mySql_insert_query = """INSERT INTO Classifieds (id, customer_id, created_at, ad_text, ad_type, price, currency, payment_type, payment_cost) 
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
                    #print(dict_tmp['id'])
                    recordTuple = ( dict_tmp['id'], dict_tmp['customer_id'], dict_tmp['created_at'], dict_tmp['text'], dict_tmp['ad_type'], str(dict_tmp['price']), dict_tmp['currency'], dict_tmp['payment_type'], str(dict_tmp['payment_cost']) )
                # when the ad_type is Free the json file does not contain any more fields after the 'ad_type' field
                else:
                    mySql_insert_query = """INSERT INTO Classifieds (id, customer_id, created_at, ad_text, ad_type) 
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
                    #print(dict_tmp['id'])
                    recordTuple = ( dict_tmp['id'], dict_tmp['customer_id'], dict_tmp['created_at'], dict_tmp['text'], dict_tmp['ad_type'])
                
                cursor.execute(mySql_insert_query, recordTuple)
                connection.commit()
                print(cursor.rowcount, "Record with Classified id: "+ dict_tmp['id'] +" inserted successfully into Classifieds table")
             
            except mysql.connector.Error as error:
                print("Failed to insert record with Classified id: "+ dict_tmp['id'] +" into Classifieds table {}".format(error))
                pass
    
    # finally close MySQL connection
    close_MySQL_connection(connection, cursor)
    return(None)


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
