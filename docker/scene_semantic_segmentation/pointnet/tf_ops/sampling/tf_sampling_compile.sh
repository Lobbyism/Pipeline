#/bin/bash
TF_INC="/usr/local/lib/python2.7/dist-packages/tensorflow/include"
/usr/local/cuda/bin/nvcc tf_sampling_g.cu -o tf_sampling_g.cu.o -c -O2 \
    -DGOOGLE_CUDA=1 -x cu -Xcompiler -fPIC -ccbin /usr/bin/g++-5
/usr/bin/g++-5 -std=c++11 tf_sampling.cpp tf_sampling_g.cu.o -o tf_sampling_so.so \
    -shared -fPIC \
    -I"$TF_INC" \
    -I"$TF_INC/external/nsync/public" \
    -I/usr/local/cuda/include \
    -L/usr/local/cuda/lib64 -lcudart \
    -O2 -D_GLIBCXX_USE_CXX11_ABI=0