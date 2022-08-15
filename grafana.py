import psycopg2
import pandas as pd
import sys
import time
from sqlalchemy2 import create_engine
import io

def main():
    api = ItsApi(user='event', password='event', host='host', port=1123)
    api.login()#登入
    tags = api.get_tags()


    q=0
    while q!=1:
        conn = psycopg2.connect(
            database="database", user='user', password='password', host='host', port= '5432'
        )

        cur = conn.cursor()
        cur.execute("""SELECT * FROM logger_ekoral WHERE _tsamp_ >= NOW()::date - INTERVAL '4 DAY';""")
        query_results = cur.fetchall()


        df = pd.DataFrame(list(query_results),columns=["id","ak3ikdf123_ph","ak3ikdf126_ph","ak3ikdf105_ph","ak6iodf101_ec","ak6iodf087_ec","ak6iodf095_ec","ak6iodf086_ec","ak6Iodf132_ec","ak3ikdf115_ph","ak6iodf103_ec","ak3ikdf143_ph","ak3ikdf121_ph","ak3ikdf151_ph","AK6IoDF099_ec","ak6iodf042_ec","ak3ikdf132_ph","_tsamp_"])
        df['_tsamp_'] = pd.to_datetime(df['_tsamp_'])


        loc_time = df['_tsamp_'].dt.tz_localize('Asia/Taipei')
        loc_time=loc_time.to_frame()
        df.drop(['_tsamp_'], axis=1, inplace=True)

        loc_time_change = df.join(loc_time)


        engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/suppliers')

        loc_time_change.head(0).to_sql('yumiao', engine, if_exists='replace',index=False) #drops old table and creates new empty table

        conn2 = engine.raw_connection()
        cur2 = conn2.cursor()
        output = io.StringIO()
        loc_time_change.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        contents = output.getvalue()
        cur2.copy_from(output, 'yumiao', null="")
        conn2.commit()
        cur2.close()

        cur.execute("""SELECT * FROM logger_ekoral_temp WHERE _tsamp_ >= NOW()::date - INTERVAL '4 DAY';""")
        query_results = cur.fetchall()
        

        df = pd.DataFrame(list(query_results),columns=["id","ak6iodf101_temp","ak6iodf087_temp","ak6iodf095_temp","ak6iodf086_temp","ak6Iodf132_temp","ak3ikdf123_temp","ak3ikdf143_temp","ak3ikdf121_temp","_tsamp_"])
        df['_tsamp_'] = pd.to_datetime(df['_tsamp_'])


        loc_time = df['_tsamp_'].dt.tz_localize('Asia/Taipei')
        loc_time=loc_time.to_frame()
        df.drop(['_tsamp_'], axis=1, inplace=True)

        loc_time_change = df.join(loc_time)


        engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/suppliers')

        loc_time_change.head(0).to_sql('yumiao_temp', engine, if_exists='replace',index=False) #drops old table and creates new empty table

        conn2 = engine.raw_connection()
        cur2 = conn2.cursor()
        output = io.StringIO()
        loc_time_change.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        contents = output.getvalue()
        cur2.copy_from(output, 'yumiao_temp', null="") # null values become ''
        conn2.commit()
        cur2.close()
        print("ok2")


        cur.execute("""SELECT * FROM logger_l_環境 WHERE _tsamp_ >= NOW()::date - INTERVAL '4 DAY';""")
        query_results = cur.fetchall()

        df = pd.DataFrame(list(query_results),columns=["id","育苗室CO2","育苗室溫度","育苗室濕度","_tsamp_"])
        df['_tsamp_'] = pd.to_datetime(df['_tsamp_'])

        loc_time = df['_tsamp_'].dt.tz_localize('Asia/Taipei')
        loc_time=loc_time.to_frame()
        df.drop(['_tsamp_'], axis=1, inplace=True)

        loc_time_change = df.join(loc_time)

        engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/suppliers')

        loc_time_change.head(0).to_sql('yumiao_environment', engine, if_exists='replace',index=False) #drops old table and creates new empty table
        conn2 = engine.raw_connection()
        cur2 = conn2.cursor()
        output = io.StringIO()
        loc_time_change.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        contents = output.getvalue()
        cur2.copy_from(output, 'yumiao_environment', null="") # null values become ''
        conn2.commit()
        cur2.close()
        print("ok3")


        cur.execute("""SELECT * FROM logger_ekoral_greenhouse WHERE _tsamp_ >= NOW()::date - INTERVAL '4 DAY';""")
        query_results = cur.fetchall()

        df = pd.DataFrame(list(query_results),columns=["id","ak3ikdf146_temp","ak3ikdf165_temp","ak3ikdf157_temp","ajbiadc001_ph","ak3ikdf098_temp","ak3ikdf093_temp","ak3ikdf155_temp","ak3ikdf146_ph","ak3ikdf165_ph","ak3ikdf157_ph","ak3ikdf098_ph","ak3ikdf093_ph","ak3ikdf155_ph","ak6iodf089_ec","ak6iodf107_ec","ak6iodf124_ec","ak6iodf106_ec","ak6iodf109_ec","ajbiadc001_ec","ajbiadc001_temp","ak6iodf110_ec","_tsamp_"])
        df['_tsamp_'] = pd.to_datetime(df['_tsamp_'])

        loc_time = df['_tsamp_'].dt.tz_localize('Asia/Taipei')
        loc_time=loc_time.to_frame()
        df.drop(['_tsamp_'], axis=1, inplace=True)

        loc_time_change = df.join(loc_time)

        engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/suppliers')

        loc_time_change.head(0).to_sql('greenhouse', engine, if_exists='replace',index=False) #drops old table and creates new empty table

        conn2 = engine.raw_connection()
        cur2 = conn2.cursor()
        output = io.StringIO()
        loc_time_change.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        contents = output.getvalue()
        cur2.copy_from(output, 'greenhouse', null="") # null values become ''
        conn2.commit()
        cur2.close()
        print("ok4")


        cur.execute("""SELECT id, 育苗1_水位, 疏苗1_水位, 疏苗4_水位, _tsamp_ FROM logger_l_水位 WHERE _tsamp_ >= NOW()::date - INTERVAL '4 DAY';""")
        query_results = cur.fetchall()

        df = pd.DataFrame(list(query_results),columns=["id","育苗1_水位","疏苗1_水位","疏苗4_水位","_tsamp_"])
        df['_tsamp_'] = pd.to_datetime(df['_tsamp_'])


        loc_time = df['_tsamp_'].dt.tz_localize('Asia/Taipei')
        loc_time=loc_time.to_frame()
        df.drop(['_tsamp_'], axis=1, inplace=True)

        loc_time_change = df.join(loc_time)

        engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/suppliers')

        loc_time_change.head(0).to_sql('water_level', engine, if_exists='replace',index=False) #drops old table and creates new empty table

        conn2 = engine.raw_connection()
        cur2 = conn2.cursor()
        output = io.StringIO()
        loc_time_change.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        contents = output.getvalue()
        cur2.copy_from(output, 'water_level', null="") # null values become ''
        conn2.commit()
        cur2.close()
        print("ok5")


        cur.execute("""SELECT * FROM logger_l_溫室環境 WHERE _tsamp_ >= NOW()::date - INTERVAL '4 DAY';""")
        query_results = cur.fetchall()

        df = pd.DataFrame(list(query_results),columns=["id","環境站6_濕度","環境站5_濕度","環境站1_光照","環境站2_光照","環境站2_溫度","環境站3_溫度","環境站4_溫度","環境站5_溫度","環境站6_溫度","環境站3_光照","環境站4_光照","環境站5_光照","環境站6_光照","環境站1_溫度","環境站2_濕度","環境站3_濕度","環境站4_濕度","環境站1_濕度","_tsamp_"])
        df['_tsamp_'] = pd.to_datetime(df['_tsamp_'])

        loc_time = df['_tsamp_'].dt.tz_localize('Asia/Taipei')
        loc_time=loc_time.to_frame()
        df.drop(['_tsamp_'], axis=1, inplace=True)

        loc_time_change = df.join(loc_time)


        engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/suppliers')

        loc_time_change.head(0).to_sql('greenhouse_environment', engine, if_exists='replace',index=False) #drops old table and creates new empty table

        conn2 = engine.raw_connection()
        cur2 = conn2.cursor()
        output = io.StringIO()
        loc_time_change.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        contents = output.getvalue()
        cur2.copy_from(output, 'greenhouse_environment', null="") # null values become ''
        conn2.commit()
        cur2.close()
        print("ok6")
        
        
        cur.execute("""select id, hum,temp,_tsamp_ from logger_cwb 
                        where temp is not null and hum is not null
                        and _tsamp_ >= NOW()::date - INTERVAL '4 DAY';""")
        query_results = cur.fetchall()

        df = pd.DataFrame(list(query_results),columns=["id","hum","temp","_tsamp_"])
        df['_tsamp_'] = pd.to_datetime(df['_tsamp_'])

        loc_time = df['_tsamp_'].dt.tz_localize('Asia/Taipei')
        loc_time=loc_time.to_frame()
        df.drop(['_tsamp_'], axis=1, inplace=True)

        loc_time_change = df.join(loc_time)


        engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/suppliers')

        loc_time_change.head(0).to_sql('cwb', engine, if_exists='replace',index=False) #drops old table and creates new empty table

        conn2 = engine.raw_connection()
        cur2 = conn2.cursor()
        output = io.StringIO()
        loc_time_change.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        contents = output.getvalue()
        cur2.copy_from(output, 'cwb', null="")
        conn2.commit()
        cur2.close()
        print("ok7")
        
        
        cur.close()
        conn.close() 
        time.sleep(300)
   
if __name__ == '__main__':
    sys.path.append('../../lib')
    #sys.path.append('../pgsql/py_lib')
    from itpt.ext.its_api import ItsApi
    #from itpt.core.db import DBConnector
    main()