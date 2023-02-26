from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
# 3 detection models
# YOLOv3
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "modles/yolov3.pt"))
# TinyYOLOv3
# detector.setModelTypeAsTinyYOLOv3()
# detector.setModelPath(os.path.join(execution_path, "modles/tiny-yolov3.pt"))
# RetinaNet
# detector.setModelTypeAsRetinaNet()
# detector.setModelPath(os.path.join(execution_path, "modles/retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "data-images/image2.jpg"),
                                             output_image_path=os.path.join(execution_path,
                                                                            "data-images/image2supernew.jpg"),
                                             minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
    print("--------------------------------")
