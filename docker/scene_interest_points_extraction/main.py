import glob
import os
LABEL_NAMES = ["unannotated", "human", "chair"]
INTERESTED_LABELS = {"human", "chair"}
INPUT_DIR = "input"
OUTPUT_DIR = "output/pose_points"


def label_index_to_name(index):
    try:
        return LABEL_NAMES[index]
    except IndexError:
        return "unannotated"


def process_scene(pred_path, agg_path, output_path):
    with open(pred_path, "r") as f:
        predictions = [int(float(line.strip())) for line in f]
    with open(agg_path, "r") as f:
        points = f.readlines()
    output_lines = []
    for i in range(len(predictions)):
        label_name = label_index_to_name(predictions[i])
        if label_name in INTERESTED_LABELS:
            parts = points[i].strip().split()
            if parts[0] == "v":
                output_lines.append(' '.join(parts[1:4]))
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    with open(output_path, "w") as f:
        for line in output_lines:
            f.write(line + "\n")
    print("Wrote {}".format(output_path))


def main():
    pred_files = glob.glob(os.path.join(INPUT_DIR, "*_pred.txt"))
    print(pred_files)
    for pred_path in pred_files:
        print(pred_path)
        scene_id = os.path.basename(pred_path).split("_pred.txt")[0]
        agg_path = os.path.join(INPUT_DIR, scene_id + "_aggregated.txt")
        output_path = os.path.join(OUTPUT_DIR, scene_id + "_points.txt")
        if os.path.exists(agg_path):
            print("Processing scene {}".format(scene_id))
            process_scene(pred_path, agg_path, output_path)
        else:
            print("Warning: missing aggregated file for {}".format(scene_id))

if __name__ == "__main__":
    main()
