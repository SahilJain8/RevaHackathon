import tensorflow as tf
import numpy as np
from tensorflow import keras
model=keras.models.load_model("Model/braintumour.h5")
name={0:"Glioma",1:"meningioma",2:"Normal",3:"pituitary"}

def predbrain(img_path):


    img=tf.keras.utils.img_to_array(img_path)
    image=tf.image.resize(img,(160,160))
    image = np.expand_dims(image, axis=0)
    image=image/255.
    predection=model.predict(image)
    pre=predection.flatten()
    m=pre.max()
    pre=list(pre)
    return str(name[pre.index(m)])   

