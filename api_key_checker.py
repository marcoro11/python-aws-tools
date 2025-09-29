import re
import json
import boto3

from datetime import datetime, timedelta


def detect_expired_api_keys():
    client = boto3.client('iam')
    users = client.list_users()['Users']
    for user in users:
        access_keys = client.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
        for key in access_keys:
            create_date = key['CreateDate']
            if create_date < datetime.now(create_date.tzinfo) - timedelta(days=90):
                print(f'Old API Key detected (over 90 days): {key["AccessKeyId"]} for User: {user["UserName"]}')
