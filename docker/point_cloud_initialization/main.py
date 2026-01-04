from dagster import asset
from vendor.plyfile import PlyData, PlyElement
import numpy as np
import os
import json
@asset
def initialize_point_cloud():
    input_dir = "/input"
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    processed_files = []
    for filename in os.listdir(input_dir):
        if not filename.endswith(".ply"):
            continue
        input_path = os.path.join(input_dir, filename)
        scene_name = os.path.splitext(filename)[0]
        scene_output_dir = os.path.join(output_dir, scene_name)
        os.makedirs(scene_output_dir, exist_ok=True)
        ply_data = PlyData.read(input_path)
        vertex = ply_data["vertex"]
        n_points = vertex.count
        points_dtype = np.dtype([
            ('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('inst_label', 'u1')
        ])
        points_with_label = np.empty(n_points, dtype=points_dtype)
        points_with_label['x'] = vertex['x']
        points_with_label['y'] = vertex['y']
        points_with_label['z'] = vertex['z']
        points_with_label['inst_label'] = 0
        output_ply_path = os.path.join(scene_output_dir, f"{scene_name}.ply")
        ply_element = PlyElement.describe(points_with_label, 'vertex')
        ply_data = PlyData([ply_element])
        ply_data.text = True
        ply_data.write(output_ply_path)
        segs = {"segIndices": [0] * n_points}
        with open(os.path.join(scene_output_dir, f"{scene_name}.segs.json"), 'w') as f:
            json.dump(segs, f, indent=4)
        aggregation = {
            "sceneId": scene_name,
            "segGroups": [{
                "id": 0,
                "objectId": 0,
                "label": "unannotated",
                "segments": [0]
            }]
        }
        with open(os.path.join(scene_output_dir, f"{scene_name}.aggregation.json"), 'w') as f:
            json.dump(aggregation, f, indent=4)
        print(f"Processed: {filename}")
        processed_files.append(filename)
    return f"Processed {len(processed_files)} file(s): {processed_files}"
if __name__ == "__main__":
    initialize_point_cloud()