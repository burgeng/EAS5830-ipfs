import requests
import json

PINATA_API_KEY = "a554e03c25c4da3d54be"
PINATA_SECRET_API_KEY = "95f333615b623785322d9338ead1c6e8778d88a32ba5777454a9e22924968ab1"

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
