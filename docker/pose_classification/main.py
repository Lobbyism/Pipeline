import os
import glob

POSE_POINTS_DIR = "/app/external_data/pose_points"
TARGET_DIR = "/app/pose_classification/data/modelnet40_normal_resampled/unknown"
TEST_LIST_PATH = "/app/pose_classification/data/modelnet40_normal_resampled/modelnet10_test.txt"
TRAIN_LIST_PATH = "/app/pose_classification/data/modelnet40_normal_resampled/modelnet10_train.txt"
SHAPE_NAMES_PATH = "/app/pose_classification/data/modelnet40_normal_resampled/modelnet10_shape_names.txt"


def prepare_test_inputs():
    if os.path.exists(TARGET_DIR):
        for f in glob.glob(os.path.join(TARGET_DIR, "*.txt")):
            os.remove(f)
    else:
        os.makedirs(TARGET_DIR)
    pose_files = glob.glob(os.path.join(POSE_POINTS_DIR, "*.txt"))
    test_lines = []
    for idx, file in enumerate(sorted(pose_files)):
        new_name = "unknown_{:04d}.txt".format(idx)
        target_path = os.path.join(TARGET_DIR, new_name)
        with open(file, "r") as fin, open(target_path, "w") as fout:
            for line in fin:
                parts = line.strip().split()
                fout.write(",".join(parts) + "\n")
        test_lines.append("unknown_{:04d}\n".format(idx))
    with open(TEST_LIST_PATH, "w") as f:
        f.writelines(test_lines)
    with open(TRAIN_LIST_PATH, "w") as f:
        f.writelines(test_lines)
    print("Test input setup complete.")
    print("-> {} files copied to 'unknown/'".format(len(pose_files)))
    print("-> modelnet10_test.txt and modelnet10_train.txt updated.")

    with open(SHAPE_NAMES_PATH, "r") as f:
        lines = f.readlines()
    original_first_label = lines[0].strip()
    lines[0] = "unknown\n"
    with open(SHAPE_NAMES_PATH, "w") as f:
        f.writelines(lines)
    print("-> First shape label '{}' replaced with 'unknown' in shape names.".format(original_first_label))


if __name__ == "__main__":
    prepare_test_inputs()
