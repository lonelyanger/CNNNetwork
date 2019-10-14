import numpy as np
import Setting


# 全连接层
class ConnectAll:
    # 收录权值矩阵的集合
    WeightSet = []

    def __init__(self):
        self.LearnRate=Setting.LearnRate
        # Structure应当是一个数组，其长度表示网络层数，
        # 第一个数字是输入向量的维数，最后一个是输出向量的维数，中间是每层神经元数量
        Structure = Setting.ConStructure
        for i in range(0, Structure.__len__() - 1):
            # w[i][j] 表示上一层神经元i的输出对下一层神经元j输入的权值
            w = np.random.rand(Structure[i] * Structure[i + 1]).reshape(Structure[i], Structure[i + 1])
            self.WeightSet.append(w)
        return

    def SigmoidActivator(self, x):
        # sigmoid激活函数
        return 1.0 / (1.0 + np.exp(-x))

    def UpdateW(self, Loss):
        # Dist 输出向量和教师向量的差值
        return

    def Run(self, InputSet):
        # 对输入向量进行前向计算得到结果向量
        Vec = self.InputSetToVec(InputSet)
        for w in self.WeightSet:
            Vec = self.SigmoidActivator(Vec.dot(w))
        return Vec

    def InputSetToVec(self, InputSet):
        Vec = np.array(InputSet).flatten()
        return Vec

    def Update(self, ErrVal):

        return