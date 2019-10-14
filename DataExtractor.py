import scipy.io as sio
import Setting as S
import numpy


# 数据提取者，函数用于数据提取

def ReadMatToDict(dir):
    a = sio.loadmat(dir)
    # dict_keys(['TrainSL', 'TestSL', 'TrainSet', 'TestSet'])
    # print(a.keys())
    return a


def GetTrainDSFromDict(dict):
    # DS =DataSet
    TDS = dict['TrainSet']
    return TDS


def GetTestDSFromDict(dict):
    # DS =DataSet
    TDS = dict['TestSet']
    return TDS


def GetTrainLFromDict(dict):
    # DS =DataSet
    TSL = dict['TrainSL']
    return TSL


def GetTestLFromDict(dict):
    # DS =DataSet
    TSL = dict['TestSL']
    return TSL



# FlowerDict = ReadMatToDict(S.SourceData_dir)
# TrainSet = GetTrainDSFromDict(FlowerDict)
# TestSet = GetTestDSFromDict(FlowerDict)
# TrainSL = GetTrainLFromDict(FlowerDict)
# TestSL = GetTestLFromDict(FlowerDict)


# 查大小 返回1000
# print(TrainSet.size)
# 提取第一个图片矩阵
# img=TrainSet[0]['data']

# Mat文件中，每张图片数据以三维矩阵存储，训练集以结构数体组存储，其中data字段存放图片的三维矩阵。
# 读取时，python将结构体数组解释成1*n形状矩阵读入，
# 故[0,1]表示第一行第二列的结构体，其中data字段就是图片数据了
# print(TrainSet[0,0]['data'].shape)

# # 图片格式200*200*3
# img=TrainSet[0,1]['data']
# # 读取200*200
# print(img[:,:,0].shape)
# # 读取200*3
# print(img[:,0,:].shape)
# # 读取200*3
# print(img[0,:,:].shape)

# # 标签数据读取使用
# # 1000*1型矩阵
# print(TrainSL.shape)
# # 读取第二个标签值
# print(TrainSL[1,0])
