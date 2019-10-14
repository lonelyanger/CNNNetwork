import numpy as np
import Setting


# 池化层
class PoolLayer:
    def __init__(self,Plen):
        self.PoolType = Setting.PoolType
        # 缩小的倍数
        self.Poollen=Plen
        return

    def Run(self, InputSet):
        OutPutSet=[]
        for input in InputSet:
            OutPutSet.append(self.Pool(input))
        return OutPutSet

    def Pool(self,Input):
        if self.PoolType == 'Max':
            Output = self.MaxPool(Input)
        if self.PoolType == 'Ave':
            Output = self.AvePool(Input)
        return Output

    def MaxPool(self, Input):
        Output = Input
        return Output

    def AvePool(self, Input):
        InShape=Input.shape
        OutShape=np.array(InShape)/self.Poollen
        Plen=int(OutShape[0])
        poolone=np.ones(self.Poollen)
        poolzero=np.zeros(self.Poollen)
        A=[]
        for i in range(Plen*Plen):
            if i%(OutShape[0]+1)==0:
                A.append(poolone)
            else:
                A.append(poolzero)
        A=np.mat(A).reshape(Plen,int(InShape[0]))
        Output=np.dot(A,Input).dot(A.T)/np.power(self.Poollen,2)
        return Output

    def Update(self, ErrVal):

        return