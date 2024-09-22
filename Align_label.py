# 假设 img_paths 是图像路径列表，label_paths 是标签路径列表
import os
import numpy as np

for img_path, label_path in zip(img_paths, label_paths):
    if not os.path.exists(img_path):
        print(f"图像文件不存在: {img_path}")
    if not os.path.exists(label_path):
        print(f"标签文件不存在: {label_path}")
try:
    for batch in data_loader:
        pass
except FileNotFoundError as e:
    print(f"文件未找到: {e.filename}")
    raise
