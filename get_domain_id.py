import requests
import os
from dotenv import load_dotenv
load_dotenv()


# Load environment variables from .env file
api_token = os.getenv('API_TOKEN')
zone_id = os.getenv('ZONE_ID')
dns_record_name = os.getenv('DNS_RECORD_NAME')

# Check if the required environment variables are set
if not all([api_token, zone_id, dns_record_name]):
    print("Erro: Certifique-se de que API_TOKEN, ZONE_ID e DNS_RECORD_NAME estão definidos no .env")
    exit(1)

# Define the headers for the request
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

# Make a request to the Cloudflare API to list DNS records
try:
    response = requests.get(
        f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records',
        headers=headers
    )

    # Verify if the request was successful
    if response.status_code == 200:
        dns_records = response.json()
        found = False
        for record in dns_records['result']:
            if record['name'] == dns_record_name:
                print(f"ID: {record['id']}, Name: {record['name']}, Type: {record['type']}, Content: {record['content']}")
                found = True
        if not found:
            print(f"Registro DNS '{dns_record_name}' não encontrado.")
    else:
        print('Falha ao listar os registros DNS:', response.status_code, response.text)

except requests.exceptions.RequestException as e:
    print("Erro ao se comunicar com a API da Cloudflare:", e)