#payloads.py
from uuid import uuid4
from datetime import datetime
from faker import Faker
from random import randint, choice
import random
from pathlib import Path
from time import time

_ASSETS = Path(__file__).resolve().parent.parent / "assets"
_ASSETS.mkdir(exist_ok=True)
SAMPLE_IMG = _ASSETS / "plate.jpg"
FACE_IMG = _ASSETS / "face.jpg" 
_fake = Faker("tr_TR")
_TURKISH_LETTERS = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def det_payload() -> dict:
    lat, lon = _fake.latitude(), _fake.longitude()
    return {
        "ptsUniqueID": uuid4().hex[:16],
        "operation": 1,
        "vehicles": [{
            "location": _fake.city(),
            "dateTime": datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3],
            "longitude": float(lon),
            "latitude": float(lat),
            "plate": _fake.license_plate(),
            "country": _fake.country(),
            "plateCoordinate": f"{lat},{lon}",
            "plateCount": randint(1, 5),
            "direction": choice([1, 2]),
            "confidence": randint(90, 100),
            "make": _fake.company().split()[0].upper(),  #vehicle modülünde sıkıntı olduğu için company koydum
            "type": "OTOMOBIL",
            "color": _fake.color_name().upper(),
            "speed": randint(0, 120),
            "camera": randint(0, 1),
        }]
    }

def status_payload() -> dict:
    return {
        "dateTime": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
        "cameraList": [{
            "ptsUniqueId": uuid4().hex[:16],
            "isCameraAlive": _fake.boolean(),
            "isSoftwareAlive": _fake.boolean(),
        }]
    }

def health_payload(template: str = "1111111111111111") -> dict:
    length = len(template)
    random_digits = str(random.randint(0, 10**length - 1)).zfill(length)
    return {
        "ptsUniqueID": random_digits
    }

def _generate_plate() -> str:
    city = str(randint(0, 81)).zfill(2)
    letters = "".join(choice(_TURKISH_LETTERS) for _ in range(3))
    numbers = str(randint(0, 999)).zfill(3)
    return f"{city}{letters}{numbers}"

def rand_filename(prefix: str) -> str:
    """plate_abe12345.jpg veya face_f67ab890.jpg gibi 8-haneli isim üretir"""
    return f"{prefix}_{uuid4().hex[:8]}.jpg"

def images_payload() -> tuple[dict, Path, str]:
    fields = {
        "PTSUniqueID": uuid4().hex[:16],
        "Plaka": _generate_plate(),
        "DateTime": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
        "Camera": str(randint(1, 5)),
    }
    return fields, SAMPLE_IMG, rand_filename("plate")

def face_payload(idx: int | None = None) -> tuple[dict, Path, str]:
    cam_id = f"Camera {idx or randint(1, 100)}"
    fields = {
        "CamId": cam_id,
        "PhotoId": str(randint(1000, 9999)),
        "Timestamp": str(int(time())),
    }
    return fields, FACE_IMG, rand_filename("face")