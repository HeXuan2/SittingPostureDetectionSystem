#根据已经0_0001.jpg格式的图片输出excel
import os
import pandas as pd

# 读取图片文件夹
img_folder = 'images/total'
images = os.listdir(img_folder)

# 整理图片的数字信息
image_info_list = []
for img_name in images:
    if not img_name.endswith('.jpg'):
        continue
    img_path = os.path.join(img_folder, img_name)
    info_str = os.path.splitext(img_name)[0]
    seg_pos = info_str.find('_')
    if seg_pos < 1 or seg_pos >= len(info_str)-1:
        continue
    num_before = int(info_str[:seg_pos])
    image_info_list.append({
        'PicName': img_name,
        'label': num_before
    })

# 将数字信息写入Excel表格
df = pd.DataFrame(image_info_list)
#df['label'] = df['label'].apply(lambda x: f'{x}.0')  # 格式化数字
df.to_excel('data/Total.xlsx', index=False)

print('Done.')
