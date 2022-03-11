from pkgutil import get_data
import requests
import boto3

def get_ssm_client():
    ssm_client = boto3.client('ssm')
    return ssm_client

def get_api_token():
    client = get_ssm_client()
    api_token = client.get_parameter(
        Name='/lambda_params/hibp_bot',
        WithDecryption=True
    )

    return api_token["Parameter"]["Value"]

def construct_user_agent():
    user_agent = "hibp_bot_v1"

    return user_agent

def get_data(user_agent, api_token, base_url):
    headers = {'hibp-api-key': f'{api_token}', 'user-agent': f'{user_agent}' }
    breaches = requests.get(base_url, headers=headers)

    print(breaches)

def construct_request(address_check_url):
        user_agent = construct_user_agent()
        api_token = get_api_token()
        base_url = f'https://haveibeenpwned.com/api/v3/{address_check_url}'

        get_data(user_agent, api_token, base_url)

def check_address(domain, address):
    for name in address:
        address_check_url = f'breachedaccount/{name}?domain={domain}'
    
        construct_request(address_check_url)
