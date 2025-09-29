import boto3
import yaml


with open('settings.yaml', 'r') as f:
    settings = yaml.safe_load(f)

def scan_s3_secrets():
    client = boto3.client('s3')
    buckets = client.list_buckets()['Buckets']
    extensions = settings['scan']['s3']['include_extensions']
    for bucket in buckets:
        objects = client.list_objects_v2(Bucket=bucket['Name']).get('Contents', [])
        for obj in objects:
            if any(obj['Key'].endswith(ext) for ext in extensions):
                print(f'Potential secret found in S3 bucket {bucket["Name"]}: {obj["Key"]}')

def detect_public_buckets():
    client = boto3.client('s3')
    buckets = client.list_buckets()['Buckets']
    for bucket in buckets:
        acl = client.get_bucket_acl(Bucket=bucket['Name'])
        for grant in acl['Grants']:
            if grant['Permission'] == 'READ' and grant['Grantee']['Type'] == 'Group' and 'AllUsers' in grant['Grantee']['URI']:
                print(f'Publicly accessible bucket detected: {bucket["Name"]}')