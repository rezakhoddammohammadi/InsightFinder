from flask import Flask, request, jsonify
from src.parser import parse_mbox_file
from src.analyzer import count_senders, count_by_day, get_most_common_words

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    try:
        # Save uploaded file temporarily
        file_path = "temp_uploaded.mbox"
        uploaded_file.save(file_path)

        emails = parse_mbox_file(file_path)
        senders = count_senders(emails)
        days = count_by_day(emails)
        common_words = get_most_common_words(emails)

        return jsonify({
            'total_emails': len(emails),
            'emails_per_sender': senders,
            'emails_per_day': days,
            'top_words': common_words
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
