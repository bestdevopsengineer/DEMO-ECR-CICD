import sys
def handler(event, context):
    return 'Hello World from AWS Lambda using Python' + sys.version + '!'
