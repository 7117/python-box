import calendar
import time
# 时间
t = time.time()
print(t)
# 本地时间
t1 = time.localtime(t)
print(t1)
# 格式化
t2 = time.asctime(t1)
print(t2)
# 时间格式化
t3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(t3)
t4 = time.strptime(t3,"%Y-%m-%d %H:%M:%S")
print(t4)
cal = calendar.month(2020,1)
print(cal)
# 休息
time.sleep(2)
print("sleep")