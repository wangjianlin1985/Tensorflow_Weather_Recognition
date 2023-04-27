# -*- coding: utf-8 -*-
# FileName  : conf.py
import os
from pathlib import Path

# 本文件位置
my_path = Path(__file__).resolve()

# 模型文件位置
model_path = os.path.join(my_path.parent, 'train_model', 'weather_model.h5')
