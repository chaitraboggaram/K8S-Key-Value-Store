from huey import RedisHuey, crontab

huey = RedisHuey(host='redis://localhost:6379/')

@huey.task()
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    res = add_numbers(1, 2)
    print(res)
    print(res())