import json


def lambda_handler(event):
    word = event["word"]
    print(word)
    output = dict()
    for i, v in enumerate(word):
        output[v] = output.get(v, 0) + 1
    return {
        'statusCode': 200,
        'body': json.dumps(output)
    }


def readInput():
    data = {"word": "Kognitos"}
    return data

def main():
    event = readInput()
    lambda_output = lambda_handler(event)
    print(lambda_output)


if __name__ == "__main__":
    main()
