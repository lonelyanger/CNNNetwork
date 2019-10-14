clc;
clear;
load('OxfordFlower10class.mat');
ll=TrainSL(1);
NewL=1;
for i=1:length(TrainSL)
    if TrainSL(i)~=ll
        ll=TrainSL(i);
        NewL=NewL+1;  
    end
        TrainSL(i)=NewL;
end

ll=TestSL(1);
NewL=1;
for i=1:length(TestSL)
    if TestSL(i)~=ll
        ll=TestSL(i);
        NewL=NewL+1;  
    end
        TestSL(i)=NewL;
end