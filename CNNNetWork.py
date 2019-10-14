import math
import numpy
import ConvLayer
import PoolLayer
import ConnectAll
import Setting


class CNN:
    def __init__(self, TrainData, TLabel):
        self.data = TrainData
        self.label = TLabel
        self.Layer = []
        self.Structure = Setting.CNNStructure
        self.Segema = Setting.Segema
        for i in range(len(self.Structure)):
            if i % 2 == 0:
                layer = ConvLayer.ConvLayer(self.Structure[i])
            else:
                layer = PoolLayer.PoolLayer(self.Structure[i])
            self.Layer.append(layer)
        ConnectLayer = ConnectAll.ConnectAll()
        self.Layer.append(ConnectLayer)
        return

    def StartTrain(self):
        Circle_t=1
        print("训练次数：", Circle_t)
        segema = self.Forward()
        pre_ErrorVal = segema
        while segema > self.Segema and Circle_t<=10:
            print("训练次数：",Circle_t)
            self.Backward(pre_ErrorVal)
            ErrorVal = self.Forward()
            segema = (pre_ErrorVal - ErrorVal) / ErrorVal
            pre_ErrorVal = ErrorVal
            Circle_t=Circle_t+1

    def Forward(self):
        sumerval = 0
        for i in range(self.data.size):
            if i%100==0:
                print("图片",i)
            ImgData = self.data[0, i]['data']
            imglabel = self.label[i, 0]
            erval = self.SingleFW(ImgData, imglabel)
            sumerval = sumerval + erval
        return sumerval

    def SingleFW(self, ImgData, label):
        # InputSet是输入集合，假设上一层是3卷积核的卷积层，那么至少有三个输出矩阵，
        # 我们将它们全加入列表中，对于下一层的输入就是这样一个列表
        InputSet = []
        InputSet.append(ImgData)
        for i in range(len(self.Structure)+1):
            OutputSet = self.Layer[i].Run(InputSet)
            InputSet = OutputSet
        ErrorValue = self.GetErrVal(OutputSet, label)
        return ErrorValue

    def GetErrVal(self, vec, label):
        lvec = numpy.zeros(len(vec))
        lvec[label - 1] = 1
        errval = numpy.linalg.norm(vec - lvec)
        return errval

    def Backward(self,ErrVal):
        for layer in self.Layer:
            layer.Update(ErrVal)
        return

    def StartTest(self):
        return
