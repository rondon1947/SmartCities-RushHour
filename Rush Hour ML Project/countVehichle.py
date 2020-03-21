"""
Yolo-v3 model Pre Trained on MS-COCO DATA SET

"""
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
import cvlib as cv
import cv2

image = cv2.imread('traffic.jpeg')
boundingbox, label, conf = cv.detect_common_objects(image)
output_image = draw_bbox(image, boundingbox, label, conf)

plt.imshow(output_image)
plt.show()
print('Number of Objects in the image is ',"Cars :",str(label.count('car'))," Bikes :",
      str(label.count('motorcycle'))," Bicycles :",str(label.count('bicycle'))," Trucks :",
      str(label.count('truck')),"Bus :",str(label.count('bus')))
