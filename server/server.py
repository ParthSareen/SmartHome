from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)

@app.route('/upload_data', methods=['POST'])
def upload_data():
    # Verify the signature of the incoming data
    signature = request.headers.get('X-Signature')
    if not signature or not verify_signature(request.data, signature):
        return jsonify({'message': 'Invalid signature'}), 403

    data = request.get_json()
    print(data)
    return jsonify({'message': 'Data received'})

def verify_signature(data, signature):
    # Replace 'your-signing-key' with your actual signing key
    signing_key = 'your-signing-key'
    # Create a new HMAC "signature", and verify it matches the incoming signature
    computed_signature = hmac.new(signing_key.encode(), data, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed_signature, signature)