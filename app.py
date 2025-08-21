#v3 

# python_backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app, resources={
    r"/**": {"origins": [
        "http://localhost:5173",
        "https://pokernow-ai.vercel.app",
        "https://pokernowai.com"
    ], "supports_credentials": True}
})

@app.route("/job-status/test", methods=["GET"])
def test():
    return jsonify({"status": "ok", "message": "API is live"})

if __name__ == "__main__":
    # use PORT env if provided (Render/Cloud Run), else 5000 locally
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))




#Current file on API: python_backend/app.py 

# from flask import Flask
# from flask_cors import CORS
# # from app import app as application  # noqa
# import os
# import pandas as pd
# import numpy as np
# from werkzeug.utils import secure_filename

# # os.environ['FLASK_ENV'] = 'production'

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "https://pokernow-ai.vercel.app"}})

# @app.route('/job-status/test')
# def test():
#     return {'status': 'ok', 'message': 'API is live'}




###############################
# Uncomment the following lines if you need to run this file directly


# #Need this file to run on PythonAnywhere, v. 3.10

# # from flask import Flask
# # from flask_cors import CORS

# # app = Flask(__name__)
# # CORS(app, resources={r"/*": {"origins": "https://pokernowai.com"}})

# # @app.route('/job-status/test')
# # def test():
# #     return {'status': 'ok', 'message': 'API is live'}

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os
# import pandas as pd
# import numpy as np
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

# # Directories
# UPLOAD_DIR = os.path.join(os.path.dirname(__file__), 'uploads')
# RESULT_DIR = os.path.join(os.path.dirname(__file__), 'results')

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(RESULT_DIR, exist_ok=True)


# @app.route('/job-status/test', methods=['GET'])
# def test():
#     return jsonify({'status': 'ok', 'message': 'API is live'})


# @app.route('/analyze', methods=['POST'])
# def analyze_log():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400

#     file = request.files['file']
#     filename = secure_filename(file.filename)

#     if not filename.endswith('.txt'):
#         return jsonify({'error': 'Only .txt files are allowed'}), 400

#     filepath = os.path.join(UPLOAD_DIR, filename)
#     file.save(filepath)

#     try:
#         with open(filepath, 'r') as f:
#             lines = f.readlines()

#         # Example analysis: count hands per player
#         player_stats = {}
#         for line in lines:
#             if 'posts small blind' in line or 'posts big blind' in line:
#                 player = line.split(':')[0].strip()
#                 player_stats[player] = player_stats.get(player, 0) + 1

#         df = pd.DataFrame(list(player_stats.items()), columns=['Player', 'Hands Played'])
#         output_file = os.path.join(RESULT_DIR, f"{filename}_analysis.csv")
#         df.to_csv(output_file, index=False)

#         return jsonify({
#             'message': 'Analysis complete',
#             'results': df.to_dict(orient='records')
#         })

#     except Exception as e:
#         return jsonify({'error': f'Failed to analyze file: {str(e)}'}), 500


# if __name__ == '__main__':
#     app.run(debug=True)