# # 右键执行该文件，下面环境合理
from celery_task.tasks import add, low
#
# # 往celery的Broker中添加立即任务
# add.delay(10, 20)



# 添加延迟任务
# args是jump任务需要的参数，没有就设置为空()
# eta是该任务执行的UTC格式的时间
from datetime import datetime, timedelta


#秒
def eta_second(second):
    #获取当前时间
    ctime = datetime.now()
    #当前时间转化为UTC格式的时间
    utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
    print(utc_ctime.__class__)
    #把秒转化为可以相加的时间
    time_delay = timedelta(seconds=second)
    print(time_delay.__class__)
    #返回执行的时间
    return utc_ctime + time_delay


#天
def eta_days(days):
    ctime = datetime.now()
    utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
    time_delay = timedelta(days=days)
    return utc_ctime + time_delay

# apply_async就是添加延迟任务
low.apply_async(args=(200, 50), eta=eta_second(10))


