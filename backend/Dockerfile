FROM python:3.5

COPY ./ /src/

ENV DEBIAN_FRONTEND noninteractive

# apt
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev \
    python3-tk \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Mask_RCNN setup
WORKDIR /src/Mask_RCNN

RUN pip3 install --upgrade pip \
    && pip3 install tensorflow==1.14 keras==2.0.8 \ 
    && pip3 install -r requirements.txt \
    && python3 setup.py install

RUN wget https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5

# gaming-hoge-generator setup
WORKDIR /src

RUN pip install --upgrade pip && pip install \
    flask \
    flask-cors \
    imgaug \
    crontab \
    pycocotools \
    docopt \
    clint \
    tablib

RUN pip install \
    coco

CMD ["python3", "app.py"]
