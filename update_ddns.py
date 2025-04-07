import os
import requests
from dotenv import load_dotenv
from cloudflare import Cloudflare

load_dotenv()

api_token = os.getenv('API_TOKEN')
zone_id = os.getenv('ZONE_ID')
dns_record_id = os.getenv('DNS_RECORD_ID')

# Method for discover the public ip
def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

# Method bellow is used to update the dns record using put with api token
def update_dns_record(ip_adress):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'A',
        'name': os.getenv("DNS_RECORD_NAME"),
        'content': ip_adress,
        'ttl': 120,
        'proxied': False
    }
    response = requests.put(
        f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record_id}',
        headers=headers,
        json=data
    )
    if response.status_code == 200:
        print('DNS record updated successfully')
    else:
        print('Failed to update DNS record:', response.json())

if __name__ == '__main__':
    # Get the current public IP address
    ip_address = get_public_ip()

    # Update the DNS record with the current public IP address
    update_dns_record(ip_address)