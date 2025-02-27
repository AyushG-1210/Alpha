from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    user_text = data.get('text')
    response_text = user_text.upper()  # Example processing (Modify later)
    return jsonify({"output": response_text})

if __name__ == '__main__':
    app.run(debug=True)
