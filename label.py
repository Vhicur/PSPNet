import os
import shutil

# 定义输入和输出目录
input_dir = r'D:\NanJing\cityspace\gtFine\train'  # Cityscapes 标签路径
output_dir = r'D:\GitHub\yuyifenge\PSPNet\VOCdevkit\VOCdevkit\VOC2007\SegmentationClass'  # VOC格式的输出路径

# 如果输出目录不存在，创建它
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历输入文件夹的所有子文件夹
for city in os.listdir(input_dir):
    city_dir = os.path.join(input_dir, city)

    if os.path.isdir(city_dir):  # 确保是子文件夹
        for filename in os.listdir(city_dir):
            if filename.endswith('labelIds.png'):  # 确认是 Cityscapes 的标签文件
                # 构造原始标签文件路径
                label_path = os.path.join(city_dir, filename)

                # 生成新的标签文件名，将子文件夹名加入文件名以避免重名
                new_filename = city + '_' + filename
                output_path = os.path.join(output_dir, new_filename)

                # 复制标签文件到目标路径
                shutil.copy(label_path, output_path)
                print(f"复制 {output_path}")
