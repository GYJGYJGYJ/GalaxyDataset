import numpy as np
# array = [[1, 2], 3]
#
# np.save("./test.npy", array)
#
# print(np.load("./test.npy", allow_pickle=True))

# import yaml
# import os
# f = open("./config.yaml")
# y = yaml.load(f)
# print(y)
# print(y["split_mode"])


# def readYaml(path, args):
#     if not os.path.exists(path):
#         return args
#     f = open(path)
#     config = yaml.load(f)
#     args.node_num = int(config[0]["node_num"])
#     args.isaverage_dataset_size = config[0]["isaverage_dataset_size"]
#     args.dataset_size_list = config[0]["dataset_size_list"]
#     args.split_mode = int(config[0]["split_mode"])
#     args.node_label_num = config[0]["node_label_num"]
#     args.isadd_label = config[0]["isadd_label"]
#     args.add_label_rate = float(config[0]["add_label_rate"])
#     args.isadd_error = config[0]["isadd_error"]
#     args.add_error_rate = float(config[0]["add_error_rate"])
#     return args
#
# readYaml("./config.yaml")

array = [
[5582, 686, 682, 793, 1475, 980, 847, 882, 1182, 1267],
[722, 5890, 682, 793, 1475, 980, 847, 882, 1182, 1267],
[722, 686, 4500, 793, 1475, 980, 847, 882, 1182, 1267],
[722, 686, 682, 3430, 1475, 980, 847, 882, 1182, 1267],
[722, 686, 682, 793, 4300, 980, 847, 882, 1182, 1267],
[722, 686, 682, 793, 1475, 5947, 847, 882, 1182, 1267],
[722, 686, 682, 793, 1475, 980, 4804, 882, 1182, 1267],
[722, 686, 682, 793, 1475, 980, 847, 4277, 1182, 1267],
[722, 686, 682, 793, 1475, 980, 847, 882, 5138, 1267],
[722, 686, 682, 793, 1475, 980, 847, 882, 1182, 3900],
]
array = np.array(array)
print(array.T.tolist())

# [[5582, 722, 722, 722, 722, 722, 722, 722, 722, 722], [686, 5890, 686, 686, 686, 686, 686, 686, 686, 686], [682, 682, 4500, 682, 682, 682, 682, 682, 682, 682], [793, 793, 793, 3430, 793, 793, 793, 793, 793, 793], [1475, 1475, 1475, 1475, 4300, 1475, 1475, 1475, 1475, 1475], [980, 980, 980, 980, 980, 5947, 980, 980, 980, 980], [847, 847, 847, 847, 847, 847, 4804, 847, 847, 847], [882, 882, 882, 882, 882, 882, 882, 4277, 882, 882], [1182, 1182, 1182, 1182, 1182, 1182, 1182, 1182, 5138, 1182], [1267, 1267, 1267, 1267, 1267, 1267, 1267, 1267, 1267, 3900]]