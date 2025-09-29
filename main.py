import argparse

from iam_checker import check_unused_iam_rules, check_insecure_iam_rules, detect_misconfigured_roles, check_mfa_enforcement
from s3_scanner import scan_s3_secrets, detect_public_buckets
from cloudtrail_analyzer import analyze_cloudtrail_logs
from cost_optimizer import suggest_cost_optimizations
from api_key_checker import detect_expired_api_keys
from security_group_analyzer import check_security_groups
from lambda_security_checker import check_lambda_security


def main():
    parser = argparse.ArgumentParser(description="AWS Toolkit - Swiss Army Knife for AWS Security")
    parser.add_argument("--check-iam", action="store_true", help="Check unused and insecure IAM rules")
    parser.add_argument("--scan-s3", action="store_true", help="Scan S3 buckets for secrets")
    parser.add_argument("--detect-public-buckets", action="store_true", help="Detect publicly accessible S3 buckets")
    parser.add_argument("--analyze-cloudtrail", action="store_true", help="Analyze CloudTrail logs for suspicious activity")
    parser.add_argument("--suggest-cost-optimizations", action="store_true", help="Suggest cost optimization strategies")
    parser.add_argument("--detect-misconfigured-roles", action="store_true", help="Detect misconfigured IAM roles")
    parser.add_argument("--detect-expired-api-keys", action="store_true", help="Detect expired API keys")
    parser.add_argument("--check-mfa", action="store_true", help="Check MFA enforcement for IAM users")
    parser.add_argument("--check-security-groups", action="store_true", help="Check for overly permissive security groups")
    parser.add_argument("--check-lambda-security", action="store_true", help="Check Lambda functions for security issues")
    args = parser.parse_args()

    if args.check_iam:
        check_unused_iam_rules()
        check_insecure_iam_rules()
    if args.scan_s3:
        scan_s3_secrets()
    if args.detect_public_buckets:
        detect_public_buckets()
    if args.analyze_cloudtrail:
        analyze_cloudtrail_logs()
    if args.suggest_cost_optimizations:
        suggest_cost_optimizations()
    if args.detect_misconfigured_roles:
        detect_misconfigured_roles()
    if args.detect_expired_api_keys:
        detect_expired_api_keys()
    if args.check_mfa:
        check_mfa_enforcement()
    if args.check_security_groups:
        check_security_groups()
    if args.check_lambda_security:
        check_lambda_security()

if __name__ == "__main__":
    main()