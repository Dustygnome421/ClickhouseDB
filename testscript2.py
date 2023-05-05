import clickhouse_driver
from clickhouse_driver import Client

client = Client(host='localhost')


client.execute('CREATE TABLE IF NOT EXISTS test_table_mt (id Int32, name String) ENGINE = MergeTree() ORDER BY id')

data = [(1, 'John'), (2, 'Doe')]
query = 'INSERT INTO test_table_mt (id, name) VALUES'

client.execute(query, data)

result = client.execute('SELECT * FROM test_table_mt')
print(result)

# client.execute('INSERT INTO test_table_mt (id, name) VALUES', [(1, 'John'), (2, 'Doe')])
# client.execute

# result = client.execute('SELECT * FROM test_table_mt')
# print(result)