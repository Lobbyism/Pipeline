#!/bin/bash
set -e

TF_INC="/usr/local/lib/python2.7/dist-packages/tensorflow/include"

echo "Compiling interpolation op..."
cd /app/pointnet/tf_ops/interpolation
bash tf_interpolate_compile.sh

echo "Compiling grouping op..."
cd /app/pointnet/tf_ops/grouping
bash tf_grouping_compile.sh

echo "Compiling sampling op..."
cd /app/pointnet/tf_ops/sampling
bash tf_sampling_compile.sh

exec "$@"