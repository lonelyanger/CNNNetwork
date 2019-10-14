import numpy as np

SourceData_dir = './data/OxfordFlower10class2.mat'

# CNN网络参数
# 收敛值
Segema = 0.01
# 数据维数
ImgDepth = 3
# 网络结构参数
# 自设定是规定一层卷积层接一层池化层
Conv1 = [3, 3, 3]
Pool1 = 22
Conv2 = [3, 3]
Pool2 = 7
CNNStructure = []
CNNStructure.append(Conv1)
CNNStructure.append(Pool1)
CNNStructure.append(Conv2)
CNNStructure.append(Pool2)

# 卷积层参数
# 卷积核数
ConvFilterNum = 3
# 步长
ConvStride = 1
# 卷积形状
# ConvFilterShape=[5,5,3]

# 池化层参数
# 池化类型
# PoolType = ['Max','Ave']
PoolType = 'Ave'
# 池化范围
# PoolRange=[2,2]


# 全连接层参数
# Structure应当是一个数组，其长度表示网络层数，
# 第一个数字是输入向量的维数，最后一个是输出向量的维数，
# 中间是每层神经元数量
ConStructure = [9, 10, 10]
LearnRate=0.1
