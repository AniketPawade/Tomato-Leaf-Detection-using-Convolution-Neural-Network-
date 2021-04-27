#Import necessary libraries
from flask import Flask, render_template, request
 
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image 

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
 
#load model
model =load_model("model/tomato_pred.h5")
 
 
def pred_cot_dieas(img_path, model):
    
  print(img_path)
 
  img = image.load_img(img_path, target_size = (128, 128)) # load image 
  x = image.img_to_array(img)
  x=x/255
  #test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  x = np.expand_dims(x, axis=0)
  #test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
 # result = model.predict(test_image)
  pred = model.predict(x)
   
  pred = np.argmax(pred,axis = 1) # get the index of max value
  
  
 
  if pred == 0:
    return 'Bacterial_spot', 'healthy_plant.html'
  elif pred == 1:
      return 'Early_blight', 'healthy_plant.html'
  elif pred == 2:
      return 'Late_blight', 'healthy_plant.html'  
  elif pred == 3:
      return 'Leaf_Mold', 'healthy_plant.html'
  elif pred == 4:
      return 'Septoria_leaf_spot', 'healthy_plant.html'
  elif pred == 5:
      return 'Spider_mites Two-spotted_spider_mite', 'healthy_plant.html'
  elif pred == 6:
      return 'Target_Spot', 'healthy_plant.html'
  elif pred == 7:
      return 'Tomato_Yellow_Leaf_Curl_Virus', 'healthy_plant.html'
  elif pred == 8:
      return 'Tomato_mosaic_virus', 'healthy_plant.html'
  else:
    return "Healthy", 'healthy_plant.html' 
 
#------------>>pred_cot_dieas<<--end
     
 
# Create flask instance
app = Flask(__name__)
 
# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
     
  
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
                 
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
 
        print("@@ Predicting class......")
        pred, output_page = pred_cot_dieas(file_path, model)
               
        return render_template(output_page, pred_output = pred, user_image = file_path)
        # Make prediction
        # pred = pred_cot_dieas(file_path, model)
        # result=pred
        #return result
        #return None

# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False) 
    
    