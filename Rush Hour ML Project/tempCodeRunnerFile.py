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
    
def get_frames(video_file):
    
  video = cv2.VideoCapture(video_file)

  if not video.isOpened():
    
    print("[ERROR TO READ VIDEO FILE]", video_file)
    video.release()
    return

  frames = []
  
  frame_count = 0

  while video.isOpened():
    
    status, frame = video.read()

    if not status:
      break
    
  frames.append(frame)

  video.release()

  return frames

def countVehicleVideo(videoPath):
  """[summary]
      
  
  Arguments:
      videoPath {[string]} -- [VideoPath]
  """
  
  frames=get_frames(videoPath)

  for i,image in enumerate(frames):
                
    #image = cv2.imread(imagePath)
    #boundingbox, label, conf = cv.detect_common_objects(image)
    boundingbox, label, conf = cv.detect_common_objects(image, confidence=0.20, model='yolov3-tiny')
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
  imglist=['indiantraffic.jpeg','traffic.jpeg']
  for img in imglist:
    countVeh(img)
  

with open('info.json', 'w') as json_file:
  json.dump(allImageCount, json_file)