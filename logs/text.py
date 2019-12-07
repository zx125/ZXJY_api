

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lufeiapi.settings.dev")
django.setup()


from libs.iPay import alipay, alipay_gateway

import time
order_params = alipay.api_alipay_trade_page_pay(out_trade_no='%s' % time.time(),
    total_amount=4200000,
    subject='波音747定金',
    return_url="http://localhost:8080",  # 同步回调的前台接口
    notify_url="https://example.com/notify" # 异步回调的后台接口
)
print(alipay_gateway + order_params)