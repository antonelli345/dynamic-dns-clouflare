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

    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    response = requests.get(url, headers=headers)
    records = response.json()['result']

    for record in records:
        if record['type'] == 'A':
            name = record['name']
            current_ip = record['content']
            record_id = record['id']
            proxied = record['proxied']

            if current_ip != ip_adress:
                print(f'Updating DNS record {name} from {current_ip} to {ip_adress}')
                data = {
                    'type': 'A',
                    'name': name,
                    'content': ip_adress,
                    'ttl': 120,
                    'proxied': proxied
                }
                update_url = f'{url}/{record_id}'
                r = requests.put(update_url, headers=headers, json=data)

                if r.status_code == 200:
                    print(f"Registro {name} atualizado com sucesso!")
                else:
                    print(f"Falha ao atualizar {name}: {r.text}")
            else:
                print(f" {name} já está com o IP correto.")



if __name__ == '__main__':
    # Get the current public IP address
    ip_address = get_public_ip()

    # Update the DNS record with the current public IP address
    update_dns_record(ip_address)