def main():
    import matplotlib.pyplot as plt
    import pandas as pd
    from DataTransform import Transform
    from Visible import DrawGraph
    from Model_train import SL_Model
    from Model_train import ML_Model
    import joblib

    #格式转换，xlsx转换成csv
    data0 = pd.read_excel('datasets/train/new_data1.xlsx')
    name = 'testdata'
    Tran = Transform()
    Tran.XtoC(data0,name)

    #数据可视化分析
    data = pd.read_csv('datasets/'+name+'.csv')
    draw = DrawGraph(data,name)

    draw.draw_common()

    target = data['target'].value_counts()
    label = target.index.tolist()
    count = target.values.tolist()

    total = 0
    count_scale = []
    dev_position = []
    colomn_name = data.columns.tolist()
    for i in count:
        total += i
    for j in range(len(count)):
        count_scale.append(count[j] / total)
        dev_position.append(0.05)

    #直方图：
    for i in range(len(colomn_name)-1):
        plt.figure()
        draw.draw_hist(columnname=colomn_name[i],imagename=colomn_name[i])
        plt.figure()
        draw.draw_pointplot(Y=colomn_name[i],imagename=colomn_name[i])
    plt.figure()
    draw.draw_circular_scale(label,count_scale,dev_list=dev_position)
    plt.figure()
    draw.draw_coldiagram(label,count,xlabel='target',ylabel='quantity')

    #建模
    #多分类效果评估
    sl_model = SL_Model(data)
    score_mean = sl_model.score_mean()

    if score_mean > 0.75:
        fit_model,high_score = sl_model.select_model()
        joblib.dump(fit_model,'model/Model.pkl')
    # 当准确率过低时考虑为多标签分类
    else:
        Tran.StoM(data,name)

    data1 = pd.read_csv('datasets/'+name+'_ml.csv')

    #建立多标签分类模型
    Ml_model = ML_Model(data1)
    clt_model,clt_score,clb = Ml_model.ml_model()

    joblib.dump(clt_model, 'model/Mlf-Model.pkl')
    joblib.dump(clb,'model/coder.pkl')
    print(clt_score)

if __name__ == '__main__':
    main()