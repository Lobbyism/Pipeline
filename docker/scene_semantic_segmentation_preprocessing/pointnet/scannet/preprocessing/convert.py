import os
import json
import sys
import numpy as np
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)
sys.path.append('../')
sys.path.append('./')
import pc_util
import scannet_util
def convert_ply_to_npy(ply_file, npy_file):
    points = pc_util.read_ply_xyz(ply_file)
    np.save(npy_file, points)
    print("Saved:", npy_file)
convert_ply_to_npy("../scene.ply", "scene.npy")