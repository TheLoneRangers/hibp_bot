import requests
from boto3 import ssm

def get_ssm_client():
    ssm_client = boto3.client('ssm')
    return ssm_client

def get_api_token():
    client = get_ssm_client()
    api_token = client.get_parameter(
        Name='/lambda_params/hibp_bot',
        WithDecryption=True
    )

    # return api_token
    print(api_token)

def construct_user_agent():
    user_agent = "hibp_bot_v1"

    return user_agent

def construct_request(user_agent, api_token, base_url):
        user_agent = construct_user_agent()
        api_token = get_api_token()
        base_url = 'https://haveibeenpwned.com/api/v3/'

def check_address(email_address):
    address_check_url = f'breachedaccount/{email_address}'