### XE-Data_Engineer_Code_Challenge

##### Author: Alexandros Ioannidis


### Description of tasks implemented
Users of a certain organisation front-facing site see the classifieds that are entered in the systems by their customers. When a customer creates a classified, the systems emit a record of it and publish it to a Kafka topic. 

- create an application that consumes these records, 
- record them in a MySQL database 
- and write a SQL script to analyse this information

In the Python Scripts folder you will find the following files:

> create_automatically_classified_records.py This script creates the application that consumes and saves non-duplicate records and it also records and outputs the total execution time. So the aspect of the "at least once delivery" strategy is handled. Furthermore, the issue of the application being stopped unexpectedly and the need for it to continue from where it left off is also tangled. I have commented my code in every step. I have also thrown a kafka producer but it has been commented out.

#### Important - How to run the application that consumes the records

Via terminal if you're using a linux flavour please go to the folder 'Python Scripts' of the project and execute the following command as explained below

```
python connect_to_the_Kafka_topic.py --projDir <<path to the root of this project directory>>
```

Please see an example below. 

```
python connect_to_the_Kafka_topic.py --projDir /home/alex/NetBeansProjects/XE/XE-Data_Engineer_Code_Challenge/
```
Note! You might have to pip install kafka if you haven't already. All the other imports are pretty standard.

In the 'Python Scripts' folder we can also find the script that records the consumed records in the MySQL database. 

> record_records_in_mysql_db.py

To execute the script you have to run the command below from inside the 'Python Scripts' folder. 

```
python record_records_in_mysql_db.py --projDir <<path to the root of this project directory>>
```

You may have to run the line below on your terminal before executing the script.

```
pip install mysql-connector-python
```

In the MySQL Scripts folder you will find the following files:

> create_table_Classifieds.sql is the mysql script which contains the commands I used to create the Classifieds table and insert some data etc.

> create_tables_Margins.sql is the mysql script which contains the commands I used to create the Margins tables and insert some data etc.

Having inserted some data in the previous tables I proceeded with the implementation of the events and procedures. 

> calculate_margin_over_time.sql is the mysql script that contains the commands I used to create the procedures for the calculation over time per
  ad_type and payment_type and the creation of the event to execute the procedures periodically.

### 
-----------------------------------------------
