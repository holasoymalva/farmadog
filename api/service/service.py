import re
import os
import json

#regex validation for service batch
def read_file():
    filename = os.path.join("../model", 'data.json')
    with open(filename) as data_file:
        mook_data = json.load(data_file) 
        return mook_data, 200

def validate_batch(batch):
    value = False
    if batch == "M216-05":
        value = True
    if batch == "U22S335":
        value = True
    if batch == "X24AU3":
        value = True
    return value