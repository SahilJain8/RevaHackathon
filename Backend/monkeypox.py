import tensorflow as tf
import numpy as np
from tensorflow import keras
model=keras.models.load_model("Model\monkeypoxmodel.h5")
classes_name={0:"Monkey-Pox",1:"normal "}

def predmonkey(img_path):


    img=tf.keras.utils.img_to_array(img_path)
    image=tf.image.resize(img,(160,160))
    image = np.expand_dims(image, axis=0)
    image=image/255.
    predection=model.predict(image)
    pre=predection.flatten()
    m=pre.max()
    pre=list(pre)
    return str(classes_name[pre.index(m)])   

