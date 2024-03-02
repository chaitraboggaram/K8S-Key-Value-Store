#!/Users/ipadhu/Documents/GitHub/K8S-Key-Value-Store/venv/bin/python3

import logging
import os
import sys

from huey.consumer import Consumer
from huey.consumer_options import ConsumerConfig
from huey.consumer_options import OptionParserHandler
from huey.utils import load_class
from huey import RedisHuey

def err(s):
    sys.stderr.write('\033[91m%s\033[0m\n' % s)

def load_huey(path):
    try:
        return load_class(path)
    except:
        cur_dir = os.getcwd()
        if cur_dir not in sys.path:
            sys.path.insert(0, cur_dir)
            return load_huey(path)
        err('Error importing %s' % path)
        raise

def consumer_main():
    parser_handler = OptionParserHandler()
    parser = parser_handler.get_option_parser()
    options, args = parser.parse_args()

    if len(args) == 0:
        err('Error:   missing import path to `Huey` instance')
        err('Example: huey_consumer.py app.queue.huey_instance')
        sys.exit(1)

    options = {k: v for k, v in options.__dict__.items() if v is not None}
    config = ConsumerConfig(**options)
    config.validate()

    huey_instance = load_huey(args[0])

    # Set up logging for the "huey" namespace.
    logger = logging.getLogger('huey')
    config.setup_logger(logger)

    redis_url = 'redis://redis-primary-service:6379/0'
    huey_instance = RedisHuey('main', host='redis-primary-service.default.svc.cluster.local', port=6379)
    huey_instance.connection = redis_url

    consumer = Consumer(huey_instance, **config.values)
    consumer.run()

if __name__ == '__main__':
    if sys.version_info >= (3, 8) and sys.platform == 'darwin':
        import multiprocessing
        try:
            multiprocessing.set_start_method('fork')
        except RuntimeError:
            pass
    consumer_main()
