import hmac


# 实现HmacSHA1加密
def hmac_sha1(key, data):
    return hmac.new(key.encode(), data.encode(), 'sha1').hexdigest()
