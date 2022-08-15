import sys
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

import datetime
from dateutil import tz
import psycopg2


def main():
    api = ItsApi(user='user', password='password', host='127.0.0.1', port=1123)
    api.login()#登入
    tags = api.get_tags()

    bucket = "goodjin"
    org = "goodjin"
    token = "LLMRypH-bAQtIU7WjaNo7P7MjI2FvUxZ0yYM5A4fHwAp2w8d6wWJ8nazftEzzwrLcLFZ5U_88pfgXxE6fg7Ehw=="
    #token="7-2UJMJU5Wc235rG6F3LqEU2S2tFQ5HCl_OysRo2D3O4DlwZTKFUL5bhe_rOwEB6O7Iug5kEX5Nn5taC3fzFcQ=="
    # Store the URL of your InfluxDB instance
    url="http://localhost:8086"

    client = influxdb_client.InfluxDBClient(
      url=url,
      token=token,
      org=org
    )

    query_api = client.query_api()
    to_zone = tz.gettz('Asia/Taipei')
    to_zone = tz.tzlocal()

    conn = psycopg2.connect(
            database="database", user='user', password='password', host='127.0.0.1', port= '5432'
            )
    cursor=conn.cursor()
   
    print("A6.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK6IoDF089")\
    |> filter(fn: (r) => r.value_type == "ec")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak6iodf089_ec = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    api.set_tags({'ec_g089':ph})
    
    print("A5.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK6IoDF107")\
    |> filter(fn: (r) => r.value_type == "ec")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak6iodf107_ec = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    api.set_tags({'ec_g107':ph})
    
    print("A4.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK6IoDF124")\
    |> filter(fn: (r) => r.value_type == "ec")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak6iodf124_ec = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    api.set_tags({'ec_g124':ph})

    print("A3.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK6IoDF110")\
    |> filter(fn: (r) => r.value_type == "ec")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak6iodf110_ec = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ec_g110':ph})
    
    print("A2.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK6IoDF106")\
    |> filter(fn: (r) => r.value_type == "ec")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak6iodf106_ec = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ec_g106':ph})
    
    print("A1.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK6IoDF109")\
    |> filter(fn: (r) => r.value_type == "ec")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak6iodf109_ec = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ec_g109':ph})
            
    
    print("(B4)菜盤4合一ec....")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AJbIaDC001")\
    |> filter(fn: (r) => r.value_type == "ec")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))

    #print(results)
    min1 = datetime.timedelta(minutes=1)

    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ajbiadc001_ec = %s
                      WHERE _tsamp_> %s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ec_g001':ph})
    
    print("A6.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF146")\
    |> filter(fn: (r) => r.value_type == "ph")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf146_ph = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ph_g146':ph}) 
    
    print("A5.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF165")\
    |> filter(fn: (r) => r.value_type == "ph")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf165_ph = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ph_g165':ph})
    
    print("A4.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF157")\
    |> filter(fn: (r) => r.value_type == "ph")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf157_ph = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ph_g157':ph})
    
    print("A3.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF098")\
    |> filter(fn: (r) => r.value_type == "ph")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf098_ph = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ph_g098':ph})
    
    print("A2.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF093")\
    |> filter(fn: (r) => r.value_type == "ph")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf093_ph = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ph_g093':ph})
    
    print("A1.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF155")\
    |> filter(fn: (r) => r.value_type == "ph")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf155_ph = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'ph_g155':ph}) 
    
    print("(B4)菜盤4合一ph....")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AJbIaDC001")\
    |> filter(fn: (r) => r.value_type == "ph")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))

    #print(results)
    min1 = datetime.timedelta(minutes=1)

    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ajbiadc001_ph = %s
                      WHERE _tsamp_> %s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    api.set_tags({'ph_g001':ph})


    print("A6_temp.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF146")\
    |> filter(fn: (r) => r.value_type == "temperature")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf146_temp = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'temp_g146':ph})
       
    print("A5temp.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF165")\
    |> filter(fn: (r) => r.value_type == "temperature")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf165_temp = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'temp_g165':ph})
    
    print("A4.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF157")\
    |> filter(fn: (r) => r.value_type == "temperature")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf157_temp = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
   
    api.set_tags({'temp_g157':ph})
    
    print("A3tem.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF098")\
    |> filter(fn: (r) => r.value_type == "temperature")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf098_temp = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'temp_g098':ph})
    
    print("A2.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF093")\
    |> filter(fn: (r) => r.value_type == "temperature")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf093_temp = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'temp_g093':ph})
    
    print("A1.......")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AK3IkDF155")\
    |> filter(fn: (r) => r.value_type == "temperature")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    min1 = datetime.timedelta(minutes=1)
    #min1 = datetime.timedelta(seconds=32)
    #min2 = datetime.timedelta(minutes=1)
    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ak3ikdf155_temp = %s
                      WHERE _tsamp_>%s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
    
    api.set_tags({'temp_g155':ph})
    
    print("(B4)菜盤4合一temp....")
    query = 'from(bucket:"goodjin")\
    |> range(start:-1d)\
    |> filter(fn:(r) => r._measurement == "sensor_reading")\
    |> filter(fn: (r) => r._field == "value")\
    |> filter(fn: (r) => r.device_sn == "AJbIaDC001")\
    |> filter(fn: (r) => r.value_type == "temperature")'

    result = query_api.query(org=org, query=query)

    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))

    #print(results)
    min1 = datetime.timedelta(minutes=1)

    for i in range(len(results)):
        lt=results[i][0]
        glt=lt.astimezone(to_zone)
        ph=results[i][1]
        min_glt=glt-min1
        max_glt=glt+min1
        print(glt)
        #print(min_glt)
        print(ph)
        
        cursor.execute('''UPDATE logger_ekoral_greenhouse
                      SET ajbiadc001_temp = %s
                      WHERE _tsamp_> %s and _tsamp_<=%s;''',[ph,min_glt,max_glt])
        conn.commit()
   
    api.set_tags({'temp_g001':ph})

    
    
    cursor.close()
    conn.close()
    api.logout()    

if __name__ == '__main__':
    sys.path.append('../../lib')
    #sys.path.append('../pgsql/py_lib')
    from itpt.ext.its_api import ItsApi
    #from itpt.core.db import DBConnector
    
    main()
