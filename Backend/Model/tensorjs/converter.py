# Python

import tensorflowjs as tfjs
import tensorflow as tf


model = tf.keras.models.load_model("C:\\Users\\jains\\Desktop\\Backend\\Model\\tensorjs\\model.h5")

tfjs.converters.save_keras_model(model)