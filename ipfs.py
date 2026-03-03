import requests
import json

PINATA_API_KEY = "c0f640505f950a609d98"
PINATA_SECRET_API_KEY = "deae804b955fb8374558234e5a6999b2cb01d6d5e4c8f76a66371807e30f0e6c"

def pin_to_ipfs(data):
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)
    response.raise_for_status()

    cid = response.json()["IpfsHash"]
    return cid

def get_from_ipfs(cid):
    url = f"https://ipfs.io/ipfs/{cid}"

    response = requests.get(url)
    response.raise_for_status()

    return response.json()
