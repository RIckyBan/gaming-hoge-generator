import tensorflow as tf
cfg = tf.ConfigProto()
cfg.gpu_options.allow_growth = True
tf.keras.backend.set_session(tf.Session(config=cfg))

import colorsys
import cv2
from flask import Flask, request, send_file, jsonify
from flask_cors import *
import numpy as np
from PIL import Image
import json
import math
import numpy as np
import os
import random
import shutil
import sys
import skimage.io
import uuid
import matplotlib
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)

# Root directory of the project
ROOT_DIR = os.path.abspath("./Mask_RCNN/")
sys.path.append(ROOT_DIR)

from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

# Import COCO config
sys.path.append(
    os.path.join(
        ROOT_DIR,
        "samples/coco/"))  # To find local version
import coco


# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")
# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# COCO Class names
# Index of the class in the list is its ID. For example, to get ID of
# the teddy bear class, use: class_names.index('teddy bear')
class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']


class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

import tensorflow as tf
from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model

sess = tf.Session()
graph = tf.get_default_graph()

# Create model object in inference mode.
set_session(sess)
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True)

@app.route("/test", methods=["GET"])
def test():
    return "gaming hoge generator is running"

@app.route("/server/segmentation", methods=["POST"])
def segmentation():
    image_file = request.files.get('image')

    image = np.array(Image.open(image_file))
    image = np.asarray(image, dtype=np.float32)

    if image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    if max(image.shape) > 3000:
        h, w, _ = image.shape
        image = cv2.resize(image, (int(h/2), int(w/2)))

    global sess
    global graph
    with graph.as_default():
        set_session(sess)
        results = model.detect([image], verbose=1)
    
    r = results[0]
    N = r['rois'].shape[0]

    if N == 0:
        return jsonify({"status":"obejct missing"}), 422

    for i in range(N):
        mask = r['masks'][:, :, i]
        base_image = image.astype(np.uint32).copy()
        masked_images = []
        for j in range(60):
            tmp = base_image.copy()
            tmp = visualize.apply_mask(tmp, mask, colorsys.hsv_to_rgb(j/60, 1, 1.0), 0.5)
            masked_images.append(Image.fromarray(tmp.astype('uint8')))
        img_id = str(uuid.uuid4())
        out_gif = img_id+'.gif'
        base_image = Image.fromarray(base_image.astype('uint8'))
        base_image.save(out_gif, save_all=True, append_images=masked_images, loop=0)
        shutil.move(out_gif, os.path.join('/tmp', out_gif))
        out_gif = os.path.join('/tmp', out_gif)
        break;

    try:
        return send_file(out_gif, attachment_filename='out.gif')
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
