import DataExtractor
import Setting
import CNNNetWork

Dict = DataExtractor.ReadMatToDict(Setting.SourceData_dir)
TrainData = DataExtractor.GetTrainDSFromDict(Dict)
TrainL = DataExtractor.GetTrainLFromDict(Dict)

OxfordCNN = CNNNetWork.CNN(TrainData, TrainL)
OxfordCNN.StartTrain()
