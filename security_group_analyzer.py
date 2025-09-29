import boto3


def check_security_groups():
    client = boto3.client('ec2')
    security_groups = client.describe_security_groups()['SecurityGroups']
    for sg in security_groups:
        for permission in sg['IpPermissions']:
            if permission.get('IpRanges'):
                for ip_range in permission['IpRanges']:
                    if ip_range['CidrIp'] == '0.0.0.0/0':
                        print(f'Overly permissive security group: {sg["GroupId"]} allows {permission["IpProtocol"]} from anywhere')