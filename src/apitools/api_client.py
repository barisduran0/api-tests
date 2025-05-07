#api_client.py
import requests
from pathlib import Path
from typing import Dict, Union
from pathlib import Path

BASE = "https://192.170.6.11:7504"
HEADERS = {"Content-Type": "application/json", "Accept": "text/plain"}

# sertifika (varsa) --> certs/server-ca.pem
CERT_PATH = Path(__file__).with_suffix(".pem")
VERIFY_SSL = CERT_PATH if CERT_PATH.exists() else False

def post(endpoint: str, payload: dict) -> requests.Response:
    return requests.post(BASE + endpoint,
                         json=payload,
                         headers=HEADERS,
                         verify=VERIFY_SSL)

def post_multipart(endpoint: str,
                   fields: Dict[str, Union[str, int]],
                   image_path: Path,
                   filename: str) -> requests.Response:
    """
    filename = HTTP form-data'da görünecek ad; her istek için benzersiz ver.
    """
    # Server hangi anahtar bekliyorsa (“Image” veya “Face”) onu seçelim:
    file_key = "Image" if endpoint.endswith("images") else "Face"
    files = {file_key: (filename, open(image_path, "rb"), "image/jpeg")}
    return requests.post(BASE + endpoint,
                         data=fields,
                         files=files,
                         verify=VERIFY_SSL)
