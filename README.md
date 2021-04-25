# Tomato-Leaf-Detection-using-Convolution-Neural-Network
Tomato is the most popular crop in the world,it is the crop which is cultivated worldwide. India ranked 2 in the production of tomato. However, the quality and quantity of tomato crop goes down due to the various kinds of diseases. So, to detect the disease a deep learning-based approach with local deployment used. For the disease detection and classification, a Convolution Neural Network based approach is applied. 


**Dataset**

Images of Tomato disease have been taken from Plant Village dataset. The dataset includes over 50,000 images of 14 crops, such as tomatoes, potatoes, grapes, apples, corn, blueberry, raspberry, soybeans, squash and strawberry. We selected tomato as our target crop.

![image](https://user-images.githubusercontent.com/82939124/115994937-abee6f80-a5f6-11eb-8f61-3c41f661ce7b.png)

There are mainly nine types of diseases in tomato: 1) Target Spot, 2) Mosaic virus, 3) Bacterial spot, 4) Late blight, 5) Leaf Mold, 6) Yellow Leaf Curl Virus, 7) Spider mites: Two-spotted spider mite, 8) Early blight and 9) Septoria leaf spot. In proposed work, there are 10000 images in training dataset, 7000 images in validation dataset and 500 images in testing dataset. Out of 10000 training images, 1000 images belong to healthy category and 1000 images belong to each tomato disease category described above.

**Model Summary**

Model: "sequential"
_________________________________________________________________
Layer (type)        |         Output Shape         |     Param #   
=================================================================
conv2d (Conv2D)              (None, 126, 126, 32)      896       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 63, 63, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 61, 61, 64)        18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 30, 30, 64)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 28, 28, 128)       73856     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 14, 14, 128)       0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 12, 12, 256)       295168    
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 6, 6, 256)         0         
_________________________________________________________________
dropout (Dropout)            (None, 6, 6, 256)         0         
_________________________________________________________________
flatten (Flatten)            (None, 9216)              0         
_________________________________________________________________
dense (Dense)                (None, 128)               1179776   
_________________________________________________________________
dropout_1 (Dropout)          (None, 128)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 256)               33024     
_________________________________________________________________
dropout_2 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                2570      
=================================================================
Total params: 1,603,786
Trainable params: 1,603,786
Non-trainable params: 0

**Prediction Result**

![image](https://user-images.githubusercontent.com/82939124/115995404-ad209c00-a5f8-11eb-9d0e-b37180c2eeb5.png)

![image](https://user-images.githubusercontent.com/82939124/115995416-b9a4f480-a5f8-11eb-8cd7-c866019b4d44.png)

