import boto3


def suggest_cost_optimizations():
    ec2_client = boto3.client('ec2')
    instances = ec2_client.describe_instances()['Reservations']
    for reservation in instances:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'stopped':
                print(f'Stopped instance detected: {instance["InstanceId"]}. Consider terminating to save costs.')
    
    volumes = ec2_client.describe_volumes()['Volumes']
    for vol in volumes:
        if vol['State'] == 'available':
            print(f'Unused EBS volume detected: {vol["VolumeId"]}. Consider deleting to save costs.')
    
    rds_client = boto3.client('rds')
    instances = rds_client.describe_db_instances()['DBInstances']
    for db in instances:
        if db['DBInstanceStatus'] == 'stopped':
            print(f'Stopped RDS instance detected: {db["DBInstanceIdentifier"]}. Consider terminating to save costs.')