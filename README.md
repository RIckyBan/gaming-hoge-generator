# gaming-hoge-generator

## Requirements
- Python 3.7
- TensorFlow GPU 1.14
- Keras 2.3.1

### Create virtual env (conda)

```bash
conda create -n gaming_hoge python=3.7
source activate gaming_hoge
conda install -c anaconda tensorflow-gpu=1.14 flask flask-cors pillow scikit-image
conda install -c conda-forge pycocotools imgaug keras=2.3.1
pip install opencv-contrib-python
```

## Installation

### For MRCNN model

```bash
cd Mask_RCNN
python3 setup.py install
# download weights
wget https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5
```

### For web client
```bash
# To install client submodule
git submodule update --init --recursive

# build nginx docker image
sudo docker build -f nginx/Dockerfile -t server .

# run nginx container
sudo docker run -d --name server -p 80:80 server
```

## Run applicataion
```
nohup python3 app.py &
```

