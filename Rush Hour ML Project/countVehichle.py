from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
import cvlib as cv
import cv2


import json

allImageCount={}

def count(imagePath):
      """
      TO COUNT NO OF VEHICHLES

      Using Yolo V3 Pre-Trained on Ms-Coco dataset
      
      Arguments:
          imagePath {[string]} -- [path of image]
      """
            
      image = cv2.imread(imagePath)
      boundingbox, label, conf = cv.detect_common_objects(image)
      output_image = draw_bbox(image, boundingbox, label, conf)

      plt.imshow(output_image)
      plt.show()
      print('Number of Objects in the image is ',"Cars :",str(label.count('car'))," Bikes :",
            str(label.count('motorcycle'))," Bicycles :",str(label.count('bicycle'))," Trucks :",
            str(label.count('truck')),"Bus :",str(label.count('bus')))
      
      
      countJson={"Labels":
          {"Cars":label.count('car'),
           "Bikes":label.count('motorcycle'),           
           "Bicycles":label.count('bicycle'),
           "Trucks":label.count('truck'),
           "Bus":label.count('bus')
          }          
          }

      allImageCount[imagePath]=countJson
        
      


if __name__ == "__main__":

  count('indiantraffic.jpeg')
  count('traffic.jpeg')

with open('info.json', 'w') as json_file:  
  json.dump(allImageCount, json_file)
  
