import json
import os
import fcntl

CACHE_FILE = '/mnt/cache/histogram.json'
cache=dict()
try:
    with open(CACHE_FILE, 'r') as cacheFile:
        fcntl.flock(cacheFile, fcntl.LOCK_SH)
        cache = json.loads(cacheFile)
        fcntl.flock(cacheFile, fcntl.LOCK_UN)
except:
    print("no cache file present")


def updateCache(cache):
    with open(CACHE_FILE, 'w') as cacheFile:
        fcntl.flock(cacheFile, fcntl.LOCK_EX)
        json.dump(cache,cacheFile)
        fcntl.flock(cacheFile, fcntl.LOCK_UN)

def lambda_handler(event, context):
    #word = event["word"]
    word = event["queryStringParameters"]["word"]
    #print(event)
    #word = "abcd"
    print(cache)
    output = cache
    for i, v in enumerate(word.lower()):
        output[v] = output.get(v, 0) + 1
    updateCache(output)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(output)
    }
