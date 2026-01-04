# import os
# import random
# import pickle
# import numpy as np
# from collections import defaultdict
# SPLIT_RATIO = 0.8
# scene_dir = "npy_scenes/"
# train_pickle_path = "scannet_train.pickle"
# test_pickle_path = "scannet_test.pickle"
# datasets = defaultdict(list)
# for filename in os.listdir(scene_dir):
#     if filename.endswith('.npy'):
#         scene_path = os.path.join(scene_dir, filename)
#         scene_points = np.load(scene_path)
#         xyz = scene_points[:, :3]
#         semantic_labels = scene_points[:, -1].astype(np.int32)
#         datasets["all"].append((xyz, semantic_labels))
# train_xyz, train_labels = [], []
# test_xyz, test_labels = [], []
# for dataset_id in datasets:
#     scenes = datasets[dataset_id]
#     print("Processing dataset '{}' with {} scenes".format(dataset_id, len(scenes)))
#     random.shuffle(scenes)
#     split_index = int(len(scenes) * SPLIT_RATIO)
#     train_scenes = scenes[:split_index]
#     test_scenes = scenes[split_index:]
#
#     train_x = [item[0] for item in train_scenes]
#     train_y = [item[1] for item in train_scenes]
#     test_x = [item[0] for item in test_scenes]
#     test_y = [item[1] for item in test_scenes]
#
#     train_xyz.extend(train_x)
#     train_labels.extend(train_y)
#     test_xyz.extend(test_x)
#     test_labels.extend(test_y)
# print("\nTotal training scenes: {}, Total testing scenes: {}".format(len(train_xyz), len(test_xyz)))
# with open(train_pickle_path, "wb") as f:
#     pickle.dump(train_xyz, f, protocol=pickle.HIGHEST_PROTOCOL)
#     pickle.dump(train_labels, f, protocol=pickle.HIGHEST_PROTOCOL)
# with open(test_pickle_path, "wb") as f:
#     pickle.dump(test_xyz, f, protocol=pickle.HIGHEST_PROTOCOL)
#     pickle.dump(test_labels, f, protocol=pickle.HIGHEST_PROTOCOL)
# print("Pickle files saved: '{}' and '{}'".format(train_pickle_path, test_pickle_path))
import os
import random
import pickle
import numpy as np
from collections import defaultdict
SPLIT_RATIO = 0.8
scene_dir = "npy_scenes/"
train_pickle_path = "scannet_train.pickle"
test_pickle_path = "scannet_test.pickle"
datasets = defaultdict(list)
for filename in os.listdir(scene_dir):
    if filename.endswith('.npy'):
        scene_path = os.path.join(scene_dir, filename)
        scene_points = np.load(scene_path)
        xyz = scene_points[:, :3]
        semantic_labels = scene_points[:, -1].astype(np.int32)
        datasets["all"].append((xyz, semantic_labels, filename.replace(".npy", "")))
train_xyz, train_labels, train_names = [], [], []
test_xyz, test_labels, test_names = [], [], []
for dataset_id in datasets:
    scenes = datasets[dataset_id]
    print("Processing dataset '{}' with {} scenes".format(dataset_id, len(scenes)))
    random.shuffle(scenes)
    split_index = int(len(scenes) * SPLIT_RATIO)
    train_scenes = scenes[:split_index]
    test_scenes = scenes[split_index:]

    train_xyz.extend([item[0] for item in train_scenes])
    train_labels.extend([item[1] for item in train_scenes])
    train_names.extend([item[2] for item in train_scenes])

    test_xyz.extend([item[0] for item in test_scenes])
    test_labels.extend([item[1] for item in test_scenes])
    test_names.extend([item[2] for item in test_scenes])
print("\nTotal training scenes: {}, Total testing scenes: {}".format(len(train_xyz), len(test_xyz)))
with open(train_pickle_path, "wb") as f:
    pickle.dump(train_xyz, f, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(train_labels, f, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(train_names, f, protocol=pickle.HIGHEST_PROTOCOL)
with open(test_pickle_path, "wb") as f:
    pickle.dump(test_xyz, f, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(test_labels, f, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(test_names, f, protocol=pickle.HIGHEST_PROTOCOL)
print("Pickle files saved: '{}' and '{}'".format(train_pickle_path, test_pickle_path))
