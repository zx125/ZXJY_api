from celery import Celery

# broker：任务仓库
broker = 'redis://127.0.0.1:6379/5'
# backend：任务结果仓库
backend = 'redis://127.0.0.1:6379/6'
# include：任务(函数)所在文件
app = Celery(broker=broker, backend=backend, include=['celery_task.tasks'])


# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False

# 自动任务的定时配置
from celery.schedules import crontab
from datetime import timedelta
app.conf.beat_schedule = {
    # 定时任务：任务名自定义
    'fall_task': {
        'task': 'celery_task.tasks.low',  # 任务源
        'args': (30, 10),  # 任务参数s
        'schedule': timedelta(seconds=3) # 定时添加任务的时间
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
    }
}