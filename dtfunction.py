import datetime as DT
import time
import schedule
def job():
    print("I'm working...")


schedule.every(1).minutes.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


while True:
    now = DT.datetime.now()
    target = DT.datetime.combine(DT.date.today(), DT.time(hour=1))
    if target < now:
        target += DT.timedelta(days=1)

    time.sleep((target-now).total_seconds())
#just to have breakpoint 
i = 0
print (i)


