# 一分钟发一次短信频率限制
from rest_framework.throttling import SimpleRateThrottle
class SMSRateThrottle(SimpleRateThrottle):
    scope = 'sms'
    def get_cache_key(self, request, view):
        mobile = request.data.get('mobile')
        if mobile:
            return 'sms_cache_%s' % mobile

