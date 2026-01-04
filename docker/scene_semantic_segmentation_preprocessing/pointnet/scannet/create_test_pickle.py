# -*- coding: utf-8 -*-
import os
import pickle
import numpy as np
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scannet'))
scene_dir = os.path.join(BASE_DIR, 'npy_scenes')
test_pickle_path = "/output/scannet_test.pickle"
def create_test_pickle():
    test_xyz, test_labels, scene_names = [], [], []
    for filename in sorted(os.listdir(scene_dir)):
        if filename.endswith('.npy'):
            scene_path = os.path.join(scene_dir, filename)
            scene_points = np.load(scene_path)
            xyz = scene_points[:, :3]
            semantic_labels = scene_points[:, -1].astype(np.int32)
            test_xyz.append(xyz)
            test_labels.append(semantic_labels)
            scene_names.append(filename.replace(".npy", ""))
    print("Total testing scenes: {}".format(len(test_xyz)))
    with open(test_pickle_path, "wb") as f:
        pickle.dump(test_xyz, f, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(test_labels, f, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(scene_names, f, protocol=pickle.HIGHEST_PROTOCOL)
    print("Test pickle file saved at '{}'".format(test_pickle_path))
create_test_pickle()
