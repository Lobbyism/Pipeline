POSE_PREDICTIONS_FILE = "/app/data/pose_predictions/predictions.txt"
EXPECTED_POSE_SEQUENCE = [6, 8, 9]
VALID_POSES = {6, 7, 8, 9}


def load_pose_predictions(predictions_file):
    with open(predictions_file, "r") as f:
        return [int(line.strip()) for line in f.readlines() if line.strip().isdigit()]


def filter_relevant_poses(predictions, valid_poses):
    return [p for p in predictions if p in valid_poses]


def match_poses_sequence(poses, target_sequence):
    seq_len = len(target_sequence)
    for i in range(len(poses) - seq_len + 1):
        if poses[i:i + seq_len] == target_sequence:
            return True
    return False


def main():
    poses = load_pose_predictions(POSE_PREDICTIONS_FILE)
    print(poses)
    filtered_poses = filter_relevant_poses(poses, VALID_POSES)
    print(filtered_poses)
    found = match_poses_sequence(filtered_poses, EXPECTED_POSE_SEQUENCE)
    print(found)


if __name__ == '__main__':
    main()
