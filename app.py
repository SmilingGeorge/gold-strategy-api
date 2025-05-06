from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    price = float(data.get("gold_price", 0))

    # Example strategy logic
    entry = price < 2300
    confidence = round(random.uniform(0.75, 0.9), 2) if entry else round(random.uniform(0.4, 0.7), 2)

    return jsonify({
        "entry_signal": entry,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


