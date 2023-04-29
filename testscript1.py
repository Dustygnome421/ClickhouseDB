#  we want to test the performance of the MergeTree and GraphiteMergeTree ClickhouseDB engines 
# for storing and querying time-series data.

# In this case, we'll measure the insert speed and query performance of each engine.

# We'll use the Python client library to write our test script. 
# First, we'll create a database and tables for each engine:

from IoTdata import generate_data
from clickhouse_driver import Client

client = Client(host='localhost')

client.execute('CREATE DATABASE IF NOT EXISTS test')

client.execute('CREATE TABLE IF NOT EXISTS test.merge_tree (device_id UInt32, timestamp DateTime, value UInt32) ENGINE = MergeTree ORDER BY (device_id, timestamp)')
client.execute('CREATE TABLE IF NOT EXISTS test.graphite_merge_tree (device_id UInt32, timestamp DateTime, value UInt32) ENGINE = GraphiteMergeTree(\'graphite_rollup_rules.txt\') ORDER BY (device_id, timestamp)')

# data = generate_data(1000)

# # Next, we'll write a function to insert data into each engine and measure input speed:

# import time

# start_time = time.time()
# client.execute('INSERT INTO test.merge_tree (device_id, timestamp, value) VALUES', data)
# end_time = time.time()
# merge_tree_insert_time = end_time - start_time

# start_time = time.time()
# client.execute('INSERT INTO test.graphite_merge_tree (device_id, timestamp, value) VALUES', data)
# end_time = time.time()
# graphite_merge_tree_insert_time = end_time - start_time

# print(f"MergeTree insert time: {merge_tree_insert_time}")
# print(f"GraphiteMergeTree insert time: {graphite_merge_tree_insert_time}")

# # Finally, we'll write a function to query data from each engine and measure query performance:

# start_time = time.time()
# result = client.execute('SELECT device_id, sum(value) FROM test.merge_tree GROUP BY device_id')
# end_time = time.time()
# merge_tree_query_time = end_time - start_time

# start_time = time.time()
# result = client.execute('SELECT device_id, sum(value) FROM test.graphite_merge_tree GROUP BY device_id')
# end_time = time.time()
# graphite_merge_tree_query_time = end_time - start_time

# print(f"MergeTree query time: {merge_tree_query_time}")
# print(f"GraphiteMergeTree query time: {graphite_merge_tree_query_time}")

# # Now, we can run our test script and compare the results:
