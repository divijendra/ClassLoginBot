from collections import namedtuple
from datetime import datetime
from datetime import timedelta
from non_epm import non_epm
from epm import epm
from tp import tp
import time
schedule = namedtuple("schedule", ["course_name", "link", "begn_time", "end_time"])


day = datetime.today().day
month = datetime.today().month
yr = datetime.today().year
classes = []
file = open("classes.csv", 'r')
lines = file.readlines()
file.close()
for line in lines:
    temp = line.split(",")
    btime = list(map(int, temp[-2].split(":")))
    etime = list(map(int, temp[-1].split(":")))
    classes.append(schedule(temp[0], temp[1], datetime(yr, month, day, btime[0], btime[1]), datetime(yr, month, day, etime[0], etime[1])))

i = 0
time_gap = timedelta(0)
while i < len(classes) and datetime.now() <= classes[-1].end_time:
    if classes[i].begn_time <= datetime.now() <= classes[i].end_time:
        print("Trying to attend {} class.".format(classes[i].course_name))
        cls_opened = tp(classes[i].link, classes[i].end_time)
        if cls_opened:
            print("Successfully attended {} class".format(classes[i].course_name))
        i += 1
    elif classes[i].end_time <= datetime.now():
        print("{} class ended at {}.".format(classes[i].course_name, classes[i].end_time.strftime("%H:%M")))
        i += 1
    elif classes[i].begn_time > datetime.now()+time_gap:
        time_gap = classes[i].begn_time - datetime.now()
        print("{} class has not started yet.I Will run the script again after {} hours {} minutes.".format(
            classes[i].course_name, int(time_gap.total_seconds()//3600), int((time_gap.total_seconds() % 3600)//60)))
        time.sleep(time_gap.total_seconds())


    '''elif classes[i].course_name == "TP" and classes[i].begn_time-timedelta(minutes=5) <= datetime.now() <= classes[i].end_time:
        print("Trying to attend TP class. Calling tp().")
        cls_opened = non_epm(classes[i].link, classes[i].end_time)
        if cls_opened:
            print("Successfully attended {} class".format(
                classes[i].course_name))
        i += 1'''