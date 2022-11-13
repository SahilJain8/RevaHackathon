import tensorflow as tf
import numpy as np
from tensorflow import keras
model=keras.models.load_model("Model/model.h5")
classes_name={0:"Choroidal neovascularization",1:"Diabetic macular edema ",2:"Drusen",3:"Normal"}

def pred(img_path):


    img=tf.keras.utils.img_to_array(img_path)
    image=tf.image.resize(img,(160,160))
    image = np.expand_dims(image, axis=0)
    image=image/255.
    predection=model.predict(image)
    pre=predection.flatten()
    m=pre.max()
    pre=list(pre)
    return str(classes_name[pre.index(m)])   

