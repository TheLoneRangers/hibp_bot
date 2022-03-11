from pkgutil import get_data
from posixpath import split
import requests
import boto3
import time

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
    print('get_data')
    headers = {'hibp-api-key': f'{api_token}', 'user-agent': f'{user_agent}' }
    breaches = requests.get(base_url, headers=headers)
    time.sleep(2)

    # Only in python 3.10, I guess...
    # match breaches.status_code:
    #     case 404:
    #         return f'No breaches found for {base_url.split("v3/")[1]}'
    #     case 200:
    #         return breaches.json
    if breaches.status_code == 404:
        return f'No breaches found for {base_url.split("v3/")[1]}'
    if breaches.status_code == 200:
        return breaches.json
    if breaches.status_code == 429:
        return "You are being rate limited."

def construct_request(address_check_url):
        user_agent = construct_user_agent()
        api_token = get_api_token()
        base_url = f'https://haveibeenpwned.com/api/v3/{address_check_url}'

        get_data(user_agent, api_token, base_url)

def check_address(address):
        address_check_url = f'breachedaccount/{address}'
    
        construct_request(address_check_url)
