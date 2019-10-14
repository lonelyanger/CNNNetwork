import numpy as np
import Setting
# 卷积层
class ConvLayer:
    def __init__(self,FS):
        # 卷积核数
        self.filternum = Setting.ConvFilterNum
        # 步长
        self.stride=Setting.ConvStride
        # 卷积核集合
        self.FilterSet=[]
        # 卷积形状
        FilterShape=FS
        size=1
        for f in FilterShape:
            size=f*size
        for i in range(0,self.filternum):
            filter=np.random.rand(size).reshape(FilterShape)
            self.FilterSet.append(filter)
        return

    def Run(self,InputSet):
        Output=[]
        # 对输入数据用卷积核进行卷积运算
        for input in InputSet:
            for f in self.FilterSet:
                output=self.Compute(input,f)
                output=self.Normalize(output)
                Output.append(output)
        # 对输出数据进行非负处理
        return Output

    def Compute(self,InputData,Filter):
        Output = np.zeros(np.array(InputData.shape) - np.array(Filter.shape) + 1)
        if len(Output.shape)==3:
            Output = Output[:, :, 0]
            for i in range(Filter.shape[0]):
                for j in range(Filter.shape[1]):
                    for z in range(Filter.shape[2]):
                        Output = Output + Filter[i, j, z] * InputData[i:Output.shape[0] + i, j:Output.shape[1] + j, z]
                    # print((Filter[i,j,z]*InputData[i:Output.shape[0]+i,j:Output.shape[1]+j,z]).shape)
        else:
            for i in range(Filter.shape[0]):
                for j in range(Filter.shape[1]):
                    Output = Output + Filter[i, j] * InputData[i:Output.shape[0] + i, j:Output.shape[1] + j]
        return Output


    def Normalize(self,Input):
        return Input-np.min(Input)

    def Update(self,ErrVal):

        return

    def UpdateFilter(self):
        return

