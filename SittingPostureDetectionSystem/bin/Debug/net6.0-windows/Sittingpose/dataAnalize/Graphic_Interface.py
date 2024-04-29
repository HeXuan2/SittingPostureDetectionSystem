import tkinter
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import joblib
from PIL import ImageTk, Image
import os
import subprocess
import tkinter.messagebox

data = None  # 全局变量，用于保存导入的数据
# 导入Excel表格数据的函数
def import_data():
    global data,name
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])
    if file_path:

        data = pd.read_excel(file_path)
        name = os.path.splitext(os.path.basename(file_path))[0]
        describe = str(data.describe())

        path_text.configure(state='normal')
        path_text.delete("1.0", tk.END)
        path_text.insert(tk.END, file_path)
        path_text.configure(state='disabled')
        describe_text.configure(state='normal')
        describe_text.delete('1.0', tk.END)
        describe_text.insert(tk.END, describe)
        describe_text.configure(state='disabled')

# 进行预测的函数
def predict_data():
    if data is not None:
        model = joblib.load('model/Mlf-Model.pkl')
        features = data[['pitch', 'yaw', 'roll', 'relative_distance', 'HunchValue']]

        predictions = model.predict(features)

        #代码再次使用 joblib.load 函数加载了一个 LabelBinarizer 对象，该对象被保存在了 model/coder.pkl 文件中，用于将预测结果转换为对应的标签。
        # 通过 mlb.inverse_transform(predictions) 函数，将模型的预测结果转换成了对应的标签。
        mlb = joblib.load('model/coder.pkl')
        labels_decoded = mlb.inverse_transform(predictions)
        ## 最后，代码将标签连接成字符串，并将其添加到原始数据集中的一个新列 target 中。
        data['target'] = [', '.join(labels) for labels in labels_decoded]

        output_filename = 'datasets/test/' + name + '(pred).xlsx'  # 使用提取的文件名构建输出文件名

        data.to_excel(output_filename, index=False)
        # 打开预测后的文件
        subprocess.Popen(['start', output_filename], shell=True)
    else:
        answer = tkinter.messagebox.askokcancel('提示','请选择文件')
        if answer:
            pass


# 这段代码使用了 Tkinter 库来创建一个 GUI 界面窗口。Tkinter 是 Python 自带的 GUI 模块，通过它可以方便地创建 GUI 应用程序，提供了许多常见的控件对象，如窗口、按钮、文本框、标签等。
#
# 首先使用 tk.Tk() 函数创建了一个顶层窗口对象 window，设置了窗口标题为 “数据预测”，并设置了窗口的大小为 650x500 像素。接着，代码从文件系统中读取了背景图片文件 “img/background2.png”，调整图片的大小为 650x500 像素，并将其显示在界面上。通过 Image.open 函数和 ImageTk.PhotoImage 函数分别读取和处理图片，最后将图片加到 Label 上以显示。
#
# 最后一行代码使用 attributes 方法为窗口设置了一个不透明度，即设置窗口的透明度为 0.8。
window = tk.Tk()
window.title('数据预测')
window.geometry("650x500")
bg_image = Image.open("img/background2.png")
bg_image = bg_image.resize((650, 500))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
window.attributes("-alpha",0.8)

# 创建按钮
import_button = tk.Button(window, text="选择文件",background='#1E90FF',command=import_data)
import_button.place(relx=0.8,rely=0.08)
predict_button = tk.Button(window, text="点击预测", background='#1E90FF',command=predict_data)
predict_button.place(relx=0.4,rely=0.19,relwidth=0.2,relheight=0.1)
path_text = tk.Text(window, height=1, background='#87CEEA',width=50,state='disabled',font=18)
path_text.place(relx=0.08,rely=0.075,relwidth=0.7,relheight=0.065)
describe_text = tk.Text(window,height=1,background='#B0C4DE',width=50,state='disabled',font=5)
describe_text.place(relx=0.05,rely=0.35,relwidth=0.9,relheight=0.45)
window.mainloop()

