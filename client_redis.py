import redis


def init_conection():
    global redis_client
    pool = redis.ConnectionPool(host='localhost', port=6379, db=1)
    redis_client = redis.Redis(connection_pool=pool)


def create_reg(key, value):
    redis_client.set(key, value)
    return True


def get_all_reg():
    values = redis_client.keys()
    return values
