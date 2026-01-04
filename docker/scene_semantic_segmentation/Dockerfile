FROM nvcr.io/nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04
RUN apt-get update && apt-get install -y \
    gcc-5 g++-5 \
    perl \
    make \
    curl \
    build-essential
RUN apt-get install -y python2.7
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && \
    python2.7 get-pip.py && \
    rm get-pip.py
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org tensorflow-gpu==1.2.0
WORKDIR /app
COPY pointnet/ ./pointnet/
COPY compile_and_run.sh /app/compile_and_run.sh
COPY compile_all.sh /app/compile_all.sh
RUN chmod +x /app/compile_all.sh /app/compile_and_run.sh
ENTRYPOINT ["/app/compile_and_run.sh"]