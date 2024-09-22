import os

# 文件夹路径
folder_path =r'D:\GitHub\yuyifenge\PSPNet\VOCdevkit\VOCdevkit\VOC2007\SegmentationClass'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件名是否包含'_leftImg8bit'
    if '_gtFine_labelIds' in filename:
        # 新文件名
        new_filename = filename.replace('_gtFine_labelIds', '')
        # 获取完整的文件路径
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        # 重命名文件
        os.rename(old_file, new_file)

print("文件重命名完成！")
