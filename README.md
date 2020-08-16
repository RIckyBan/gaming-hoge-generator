# gaming-hoge-generator

## Requirements
- Python 3.7
- TensorFlow GPU 1.14
- Keras 2.3.1

### Create virtual env (conda)
```bash
conda create -n gaming_hoge python=3.7
conda install -c anaconda tensorflow-gpu=1.14 flask flask-cors
conda install -c conda-forge imgaug keras=2.3.1
```

## Installation

### For MRCNN model

```bash
cd ~/src
git clone https://github.com/matterport/Mask_RCNN
cd Mask_RCNN
python3 setup.py install
# download weights
wget https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5
```

### For web client
```bash
# To install client submodule
git submodule update --init --recursive
```

## Run applicataion
```
nohup python3 app.py &
```