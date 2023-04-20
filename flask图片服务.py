

import os
import io
import json
import torch

from PIL import Image
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # 解决跨域问题





basedir = os.path.abspath(os.path.dirname(__file__))  # 定义一个根目录 用于保存图片用

import cv2
#http://172.27.118.204:5050
@app.route('/', methods=['GET', 'POST'])
def editorData():
    # 获取图片文件 name = upload
    img = request.files.get('upload')

    # 定义一个图片存放的位置 存放在static下面
    path = basedir

    # 图片名称
    imgName = img.filename

    # 图片path和名称组成图片的保存路径
    file_path = path + '/'+imgName
    print(file_path,22222222)
    a=img.read()
    a=bytearray(a)
    # print(a)
    import numpy as np
    a=cv2.imdecode(np.array(a, dtype='uint8'), cv2.IMREAD_UNCHANGED)  # 从二进制图片数据中读取
    print(a)
    print(a.shape)#===============成功打印到了图片信息.

    # a=cv2.imread(img.read())
    # # 保存图片
    # img.save(file_path)

    # url是图片的路径
    url =  imgName
    return url


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)