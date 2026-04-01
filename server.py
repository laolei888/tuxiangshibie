from flask import Flask, request, jsonify
from flask_cors import CORS
from aip import AipImageClassify
from aip import AipOcr
import base64

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client_classify = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
client_ocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

app = Flask(__name__)
CORS(app)  # 允许跨域



@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    image_base64 = data.get('image')

    if not image_base64:
        return jsonify({"error": "图片数据为空"}), 400

    if ',' in image_base64:
        image_base64 = image_base64.split(',')[1]
    try:
        image_data = base64.b64decode(image_base64)
    except Exception as e:
        return jsonify({'error': '图片解码失败: ' + str(e)}), 400

    results = {
        'objects': [],
        'texts': []
    }

    try:
        res_obj = client_classify.advancedGeneral(image_data)
        if 'result' in res_obj:
            results['objects'] = res_obj['result'][:5]
    except Exception as e:
        print(f"物体识别错误: {e}")

    try:
        res_txt = client_ocr.basicGeneral(image_data)
        if 'words_result' in res_txt:
            results['texts'] = res_txt['words_result']
    except Exception as e:
        print(f"文字识别错误: {e}")

    return jsonify(results)


if __name__ == '__main__':
    print("🚀 服务器已启动，地址: http://127.0.0.1:5000")
    app.run(debug=True)
