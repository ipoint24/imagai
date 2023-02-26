# Image Classification
* [OlafenwaMoses/ImageAI](https://github.com/OlafenwaMoses/ImageAI)

In ImageAi sind 4 verschiedene Algorithmen und Modeltypen für die Bilderkennung enthalten.
## ResNet-50
ResNet-50 is a 50-layer convolutional neural network (48 convolutional layers, one MaxPool layer, and one average pool layer). Residual neural networks are a type of artificial neural network (ANN) that forms networks by stacking residual blocks.
* [ResNet50](https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/resnet50-19c8e357.pth) by Microsoft Research (Size = 98 mb, fast prediction time and high accuracy)

## MobileNetV2
MobileNetV2 is a convolutional neural network architecture that seeks to perform well on mobile devices. 
* [MobileNetV2](https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/mobilenet_v2-b0353104.pth) (Size = 4.82 mb, fastest prediction time and moderate accuracy)

## InceptionV3
Inception v3[1][2] is a convolutional neural network for assisting in image analysis and object detection, and got its start as a module for GoogLeNet. It is the third edition of Google's Inception Convolutional Neural Network, originally introduced during the ImageNet Recognition Challenge. 
* [InceptionV3](https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/inception_v3_google-1a9a5a14.pth) by Google Brain team (Size = 91.6 mb, slow prediction time and higher accuracy)

## DenseNet121

* [DenseNet121](https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/densenet121-a639ec97.pth) by Facebook AI Research (Size = 31.6 mb, slower prediction time and highest accuracy)

# Object Detection

## RetinaNet
RetinaNet is one of the best one-stage object detection models that has proven to work well with dense and small scale objects
* [RetinaNet](https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth) (Size = 130 mb, high performance and accuracy, with longer detection time)

The object detection model (RetinaNet) supported by ImageAI can detect 80 different types of objects. They include:
```text
person,  bicycle,  car, motorcycle, airplane, bus, train,  truck,  boat,  traffic light,  fire hydrant, stop_sign,
parking meter,   bench,   bird,   cat,   dog,   horse,   sheep,   cow,   elephant,   bear,   zebra,
giraffe,   backpack,   umbrella,   handbag,   tie,   suitcase,   frisbee,   skis,   snowboard,
sports ball,   kite,   baseball bat,   baseball glove,   skateboard,   surfboard,   tennis racket,
bottle,   wine glass,   cup,   fork,   knife,   spoon,   bowl,   banana,   apple,   sandwich,   orange,
broccoli,   carrot,   hot dog,   pizza,   donot,   cake,   chair,   couch,   potted plant,   bed,
dining table,   toilet,   tv,   laptop,   mouse,   remote,   keyboard,   cell phone,   microwave,   oven,
toaster,   sink,   refrigerator,   book,   clock,   vase,   scissors,   teddy bear,   hair dryer,   toothbrush.
```

## YOLOv3
YOLOv3 uses a few tricks to improve training and increase performance, including: multi-scale predictions, a better backbone classifier, real-time detection and more. 
* [YOLOv3](https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt) (Size = 237 mb, moderate performance and accuracy, with a moderate detection time)
## TinyYOLOv3
s. YOLOv3
* [TinyYOLOv3](https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/tiny-yolov3.pt) (Size = 34 mb, optimized for speed and moderate performance, with fast detection time)

# Bugs

* Bug: `[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.`
* Fix: `export USE_NNPACK=0`
---
* Bug: Deprecated Warning `The parameter 'pretrained' is deprecated since 0.13` 
* Fix:
```python
# Deprecated
from torchvision import models
model = models.resnet50(pretrained=True)
# New
from torchvision import models
model = models.resnet50(weights='ResNet50_Weights.DEFAULT')
```

* Bug:  `No module named 'tkinter'`
* Fix: `sudo apt-get install python3-tk`
