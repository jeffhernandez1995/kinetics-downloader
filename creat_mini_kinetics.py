import json

TRAIN_PATH = 'resources/minikinetics_train_ytid_list.txt'
VAL_PATH = 'resources/minikinetics_val_ytid_list.txt'

TRAIN_IDS = [line.rstrip('\n') for line in open(TRAIN_PATH).readlines()]
VAL_IDS = [line.rstrip('\n') for line in open(VAL_PATH).readlines()]

VAL_JSON = "resources/kinetics_val.json"
TRAIN_JSON = "resources/kinetics_train.json"
CATEGORIES_JSON = "resources/categories.json"

with open(TRAIN_JSON) as f:
    TRAIN_DICT = json.load(f)

with open(VAL_JSON) as f:
    VAL_DICT = json.load(f)

with open(CATEGORIES_JSON) as f:
    CATEGORIES_DICT = json.load(f)

print(len(TRAIN_DICT), len(VAL_DICT))

MINI_TRAIN_DICT = {
    key: TRAIN_DICT[key] for key in TRAIN_IDS
}

MINI_VAL_DICT = {
    key: VAL_DICT[key] for key in VAL_IDS
}

all_labels_train = [
    value["annotations"]["label"] for key, value in MINI_TRAIN_DICT.items()
]
all_labels_val = [
    value["annotations"]["label"] for key, value in MINI_VAL_DICT.items()
]

all_labels = list(set(all_labels_train + all_labels_val))

MINI_CAT_DICT = {}
for key, values in CATEGORIES_DICT.items():
    MINI_CAT_DICT[key] = []
    for val in values:
        if val in all_labels:
            MINI_CAT_DICT[key].append(val)


print(len(MINI_TRAIN_DICT), len(MINI_VAL_DICT))

with open('resources/minikinetics_val.json', 'w') as f:
    json.dump(MINI_VAL_DICT, f)

with open('resources/minikinetics_train.json', 'w') as f:
    json.dump(MINI_TRAIN_DICT, f)

with open('resources/minicategories.json', 'w') as f:
    json.dump(MINI_CAT_DICT, f)

