from flask import Flask, render_template, request, jsonify
import your_model_module  # replace with your model import

app = Flask(__name__)

# load or initialize your ASO model\model = your_model_module.load_model()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    rna_seq = data.get('rna_sequence', '').strip().upper()
    if not rna_seq:
        return jsonify({'error': 'No sequence provided'}), 400

    try:
        aso = model.predict_aso(rna_seq)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'aso': aso})

if __name__ == '__main__':
    app.run(debug=True)