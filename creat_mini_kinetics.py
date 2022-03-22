import json

TRAIN_PATH = 'resources/minikinetics_train_ytid_list.txt'
VAL_PATH = 'resources/minikinetics_val_ytid_list.txt'

TRAIN_IDS = [line.rstrip('\n') for line in open(TRAIN_PATH).readlines()]
VAL_IDS = [line.rstrip('\n') for line in open(VAL_PATH).readlines()]

VAL_JSON = "resources/kinetics_val.json"
TRAIN_JSON = "resources/kinetics_train.json"

with open(TRAIN_JSON) as f:
    TRAIN_DICT = json.load(f)

with open(VAL_JSON) as f:
    VAL_DICT = json.load(f)

print(len(TRAIN_DICT), len(VAL_DICT))

MINI_TRAIN_DICT = {
    key: TRAIN_DICT[key] for key in TRAIN_IDS
}

MINI_VAL_DICT = {
    key: VAL_DICT[key] for key in VAL_IDS
}

print(len(MINI_TRAIN_DICT), len(MINI_VAL_DICT))

with open('resources/minikinetics_val.json', 'w') as f:
    json.dump(MINI_VAL_DICT, f)

with open('resources/minikinetics_train.json', 'w') as f:
    json.dump(MINI_TRAIN_DICT, f)
