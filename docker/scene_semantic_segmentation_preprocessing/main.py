import sys
import os
import shutil
import subprocess
source_dir = "/input"
target_dir = "/app/pointnet/scannet/preprocessed_scenes"
scenes_file = "/app/pointnet/scannet/scenes_all.txt"
if os.path.exists(target_dir):
    shutil.rmtree(target_dir)
os.makedirs(target_dir)
print("Cleared " + target_dir)
for scene_name in os.listdir(source_dir):
    src = os.path.join(source_dir, scene_name)
    dst = os.path.join(target_dir, scene_name)
    if os.path.isdir(src):
        shutil.copytree(src, dst)
print("Copied scenes from {} to {}".format(source_dir, target_dir))
scene_dirs = sorted(os.listdir(target_dir))
with open(scenes_file, "w") as f:
    for scene in scene_dirs:
        f.write(scene + "\n")
print("Generated scenes_all.txt with {} scenes".format(len(scene_dirs)))
sys.stdout.flush()
print("Running collect_scannet_scenes.py...")
sys.stdout.flush()
subprocess.check_call([
    "python2.7", "pointnet/scannet/preprocessing/collect_scannet_scenes.py"
])
print("Running create_test_pickle.py...")
sys.stdout.flush()
subprocess.check_call([
    "python2.7", "pointnet/scannet/create_test_pickle.py"
])
print("Done.")