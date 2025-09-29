import boto3


def analyze_cloudtrail_logs():
    client = boto3.client('cloudtrail')
    trails = client.describe_trails()['trailList']
    for trail in trails:
        # Look for failed console logins
        events = client.lookup_events(LookupAttributes=[{'AttributeKey': 'EventName', 'AttributeValue': 'ConsoleLogin'}])
        for event in events['Events']:
            if event.get('ErrorCode'):
                print(f"Suspicious activity: Failed login in trail {trail['Name']}: {event['ErrorCode']} at {event['EventTime']}")
        # Look for unauthorized operations
        events = client.lookup_events(LookupAttributes=[{'AttributeKey': 'EventName', 'AttributeValue': 'AssumeRole'}])
        for event in events['Events']:
            if event.get('ErrorCode'):
                print(f"Suspicious activity: Failed AssumeRole in trail {trail['Name']}: {event['ErrorCode']} at {event['EventTime']}")