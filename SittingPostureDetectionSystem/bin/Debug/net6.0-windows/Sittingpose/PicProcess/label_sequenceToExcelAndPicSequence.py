import pandas as pd
import shutil

#将筛选后的图片重新从1开始命名，并输出到excel中

# 图片所在的文件夹路径
src_folder = "images/OriginGoodImage"
# 目标文件夹路径，用于存储重命名后的图片
dst_folder = "images/fore1"

# 创建label计数器
label_count = {
    '0': 304,
    '1': 528,
    '2': 342,
    '3': 243,
    '4': 403,
    '5': 358,
}

# 读取excel数据

#df = pd.read_excel("data/label1.xlsx", sheet_name="Sheet1")
df = pd.read_excel("data/label1.xlsx", sheet_name="Sheet1",dtype={"label": str})
#df["label"] = df["label"].replace({"2.0": "2","4.0":"4","0.0":"0","1.0":"1","3.0":"3","5.0":"5"})

# 遍历每一行数据
for index, row in df.iterrows():
    # 获取文件名和标签
    picname = row["PicName"]
    label = str(row["label"])
    print(picname,label)
    # 按照下划线切割文件名，获取数字部分
    num_str = picname.split("_")[1].split(".")[0]
    # 构建新文件名，使用 label 数字部分作为前缀，序号部分使用 label 计数器
    new_picname = "{}_{:04d}.jpg".format(label, label_count[str(label)])
    label_count[label] += 1
    # 拼接完整路径
    src_path = "{}/{}".format(src_folder, picname)
    dst_path = "{}/{}".format(dst_folder, new_picname)
    # 复制文件到目标文件夹，并重命名
    shutil.copyfile(src_path, dst_path)

    # 更新数据框中的文件名
    df.at[index, "PicName"] = new_picname.split(".")[0]
    # 更新数据框中的标签
    df.at[index, "label"] = int(label)

# 将更新后的数据保存到新的 Excel 文件中
df.to_excel("data/fore1.xlsx", index=False)



# 定义原始 Excel 表路径、输出 Excel 表路径和图片标签字典（包含每个标签对应的计数器）
# original_excel_path = 'data/label1.xlsx'
# output_excel_path = 'data/output.xlsx'
# pic_labels_dict = {
#     0: 1,
#     1: 1,
#     2: 1,
#     3: 1,
#     4: 1,
#     5: 1
# }
#
# # 从原始 Excel 表中读取数据到 DataFrame 中
# df_original = pd.read_excel(original_excel_path)
#
# # 创建输出 Excel 表的 DataFrame，并设置列名
# df_output = pd.DataFrame(columns=['PicName', 'label'])
#
# # 遍历原始 Excel 表中的每一行数据
# for index, row in df_original.iterrows():
#     # 获取当前行的图片名称和标签
#     pic_name = row['PicName']
#     label = row['label']
#
#     # 构造新的图片名称
#     new_pic_name = f"{label}_{str(pic_labels_dict[label]).zfill(4)}"
#
#     # 更新该标签对应的计数器
#     pic_labels_dict[label] += 1
#
#     # 将当前处理行的信息添加到列表中
#     row_info = [new_pic_name + '.jpg', label]
#     df_row = pd.DataFrame([row_info], columns=['PicName', 'label'])
#
#     # 将当前处理行的信息添加到输出 Excel 表的 DataFrame 中
#     df_output = pd.concat([df_output, df_row], ignore_index=True)
#
# # 保存结果到输出 Excel 表中
# df_output.to_excel(output_excel_path, index=False)

#输出结果
# print(f"处理后的 Excel 表已经保存到 {output_excel_path} 中。")


