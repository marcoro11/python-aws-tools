import boto3


def check_lambda_security():
    client = boto3.client('lambda')
    functions = client.list_functions()['Functions']
    for func in functions:
        if not func.get('VpcConfig') or not func['VpcConfig'].get('VpcId'):
            print(f'Lambda function not in VPC: {func["FunctionName"]}')
        env_vars = func.get('Environment', {}).get('Variables', {})
        sensitive_keys = ['password', 'secret', 'key']
        for key in env_vars:
            if any(s in key.lower() for s in sensitive_keys):
                print(f'Potential sensitive env var in Lambda: {func["FunctionName"]} - {key}')