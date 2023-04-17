import json
import os
import fcntl
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

CACHE_FILE = '/mnt/cache/histogram.json'
cache=dict()
try:
    with open(CACHE_FILE, 'r') as cacheFile:
        fcntl.flock(cacheFile, fcntl.LOCK_SH)
        json_object = json.load(cacheFile)
        print(json_object)
        fcntl.flock(cacheFile, fcntl.LOCK_UN)
except:
    logger.info('no cache file present')


def updateCache(cache):
    with open(CACHE_FILE, 'w') as cacheFile:
        fcntl.flock(cacheFile, fcntl.LOCK_EX)
        logger.info('Updating cache')
        json_object = json.dumps(cache)
        cacheFile.write(json_object)
        fcntl.flock(cacheFile, fcntl.LOCK_UN)


def lambda_handler(event, context):
    #word = event["word"]
    word = event["queryStringParameters"]["word"]
    output = cache
    for i, v in enumerate(word.lower()):
        output[v] = output.get(v, 0) + 1
    updateCache(output)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(output)
    }
