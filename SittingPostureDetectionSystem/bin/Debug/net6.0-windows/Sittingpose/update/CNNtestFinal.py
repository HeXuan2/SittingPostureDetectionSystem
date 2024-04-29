import time
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.feature_selection import SelectKBest, chi2
import torch
import torch.nn as nn
import torch.nn.functional as F

CLASS_NAMES = ['0', '1', '2', '3']
START_ID = 120000
END_ID = 140000

def set_random_seed(state):
    gens = (np.random.seed, torch.manual_seed)
    for set_state in gens:
        set_state(state)
    """设置随机种子"""
    # torch.manual_seed(state)
def process_data(data):
    """处理训练数据"""
    """处理训练数据"""
    # 获取特征和标签
    features = data[['pitch', 'yaw', 'roll']].values
    labels = data['label'].values
    return features, labels
def get_pred_x(data):
    """处理预测数据"""
    features = data[['pitch', 'yaw', 'roll']].values
    return features
def train_loop(dataloader, model, loss_fn, optimizer):
    """模型训练"""
    model.train()
    for x, y in dataloader:
        x, y = x.to(device), y.long().to(device)
        pred = model(x)
        loss = loss_fn(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
def test_loop(dataloader, model, loss_fn):
    """模型测试"""
    size = len(dataloader.dataset)
    test_loss, correct = 0, 0
    with torch.no_grad():
        model.eval()
        for x, y in dataloader:
            x, y = x.to(device), y.long().to(device)
            pred = model(x)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= size
    correct /= size
    print(f"Test Results: Accuracy: {(100 * correct):>0.1f}%, Loss: {test_loss:>8f}")
def prediction(model, filename):
    """模型预测"""
    with torch.no_grad():
        model.eval()
        preds = []
        data = pd.read_csv(filename)
        pred_x = get_pred_x(data)
        pred_x = torch.Tensor(pred_x).to(device)
        outputs = model(pred_x)
        preds.append(outputs.cpu().numpy())
    preds = np.concatenate(preds)
    df = pd.DataFrame(preds, columns=CLASS_NAMES)
    id_cols = np.arange(START_ID, START_ID + data.shape[0])  # 生成匹配长度的id
    df.insert(0, "id", id_cols)
    df.to_csv(f"predictions.csv", index=False)

#
class Swish(nn.Module):
    def forward(self, x):
        return x * torch.sigmoid(x)

class Model(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(3, 16)  # 隐藏层1,宽度加大
        self.dropout1 = nn.Dropout(0.1)  # dropout1
        self.fc2 = nn.Linear(16, 4)  # 隐藏层2
        # self.dropout2 = nn.Dropout(0.1)  # dropout2
        # self.fc3 = nn.Linear(16, 4)  # 隐藏层3
        # self.fc4 = nn.Linear(16, 4)  # 输出层,输出大小为1,回归任务
        self.lstm = None  # 删除LSTM层
    def forward(self, x):
        self.swish = Swish()
        x = F.leaky_relu(self.fc1(x))
        x = self.dropout1(x)
        x = self.fc2(x)
        # x = F.relu(self.fc2(x))
        # x = self.dropout2(x)
        # x = self.swish(self.fc3(x))  # 使用自定义的Swish激活层
        # x = self.fc4(x)
        # x = self.fc3(x)
        return x
#
if __name__ == '__main__':
    set_random_seed(2)
    df = pd.read_csv('./data/head123total.CSV')
    features, labels = process_data(df)
    # 训练/测试集划分
    X_train, X_test, y_train, y_test = train_test_split(features, labels,
                                                        test_size=0.2, stratify=labels)
    trainset = torch.utils.data.TensorDataset(torch.Tensor(X_train), torch.Tensor(y_train))
    testset = torch.utils.data.TensorDataset(torch.Tensor(X_test), torch.Tensor(y_test))
    train_loader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
    test_loader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = Model().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)
    loss_fn = nn.CrossEntropyLoss()
    torch.save(model.state_dict(), "../../../Tencent/QQtemp/1402050127/FileRecv/modelf.pth")
    for epoch in range(300):
        start = time.time()
        train_loop(train_loader, model, loss_fn, optimizer)
        test_loop(test_loader, model, loss_fn)
        end = time.time()
        print(f'Time elapsed: {end - start:.2f}s')
    prediction(model, "./data/head123totalTest.CSV")
    CLASS_NAMES = ['0', '1', '2', '3']
    START_ID = 120000
    END_ID = 140000