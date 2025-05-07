from flask import Flask, request

app = Flask(__name__)

# 1) Mirsad endpoint
@app.route('/services/detections', methods=['POST'])
def mirsad_handler():
    data = request.get_json()
    print("[Mirsad_Detections] Received:", data)
    return {"status": "mirsad ok"}, 200

@app.route('/services/deviceStatus', methods=['POST'])
def status_handler():
    data = request.get_json()
    print("[Mirsad_Status] Received:", data)
    return {"status": "status ok"}, 200

@app.route('/services/health', methods=['POST'])
def health_handler():
    data = request.get_json()
    print("[Mirsad_Health] Received:", data)
    return {"status": "health ok"}, 200

# 2) Odakan endpoint
@app.route('/odakan', methods=['POST'])
def odakan_handler():
    content_type = request.headers.get('Content-Type')
    print("[Odakan] Content-Type:", content_type)

    raw_data = request.get_data()
    print("[Odakan] Raw data length:", len(raw_data))
    return {"status": "odakan ok"}, 200

# 3) Yaka endpoint
@app.route('/v1/faces/search', methods=['POST'])
def face_search_handler():
    content_type = request.headers.get('Content-Type')
    print("[FaceImageService] Content-Type:", content_type)

    raw_data = request.get_data()
    print("[FaceImageService] Raw data length:", len(raw_data))
    return {"result": "face search ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1880)
