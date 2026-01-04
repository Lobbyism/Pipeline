import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TSV_PATH = os.path.join(BASE_DIR, "scannet-labels.combined.tsv")
g_label_names = ['unannotated', 'human', 'chair']
def get_raw2scannet_label_map():
    lines = [line.rstrip() for line in open(TSV_PATH)]
    lines = lines[1:]
    raw2scannet = {}
    for i in range(len(lines)):
        label_classes_set = set(g_label_names)
        elements = lines[i].split('\t')
        raw_name = elements[0]
        nyu40_name = elements[6]
        if nyu40_name not in label_classes_set:
            raw2scannet[raw_name] = 'unannotated'
        else:
            raw2scannet[raw_name] = nyu40_name
    return raw2scannet
g_raw2scannet = get_raw2scannet_label_map()
