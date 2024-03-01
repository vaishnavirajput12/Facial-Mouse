#training model

import cv2                        #open cv library
import numpy as np                #for mathematical calculation
from os import listdir            #class of os module // when fetching data
from os.path import isfile,join


data_path = "C:/Users/Vaishnavi Rajput/Downloads/aaafaceezip/aaafacee/Face-Recognition-Project-master/Face-Recognition-Project-master/sample"
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

Training_Data,Labels = [],[]

# for i,files in enumerate(onlyfiles):
#     image_path = data_path + onlyfiles[i]
#     images = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
#     Training_Data.append(np.asarray(images,dtype=np.uint8))
#     Labels.append(i)

# Labels = np.asarray(Labels,dtype=np.int32)
for i, file in enumerate(onlyfiles):
    image_path = join(data_path, file)  # Construct full path to the image
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if images is not None:
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
    else:
        print(f"Error: Failed to read image at {image_path}")


model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data),np.asarray(Labels))

print("Congratulations model is TRAINED ... *_*...")

face_classifier = cv2.CascadeClassifier("C:/Users/Vaishnavi Rajput/Downloads/aaafaceezip/aaafacee/virtualmouse/virtualmouse/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
