# 右键执行该文件，下面环境合理
from celery_task.celery import app

from celery.result import AsyncResult

id = '016d69b1-f066-4817-85de-5b594f65ddc4'
if __name__ == '__main__':
    async = AsyncResult(id=id, app=app)
    if async.successful():
        result = async.get()
        print(result)
    elif async.failed():
        print('任务失败')
    elif async.status == 'PENDING':
        print('任务等待中被执行')
    elif async.status == 'RETRY':
        print('任务异常后正在重试')
    elif async.status == 'STARTED':
        print('任务已经开始被执行')