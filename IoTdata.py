import random
import datetime

#Prepare your test data: We'll generate sample time-series data 
#to simulate the data that an IoT device might send to a cloud service.

def generate_data(num_rows):
    data = []
    for i in range(num_rows):
        device_id = random.randint(1, 1000)
        timestamp = datetime.datetime.now() - datetime.timedelta(days=i)
        value = random.randint(0, 100)
        data.append((device_id, timestamp, value))
    return data


data = generate_data(1000)
print(data[:10])