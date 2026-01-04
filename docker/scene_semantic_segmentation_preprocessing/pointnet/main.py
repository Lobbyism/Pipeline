import os
import h5py
import pandas as pd
import numpy as np
from tqdm import tqdm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_PATH = os.path.join(BASE_DIR, "data/modelnet40/partial_metadata_modelnet40.csv")
DATASET_PATH = os.path.join(BASE_DIR, "data/modelnet40/ModelNet40")
OUTPUT_DIR = os.path.join(BASE_DIR, "data/modelnet40_ply_hdf5_2048")

NUM_POINTS = 2048

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
df = pd.read_csv(CSV_PATH)

class_map = { cls: i for i, cls in enumerate(df["class"].unique()) }
df["label"] = df["class"].map(class_map)
train_df = df[df["split"] == "train"]
test_df = df[df["split"] == "test"]

train_data, train_labels = [], []
test_data, test_labels = [], []

def save_h5(h5_filename, data, label):
    with h5py.File(h5_filename, 'w') as f:
        f.create_dataset('data', data=data, compression='gzip', compression_opts=4)
        f.create_dataset('label', data=label, compression='gzip', compression_opts=4)

def load_off_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        if lines[0].strip() != "OFF":
            raise ValueError("Invalid OFF file: {}".format(file_path))
        num_vertices, num_faces, _ = map(int, lines[1].split())
        vertices = np.array(
            [map(float, line.split()) for line in lines[2:num_vertices + 2]]
        )
    return vertices

print("Processing train dataset...")
for _, row in tqdm(train_df.iterrows(), total=len(train_df)):
    file_path = os.path.join(DATASET_PATH, row["object_path"])
    if os.path.exists(file_path):
        point_cloud = load_off_file(file_path)
        if len(point_cloud) > NUM_POINTS:
            point_cloud = point_cloud[:NUM_POINTS]
        elif len(point_cloud) < NUM_POINTS:
            point_cloud = np.pad(point_cloud, ((0, NUM_POINTS - len(point_cloud)), (0, 0)), mode='constant')
        train_data.append(point_cloud)
        train_labels.append(row["label"])
print("Processing test dataset...")
for _, row in tqdm(test_df.iterrows(), total=len(test_df)):
    file_path = os.path.join(DATASET_PATH, row["object_path"])
    if os.path.exists(file_path):
        point_cloud = load_off_file(file_path)
        if len(point_cloud) > NUM_POINTS:
            point_cloud = point_cloud[:NUM_POINTS]
        elif len(point_cloud) < NUM_POINTS:
            point_cloud = np.pad(point_cloud, ((0, NUM_POINTS - len(point_cloud)), (0, 0)), mode='constant')
        test_data.append(point_cloud)
        test_labels.append(row["label"])
train_data, train_labels = np.array(train_data), np.array(train_labels)
test_data, test_labels = np.array(test_data), np.array(test_labels)

train_h5_path = os.path.join(OUTPUT_DIR, "train_data.h5")
test_h5_path = os.path.join(OUTPUT_DIR, "test_data.h5")

print("Saving train data to HDF5...")
save_h5(train_h5_path, train_data, train_labels)

print("Saving test data to HDF5...")
save_h5(test_h5_path, test_data, test_labels)

train_files_txt = os.path.join(OUTPUT_DIR, "train_files.txt")
test_files_txt = os.path.join(OUTPUT_DIR, "test_files.txt")

with open(train_files_txt, "w") as f:
    f.write(train_h5_path + "\n")
with open(test_files_txt, "w") as f:
    f.write(test_h5_path + "\n")
print("Conversion completed!")