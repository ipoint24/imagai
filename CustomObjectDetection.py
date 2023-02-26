from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "modles/yolov3.pt"))
detector.loadModel()

custom_objects = detector.CustomObjects(car=True, motorcycle=True)
detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects,
                                                   input_image=os.path.join(execution_path, "data-images/image3.jpg"),
                                                   output_image_path=os.path.join(execution_path, "data-images/image3custom.jpg"),
                                                   minimum_percentage_probability=30)
# hiding name and probability
# detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image3.jpg"), output_image_path=os.path.join(execution_path , "image3new_nodetails.jpg"), minimum_percentage_probability=30, display_percentage_probability=False, display_object_name=False)
for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
    print("--------------------------------")
