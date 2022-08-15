from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import datetime
import psycopg2
import sys

def main():
    api = ItsApi(user='user, password='password', host='127.0.0.1', port=1123)
    api.login()
    tags = api.get_tags()
    q=0

    while q!=1:
        PATH="C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.cwb.gov.tw/V8/E/W/Town/Town.html?TID=6800600")

        driver.find_element_by_xpath('//*[@id="Tab_24hrTable"]').click()
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, features='lxml')
        driver.quit()
        
        conn = psycopg2.connect(
        database="its", user='itsuser', password='itsuser1123', host='127.0.0.1', port= '5432'
        )
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM logger_cwb ORDER BY _tsamp_""")
        query_results = cursor.fetchall()


        soup.find_all('td')
        soup.find_all(class_="GT_Time")
        cur_t=soup.find(class_="GT_Time")
        curdat=cur_t.text
        cur=soup.find("span", {"class": "tem-C is-active"})
        cur2=soup.find("span", {"class": "GT_T"})
        c_hum=soup.find("span", {"class": "GT_RH"})


        d1_date=soup.find("th",{"id":"PC1_D1"})
        d2_date=soup.find("th",{"id":"PC1_D2"})

        if d1_date is None:
            d1_date=d2_date
            
        if d2_date is None:
            d2_date=d1_date

        d1_str=str(d1_date.text)
        d1_str_date=d1_str[0:-6]

        d2_str=str(d2_date.text)
        d2_str_date=d2_str[0:-6]

        d1_t=soup.find_all("th",{"headers":"PC1_Ti PC1_D1"})
   

        d2_t=soup.find_all("th",{"headers":"PC1_Ti PC1_D2"})
    
        table=soup.find_all('tr')
        table_body=table[16]
        hum_table=table[19]
        rows = table_body.find_all('td')

        hum_row=hum_table.find_all('td')
        j=0
        now = datetime.datetime.now()
        min1 = datetime.timedelta(minutes=1)
        for i in range(len(d1_t)):
            c1=d1_str_date+' '+d1_t[i].string
            
            temp=rows[j].text[0:2]
            hum=hum_row[j].text[0:2]
            if(temp=='--'):            
                temp=None
            
            if(hum=='-%'):
                hum=None
            month=int(c1[0:2])
            day=int(c1[3:5])
            hour=int(c1[6:8])
            minu=int(c1[9:11])
            
            year = now.strftime("%Y")
            dt=datetime.datetime(int(year),int(month),int(day),int(hour),int(minu))
        
            print(dt)
            print(temp)
            print(hum)
            min_dt=dt-min1
            max_dt=dt+min1
            cursor.execute('''UPDATE logger_cwb
                            SET temp = %s,hum=%s
                            WHERE _tsamp_>= %s and _tsamp_<=%s;''',[temp,hum,min_dt,max_dt])
            
            conn.commit()
            j+=1

        for i in range(len(d2_t)):
            c2=d2_str_date+' '+d2_t[i].string
            temp=rows[j].text[0:2]
            hum=hum_row[j].text[0:2]
            if(temp=='--'):
                temp=None
            if(hum=='-%'):
                hum=None
            month=int(c2[0:2])
            day=int(c2[3:5])
            hour=int(c2[6:8])
            minu=int(c2[9:11])
            
            year = now.strftime("%Y")
            dt=datetime.datetime(int(year),int(month),int(day),int(hour),int(minu))
    
            min_dt=dt-min1
            max_dt=dt+min1
            cursor.execute('''UPDATE logger_cwb
                            SET temp = %s,hum=%s
                            WHERE _tsamp_>= %s and _tsamp_<=%s;''',[temp,hum,min_dt,max_dt])
            conn.commit()
            j+=1
            
        month=int(curdat[0:2])
        day=int(curdat[3:5])
        hour=int(curdat[11:13])
        minu=int(curdat[14:16])    
        year = now.strftime("%Y")   
        dt=datetime.datetime(int(year),int(month),int(day),int(hour),int(minu))
        temp=cur.text 
        hum=c_hum.text[0:2]
        if(temp=='--'):
            temp=None
    
        if(hum=='-%'):
            hum=None
                 
        min_dt=dt-min1
        max_dt=dt+min1

        cursor.execute('''UPDATE logger_cwb
                            SET temp = %s,hum=%s
                            WHERE _tsamp_>= %s and _tsamp_<=%s;''',[temp,hum,min_dt,max_dt])
        conn.commit()


        cursor.close()     
        conn.close()
        api.logout()        
        time.sleep(2400)
        

if __name__ == '__main__':
    sys.path.append('../../lib')
    from itpt.ext.its_api import ItsApi   
    main()
