# -*- coding: utf-8 -*-
# FileName  : image_check.py
import tensorflow as tf
from .conf import model_path
import numpy as np

weather_name = ['多云', '雨天', '晴天', '日出']

#将天气图片转为固定像素格式的数据
def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [180, 180])
    image = tf.cast(image, tf.float32)
    return image

#根据图片路径预测图片的天气
def check_handle(img_path):
    model = tf.keras.models.load_model(model_path)  #加载训练好的预测模型

    test_img = img_path
    test_tensor = load_and_preprocess_image(test_img)  #预处理图片格式
    test_tensor = tf.expand_dims(test_tensor, axis=0)
    pred = model.predict(test_tensor)  #调用模型预测各种天气概率
    pred_num = np.argmax(pred)  #选择概率最大的作为天气结果
    result = weather_name[int(pred_num)]
    return result
