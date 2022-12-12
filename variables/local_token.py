import threading

# 用于feignClient调用时 拦截传入token
local_token = threading.local()