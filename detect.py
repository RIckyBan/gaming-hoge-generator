import tensorflow as tf
cfg = tf.ConfigProto()
cfg.gpu_options.allow_growth = True
tf.keras.backend.set_session(tf.Session(config=cfg))

import argparse
<<<<<<< HEAD
import colorsys
=======
import os
import sys
import colorsys
import random
>>>>>>> 2888c9028e9b247dbb9d02cf3b0e12168c400002
import math
import numpy as np
import os
import random
import sys
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

# Root directory of the project
ROOT_DIR = os.path.abspath("../Mask_RCNN/")
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

# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True)


def predict(image):
    results = model.detect([image], verbose=1)
    return results[0]


def main(img_path):
    # Get image
    image = skimage.io.imread(img_path)

    # Run detection
    r = predict(image)
    N = r['rois'].shape[0]

    for i in range(N):
        mask = r['masks'][:, :, i]
        base_image = image.astype(np.uint32).copy()
        masked_images = []
        for j in range(60):
            tmp = visualize.apply_mask(base_image, mask, colorsys.hsv_to_rgb(j/60, 1, 1.0), 0.1)
            masked_images.append(Image.fromarray(tmp.astype('uint8')))
            #skimage.io.imsave("output/output" + str(j) + ".bmp", masked_image.astype(np.uint8))        
        base_image = Image.fromarray(base_image.astype('uint8'))
        base_image.save('out.gif', save_all=True, append_images=masked_images)
        break;

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image')
    args = parser.parse_args()

    main(args.image)
    
    
    
    
    
