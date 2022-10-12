
# import pickle

# from flask import Flask,request,app,jsonify,url_for,render_template
# import numpy as np
# import tensorflow_hub as hub
# import tensorflow as tf
# import PIL.Image

# app=Flask(__name__)

# def tensor_to_image(tensor):
#   tensor = tensor*255
#   tensor = np.array(tensor, dtype=np.uint8)
#   if np.ndim(tensor)>3:
#     assert tensor.shape[0] == 1
#     tensor = tensor[0]
#   return PIL.Image.fromarray(tensor)

# def load_img(path_to_img):
#   max_dim = 512
#   img = path_to_img
#   # img = tf.io.read_file(path_to_img)
#   img = tf.image.decode_image(img, channels=3)
#   img = tf.image.convert_image_dtype(img, tf.float32)

#   shape = tf.cast(tf.shape(img)[:-1], tf.float32)
#   long_dim = max(shape)  # type: ignore
#   scale = max_dim / long_dim

#   new_shape = tf.cast(shape * scale, tf.int32)

#   img = tf.image.resize(img, new_shape)
#   img = img[tf.newaxis, :]  # type: ignore
#   return img

# content_path = tf.keras.utils.get_file('jr-NTR-latest-UHD-4.jpg','http://www.teluguclix.com/image/ntr/jr-NTR-latest-UHD-4.jpg')
# style_path = tf.keras.utils.get_file('kandinsky5.jpg','https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg')

# # Load TF Hub module.
# hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
# hub_module = hub.load(hub_handle)
# content_image = load_img(content_path)
# style_image = load_img(style_path)
# stylized_image = hub_module(tf.constant(content_image),tf.constant(style_image))[0]  # type: ignore
# tensor_to_image(stylized_image)

from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')
 
if __name__ == "__main__":
    app.run(debug=True)

   