#!/bin/bash

set -e

echo "Compiling TensorFlow ops..."
/app/compile_all.sh

echo "Running inference..."
cd /app/pointnet
exec python2.7 predict.py \
  --cloud true \
  --ckpt logs/scannet/model.ckpt \
  --dataset scannet \
  --set test \
  --n 25

