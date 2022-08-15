import sys
import threading
from time import sleep
import time
#import schedule
#from datetime import datetime, timedelta
import os

def main():
    api = ItsApi(user='user', password='password', host='127.0.0.1', port=1123)
    api.login()
    tags = api.get_tags()

    #start = datetime.now()
    #end = start + timedelta(seconds=24)
    #end = start + timedelta(hours=24) 
    device_list=["A","C","F"]
    threads = []
    timeout = 3600
    start_time = time.time()
    rest=0
    time_counter=1
    CYCLE_ON="CYCLE_ON"
    CYCLE_OFF="CYCLE_OFF"
    #start_hour=tags[CYCLE_ON]*3600
    #rest_hour=tags[CYCLE_OFF]*3600
    sys_motor="SYS_CYCLE"
    #global q
    MOTOR_SWITCH="CIRCULATOR_PUMP"
    recharge="WATER_RECHARGE"
    print("this is a main\n")
    def water_input(device):
        on_tag=device+"_WATER_SWITCH_ON"
        off_tag=device+"_WATER_SWITCH_OFF"
        water_tag=device+"_WATER"
        water_max=device+"_WATER_MAX"
        switch_tag=device+"_SWITCH"
        tags=api.get_tags()
        #api.set_tags({water_tag:0}) 
        #global q
        if tags[water_tag] <= tags[water_max] and tags[switch_tag]==1:
            print("send",device, "_water tag on to its....")
            tags = api.get_tags()
            api.set_tags({on_tag:1})
            sleep(11)
            api.set_tags({on_tag:0})
            while tags[water_tag] <= tags[water_max] and time.time() < start_time + timeout:
                #api.set_tags({water_tag:tags[water_tag]+1})
                tags = api.get_tags()
                #q=0
                if tags[MOTOR_SWITCH]==1:
                    print("send all water tag OFF to its before quit....,")
                    api.set_tags({off_tag:1})
                    sleep(11)
                    api.set_tags({off_tag:0})
                    #schedule.clear()
                    sleep(5)
                    api.logout()
                    sys.exit()
                print(tags[water_tag])
                sleep(1)
               
            
            print("send",device,"_water tag OFF to its...\n")
            api.set_tags({off_tag:1})
            sleep(11)
            api.set_tags({off_tag:0})


    
    

    print("rest=",rest)    
    while rest==0: 
        if rest==0:
            #tags = api.get_tags()
            start_hour=int(tags[CYCLE_ON]*12)
            print("\nset motor tag= 0(on) to its")
            api.set_tags({sys_motor:0})
            for i in range(start_hour):
                print("rest=",rest)   
                tags = api.get_tags()
                if tags[MOTOR_SWITCH]==1:
                    print("send motor off to its...")
                    api.set_tags({sys_motor:1})
                    print("motor exit") 
                    #schedule.clear()
                    api.logout()
                    sys.exit()
                                      
                #if datetime.now() > end:
                    #print("\nset motor tag= 1(off) to its before restarting again...")
                    #api.set_tags({sys_motor:1})
                    #rest=0                    
                    #main()
                    #schedule.every(1).seconds.do(main) 
                    #return schedule.CancelJob
                if tags[recharge]==1:
                    api.set_tags({sys_motor:1})
                    initial_sleep=360 #30 min sleep part
                    for i in range(initial_sleep):
                        sleep(5)
                        print(time_counter)
                        print("sleep hour")
                        time_counter+=1
                        #q=0
                        tags = api.get_tags()
                        if tags[MOTOR_SWITCH]==1:
                            print("program exit....")
                            #schedule.clear()
                            api.logout()
                            sys.exit()
    
                    for device in device_list:      
                        t = threading.Thread(target=water_input, args=(device))
                        threads.append(t)        
                        t.start()
                
                    for t in threads:
                        t.join()
                    api.set_tags({recharge:0})
                    rest=0
                    api.logout()
                    main()
                print(time_counter)
                print("motor is running...")
                #print("set tag: 0")
                rest=1
                time_counter+=1
                #q=0
                sleep(5)

        
        if rest==1:
            #tags = api.get_tags()
            rest_hour=int(tags[CYCLE_OFF]*12)
            print("\n set motor tag= 1(off) to its")
            api.set_tags({sys_motor:1})
            for i in range(rest_hour):
                print("rest=",rest)
                tags = api.get_tags()
                if tags[MOTOR_SWITCH]==1:                    
                    print("motor exit") 
                    #schedule.clear()
                    api.logout()
                    sys.exit()
                    
                #if datetime.now() > end:
                    #rest=0
                    #main()
                    #schedule.every(1).seconds.do(main) 
                    #return schedule.CancelJob
                if tags[recharge]==1:
                    #api.set_tags({sys_motor:1})
                    initial_sleep=360 #30 min sleep part
                    for i in range(initial_sleep):
                        sleep(5)
                        print(time_counter)
                        print("sleep hour")
                        time_counter+=1
                        #q=0
                        tags = api.get_tags()
                        if tags[MOTOR_SWITCH]==1:
                            print("program exit....")
                            #schedule.clear()
                            api.logout()
                            sys.exit()
    
                    for device in device_list:      
                        t = threading.Thread(target=water_input, args=(device))
                        threads.append(t)        
                        t.start()
                
                    for t in threads:
                        t.join()
                    api.set_tags({recharge:0})
                    rest=0
                    api.logout()
                    main()
                    
                rest=0
                print(time_counter)
                print("motor is resting...")
                time_counter+=1
                #q=0
                sleep(5)
    api.logout()
        
'''    
q=0
schedule.clear()
schedule.every(1).seconds.do(main) 
while 1:
    schedule.run_pending()
    time.sleep(1)
'''

if __name__ == '__main__':
    sys.path.append('../../lib')
    from itpt.ext.its_api import ItsApi
    main()
