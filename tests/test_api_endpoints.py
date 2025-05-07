import pytest, requests
from apitools.payloads import det_payload, status_payload, health_payload, images_payload, face_payload
from apitools.api_client import post, post_multipart

ENDPOINTS = [
    ("/services/detections", det_payload, "json"),
    ("/services/deviceStatus", status_payload, "json"),
    ("/services/health", health_payload, "json"),
    ("/services/images", images_payload, "multipart"),
    ("/services/face", face_payload, "multipart")
]

@pytest.mark.parametrize("endpoint,payload_fn,kind", ENDPOINTS,
                         ids=[e[0] for e in ENDPOINTS])
def test_returns_200(endpoint, payload_fn, kind):
    if kind == "json":
        resp: requests.Response = post(endpoint, payload_fn())
    else:  # multipart
        fields, img, fname = payload_fn()
        resp: requests.Response = post_multipart(endpoint, fields, img, fname)

    print(f"[CHECK] {endpoint} -> {resp.status_code}")
    assert resp.status_code == 200
