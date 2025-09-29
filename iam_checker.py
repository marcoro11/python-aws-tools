import boto3


def check_unused_iam_rules():
    client = boto3.client('iam')
    users = client.list_users()['Users']
    for user in users:
        access_keys = client.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
        for key in access_keys:
            if key['Status'] == 'Inactive':
                print(f'Unused IAM Access Key: {key["AccessKeyId"]} for User: {user["UserName"]}')

def check_insecure_iam_rules():
    client = boto3.client('iam')
    policies = client.list_policies(Scope='Local')['Policies']
    for policy in policies:
        policy_details = client.get_policy(PolicyArn=policy['Arn'])
        version_id = policy_details['Policy']['DefaultVersionId']
        version = client.get_policy_version(PolicyArn=policy['Arn'], VersionId=version_id)
        document = version['PolicyVersion']['Document']
        statements = document.get('Statement', [])
        if not isinstance(statements, list):
            statements = [statements]
        for stmt in statements:
            if stmt.get('Effect') == 'Allow':
                actions = stmt.get('Action', [])
                if not isinstance(actions, list):
                    actions = [actions]
                principals = stmt.get('Principal', {})
                if isinstance(principals, dict) and '*' in str(principals):
                    print(f'Insecure IAM Policy: {policy["PolicyName"]} - Allows actions to all principals')
                elif '*' in actions:
                    print(f'Insecure IAM Policy: {policy["PolicyName"]} - Allows all actions')

def detect_misconfigured_roles():
    client = boto3.client('iam')
    roles = client.list_roles()['Roles']
    for role in roles:
        policies = client.list_attached_role_policies(RoleName=role['RoleName'])['AttachedPolicies']
        for policy in policies:
            policy_details = client.get_policy(PolicyArn=policy['PolicyArn'])
            version_id = policy_details['Policy']['DefaultVersionId']
            version = client.get_policy_version(PolicyArn=policy['PolicyArn'], VersionId=version_id)
            document = version['PolicyVersion']['Document']
            statements = document.get('Statement', [])
            if not isinstance(statements, list):
                statements = [statements]
            for stmt in statements:
                if stmt.get('Effect') == 'Allow':
                    actions = stmt.get('Action', [])
                    if not isinstance(actions, list):
                        actions = [actions]
                    if '*' in actions:
                        print(f'Misconfigured role: {role["RoleName"]} - Has policy allowing all actions: {policy["PolicyName"]}')

def check_mfa_enforcement():
    client = boto3.client('iam')
    users = client.list_users()['Users']
    for user in users:
        mfa_devices = client.list_mfa_devices(UserName=user['UserName'])['MFADevices']
        if not mfa_devices:
            print(f'User without MFA: {user["UserName"]}')