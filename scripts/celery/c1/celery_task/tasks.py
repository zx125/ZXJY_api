from .celery import app

@app.task
def add(n1, n2):
    res = n1 + n2
    print('n1 + n2 = %s' % res)
    return res

@app.task
def low(n1, n2):
    res = n1 - n2
    print('n1 - n2 = %s' % res)
    return res

