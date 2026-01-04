FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04
WORKDIR /app
RUN apt-get update && apt-get install -y \
    software-properties-common \
    git \
    curl \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.7 python3.7-dev python3.7-distutils \
    && curl -sS https://bootstrap.pypa.io/pip/3.7/get-pip.py -o get-pip.py && python3.7 get-pip.py \
    && ln -s /usr/bin/python3.7 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --upgrade pip && \
    pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 \
    -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install tqdm
COPY . .
CMD bash -c "python main.py && cd pose_classification && python test_classification.py --log_dir 2025-03-08_17-13 --num_category 10"






