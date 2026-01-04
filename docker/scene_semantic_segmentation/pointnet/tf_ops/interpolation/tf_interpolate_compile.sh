#/bin/bash
TF_INC="/usr/local/lib/python2.7/dist-packages/tensorflow/include"
g++ -std=c++11 tf_interpolate.cpp -o tf_interpolate_so.so -shared -fPIC \
  -I"$TF_INC" \
  -I"$TF_INC/external/nsync/public" \
  -I/usr/local/cuda-8.0/include \
  -L/usr/local/cuda-8.0/lib64 -lcudart \
  -O2 -D_GLIBCXX_USE_CXX11_ABI=0

