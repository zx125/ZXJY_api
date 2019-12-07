# 后台http根路径
# BASE_URL = 'http://127.0.0.1:8000'

# 前台http根路径
# LUFFY_URL = 'http://127.0.0.1:8080'

# 后台http根路径
BASE_URL = 'http://116.62.152.65:8000'

# 前台http根路径
LUFFY_URL = 'http://116.62.152.65:8080'

# 订单支付成功的后台异步回调接口
NOTIFY_URL = BASE_URL + '/order/success'

# 订单支付成功的前台同步回调接口
RETURN_URL = LUFFY_URL + '/pay/success'

# 短信过期时间
SMS_EXP = 300

SMS_CACHE_KEY = 'sms_%s'

# 轮播图推荐数
BANNER_COUNT = 3
