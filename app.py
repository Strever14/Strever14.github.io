from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Backend Jalan di Render!"

@app.route('/save_jadwal', methods=['POST'])
def save_jadwal():
    data = request.get_json()
    with open("jadwal.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return jsonify({"status": "success", "message": "Jadwal berhasil disimpan"})

@app.route('/get_jadwal', methods=['GET'])
def get_jadwal():
    try:
        with open("jadwal.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "Belum ada jadwal"})
