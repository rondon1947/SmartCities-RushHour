from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
import cvlib as cv
import cv2


import json

allImageCount={}

def countVeh(imagePath):
  """
  TO COUNT NO OF VEHICHLES

  Using Tiny Yolo v3  Pre-Trained on Ms-Coco dataset
  
  Arguments:
      imagePath {[string]} -- [path of image]
  """
        
  image = cv2.imread(imagePath)
  #boundingbox, label, conf = cv.detect_common_objects(image)
  boundingbox, label, conf = cv.detect_common_objects(image, confidence=0.25, model='yolov3-tiny')
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
    

def countVehicleVideo(videoPath):
  """[summary]
      
  
  Arguments:
      videoPath {[string]} -- [VideoPath]
  """

  vidObj = cv2.VideoCapture(videoPath)

  count = 0
  
  success = 1

  while success: 

    success, image = vidObj.read()
    

    boundingbox, label, conf = cv.detect_common_objects(image, confidence=0.20, model='yolov3-tiny')
    output_image = draw_bbox(image, boundingbox, label, conf)
    
    car=label.count('car')
    bike=label.count('motorcycle')
    bicycle=label.count('bicycle')
    truck=label.count('truck')
    bus=label.count('bus')

    if not ((bike==0) and (car==0) and (truck==0) and (bus==0) and (bicycle==0)):
        
      print(len(label))
      plt.imshow(output_image)

      plt.show()
      print('Number of Objects in the image is ',"Cars :",str(car)," Bikes :",
            str(bike)," Bicycles :",str(bicycle)," Trucks :",
            str(truck),"Bus :",str(bus))
      
      
    countJson={"Labels":
        {"Cars":car,
          "Bikes":bike,           
          "Bicycles":bicycle,
          "Trucks":truck,
          "Bus":bus
        }          
        }

    allImageCount["img{:d}".format(count)]=countJson 

    count += 1  
              
    
    #boundingbox, label, conf = cv.detect_common_objects(image)

  vidObj.release()
  cv2.destroyAllWindows()  




if __name__ == "__main__":
  # imglist=['indiantraffic.jpeg','traffic.jpeg']
  # for img in imglist:
  #   countVeh(img)
  countVehicleVideo("red.mp4")
  

with open('info.json', 'w') as json_file:
  json.dump(allImageCount, json_file)