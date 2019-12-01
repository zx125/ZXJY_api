from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.views import Response
from rest_framework import status
from utils.logging import logger
def exception_handler(exc, context):
    #异常信息字典context
    response = drf_exception_handler(exc, context)
    # 异常模块就是记录项目的错误日志
    logger.error('%s - %s - %s' % (context['view'], context['request'].method, exc))
    if response is None:
        return Response({
            'detail': '%s' % exc
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)
    return response