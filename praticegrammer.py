import scipy.io as sio
import Setting as S
import numpy
from PIL import Image

def ReadMatToDict(dir):
    a=sio.loadmat(dir)
    # dict_keys(['TrainSL', 'TestSL', 'TrainSet', 'TestSet'])
    print(a.keys())
    return a

def GetTrainDSFromDict(dict):
    # DS =DataSet
    TDS=dict['TrainSet']
    return TDS



def readimage(name):
    img=Image.open(S.Image_dir+name)
    numpy.asarray(img)
    return numpy.asarray(img)


# ReadMatToDict(S.SourceData_dir)
# imgdata=readimage('image_00001.jpg')
# print(type(imgdata.shape))

# myshape=(2,2,3)
# a=numpy.random.rand(myshape[0]*myshape[1]*myshape[2]).reshape(3,2,2)
# print(a)
# a=numpy.arange(12).reshape(myshape)3
# b=(9,8,7)
# print(b[2])
# for i in range(0,10):
#     print(i)
# label=readlabel(S.DataLabel_dir)

# WS=[]
# Wstruct=(2,3,3,2)
# for i in range(0,Wstruct.__len__()-1):
#     w=numpy.random.rand(Wstruct[i]*Wstruct[i+1]).reshape(Wstruct[i],Wstruct[i+1])
#     print(w[0][0])
#     WS.append(w)
#     # print(WS[i])


# vector=numpy.random.rand(4)
# ans=numpy.exp(-vector)
# print(ans)



# # 计算向量的欧式距离
# vec=numpy.zeros(15).reshape(15,1)
# lvec=numpy.zeros(vec.shape)
# lvec[1]=1
# print(lvec)
# print(numpy.linalg.norm(vec-lvec))

# class A:
#     def __init__(self):
#         return
# a=A
# print(a.__name__)

# a=[1,2,5]
# print(len(a))


# A=numpy.random.rand(27).reshape(3,3,3)-1
# print(A-numpy.min(A))

# CS=[2,1,2]
# CNN=[]
# CNN.append(3)
# CNN.append(CS)
# print(CNN[1][0])


# InputData=numpy.random.rand(243).reshape(9,9,3)
# Filter=numpy.random.rand(27).reshape(3,3,3)

# def Compute(InputData, Filter):
#
#     Output=numpy.zeros(numpy.array(InputData.shape)-numpy.array(Filter.shape)+1)
#     Output=Output[:,:,0]
#     print(Output.shape)
#     for i in range(Filter.shape[0]):
#         for j in range(Filter.shape[1]):
#             for z in range(Filter.shape[2]):
#                 Output = Output +Filter[i,j,z]*InputData[i:Output.shape[0]+i,j:Output.shape[1]+j,z]
#                 # print((Filter[i,j,z]*InputData[i:Output.shape[0]+i,j:Output.shape[1]+j,z]).shape)
#     return Output
#
#
#
# data=Compute(InputData,Filter)
# print(data.shape)


# 池化功能测试
# poollen=3
# InputData=numpy.random.rand(81).reshape(9,9)
# Inshape=InputData.shape
# Outshape=numpy.array(Inshape)/3
# a=int(Outshape[0])
# b=int(Outshape[1])
# poolone=numpy.ones(poollen)
# poolzero=numpy.zeros(poollen)
# OutPut=[]
# for i in range(a):
#     for j in range(b):
#         if (i*Outshape[0]+j)%(Outshape[0]+1)==0:
#             OutPut.append(poolone)
#         else:
#             OutPut.append(poolzero)
# OutPut=numpy.mat(OutPut).reshape(a,int(Inshape[0]))
# OutPut=numpy.dot(OutPut,InputData).dot(OutPut.T)/numpy.power(poollen,2)
# print(OutPut)
# print(InputData)

# Input=numpy.random.rand(9).reshape(3,3)
t=numpy.random.rand(24).reshape(12,2)
a=numpy.random.rand(6).reshape(2,3)
b=numpy.random.rand(3)
# vec=Input.flatten()

VecSet=[]
for i in range(3):
    Input = numpy.random.rand(4).reshape(2, 2)
    VecSet.append(Input.flatten())
Vec = numpy.mat(VecSet).flatten()
v=(Vec.dot(t)).dot(a)
print(numpy.linalg.norm(v-b))

