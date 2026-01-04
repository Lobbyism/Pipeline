FROM python:2.7-slim
WORKDIR /app
RUN pip install numpy
COPY pointnet ./pointnet
COPY main.py .
ENTRYPOINT ["python2.7", "main.py"]