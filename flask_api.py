import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


DJANGO_BASE_URL = 'http://host.docker.internal:8000'


@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        response = requests.get(f'{DJANGO_BASE_URL}/api/products/')
        response.raise_for_status()  
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        response = requests.get(f'{DJANGO_BASE_URL}/api/placed-orders/')
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/revenue-by-category', methods=['GET'])
def get_revenue_per_product():
    try:
        response = requests.get(f'{DJANGO_BASE_URL}/api/revenue-by-category/')
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/highest-selling-product', methods=['GET'])
def get_highest_selling():
    try:
        response = requests.get(f'{DJANGO_BASE_URL}/api/highest-selling-product')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

