from imageai.Classification import ImageClassification
import os
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

execution_path = os.getcwd()

prediction = ImageClassification()
# 4 Models
#  pre-trained “ResNet50” model
# prediction.setModelTypeAsResNet50()
# prediction.setModelPath(os.path.join(execution_path, "modles/resnet50-19c8e357.pth"))
#  pre-trained “MobileNetV2” model
# prediction.setModelTypeAsMobileNetV2()
# prediction.setModelPath(os.path.join(execution_path, "modles/mobilenet_v2-b0353104.pth"))
# pre-trained “InceptionV3” model
prediction.setModelTypeAsInceptionV3()
prediction.setModelPath(os.path.join(execution_path, "modles/inception_v3_google-1a9a5a14.pth"))
# pre-trained “DenseNet121” model
# prediction.setModelTypeAsDenseNet121()
# prediction.setModelPath(os.path.join(execution_path, "modles/densenet121-a639ec97.pth"))

prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "data-images/3.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
