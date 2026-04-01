# Vision API Server

基于 Flask 和 百度 AI 的图像识别与文字识别服务。

## 功能
- 📷 **图像识别**：识别图片中的物体和场景 (使用 `AipImageClassify`).
- 📝 **文字识别**：提取图片中的文字 (使用 `AipOcr`).

## 快速开始

### 1. 获取密钥
前往 [百度智能云控制台](https://console.bce.baidu.com/) 创建应用，获取 `APP_ID`, `API_KEY`, `SECRET_KEY`。

### 2. 安装依赖
```bash
pip install -r requirements.txt
