from huey import RedisHuey

huey = RedisHuey(url='redis://localhost:6379/0')

@huey.task()
def background_task(key, value):
    pass
