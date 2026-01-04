import os
import re
import random
import shutil
def convert_ply_to_txt(ply_filepath, txt_filepath):
    with open(ply_filepath, "r") as ply_file:
        lines = ply_file.readlines()
    try:
        header_end = lines.index("end_header\n") + 1
    except ValueError:
        print(f"Skipping {ply_filepath}: No valid PLY header found.")
        return
    coordinates = [line.split()[:3] for line in lines[header_end:]]
    with open(txt_filepath, "w") as txt_file:
        for coord in coordinates:
            txt_file.write(",".join(coord) + "\n")
    print(f"Conversion complete: {txt_filepath}")
def get_merged_shapes(input_dataset_filepath, output_dataset_filepath):
    """Finds shapes that exist in the output shape file but not in the input shape file."""
    input_shape_file = f"{input_dataset_filepath}/modelnet10_shape_names.txt"
    output_shape_file = f"{output_dataset_filepath}/modelnet10_shape_names.txt"
    with open(input_shape_file, "r") as input_file:
        input_shapes = set(input_file.read().splitlines())
    with open(output_shape_file, "r") as output_file:
        output_shapes = set(output_file.read().splitlines())
    merged_shapes = output_shapes - input_shapes
    return list(merged_shapes)
def process_datasets(input_dataset_filepath, output_dataset_filepath):
    """Updates train and test datasets by splitting newly merged shapes."""
    merge_shape_names = get_merged_shapes(input_dataset_filepath, output_dataset_filepath)
    if not merge_shape_names:
        print("No merged shapes detected. No updates required.")
        return
    with open(f"{output_dataset_filepath}/modelnet10_shape_names.txt", "r") as shapes_name_file:
        shape_names = set(shapes_name_file.read().splitlines())
    test_result = []
    train_result = []
    with open(f"{input_dataset_filepath}/modelnet10_test.txt", "r") as input_test_file:
        for line in input_test_file:
            line_shape = re.sub(r"_\d+", "", line).strip()
            if line_shape in shape_names:
                test_result.append(line)
    with open(f"{input_dataset_filepath}/modelnet10_train.txt", "r") as input_train_file:
        for line in input_train_file:
            line_shape = re.sub(r"_\d+", "", line).strip()
            if line_shape in shape_names:
                train_result.append(line)
    for merge_shape_name in merge_shape_names:
        shape_dir = f"{output_dataset_filepath}/{merge_shape_name}"
        if not os.path.exists(shape_dir):
            print(f"Warning: Directory {shape_dir} not found. Skipping...")
            continue
        shape_files = [os.path.splitext(f)[0] for f in os.listdir(shape_dir)]
        random.shuffle(shape_files)
        num_test_samples = int(len(shape_files) * 0.3)
        num_train_samples = len(shape_files) - num_test_samples
        test_samples = shape_files[:num_test_samples]
        train_samples = shape_files[num_test_samples:num_test_samples + num_train_samples]
        for sample in test_samples:
            test_result.append(sample + "\n")
        for sample in train_samples:
            train_result.append(sample + "\n")
    with open(f"{output_dataset_filepath}/modelnet10_test.txt", "w") as output_test_file:
        for element in test_result:
            output_test_file.write(element)
    with open(f"{output_dataset_filepath}/modelnet10_train.txt", "w") as output_train_file:
        for element in train_result:
            output_train_file.write(element)
    print(f"Updated training and testing datasets with merged shapes: {merge_shape_names}")
# input_dir = "scenes_cloudcompare/chair_human_standing_up/"
# output_dir = "data/modelnet40_normal_resampled/chair_human_standing_up/"
# os.makedirs(output_dir, exist_ok=True)
# for file in sorted(os.listdir(input_dir)):
#     if file.endswith(".ply"):
#         input_ply_filepath = os.path.join(input_dir, file)
#         output_txt_filename = os.path.splitext(file)[0] + ".txt"
#         output_txt_filepath = os.path.join(output_dir, output_txt_filename)
#         convert_ply_to_txt(input_ply_filepath, output_txt_filepath)
#     elif file.endswith(".txt"):
#         input_txt_filepath = os.path.join(input_dir, file)
#         output_txt_filepath = os.path.join(output_dir, file)
#         shutil.copy2(input_txt_filepath, output_txt_filepath)
input_root = "scenes_cloudcompare/"
output_root = "data/modelnet40_normal_resampled/"

for subdir in sorted(os.listdir(input_root)):
    input_dir = os.path.join(input_root, subdir)
    if not os.path.isdir(input_dir):
        continue
    output_dir = os.path.join(output_root, subdir)
    os.makedirs(output_dir, exist_ok=True)
    for file in sorted(os.listdir(input_dir)):
        if file.endswith(".ply"):
            input_ply_filepath = os.path.join(input_dir, file)
            output_txt_filename = os.path.splitext(file)[0] + ".txt"
            output_txt_filepath = os.path.join(output_dir, output_txt_filename)
            convert_ply_to_txt(input_ply_filepath, output_txt_filepath)
        elif file.endswith(".txt"):
            input_txt_filepath = os.path.join(input_dir, file)
            output_txt_filepath = os.path.join(output_dir, file)
            shutil.copy2(input_txt_filepath, output_txt_filepath)
process_datasets(
    "data/modelnet40_normal_resampled_default",
    "data/modelnet40_normal_resampled"
)