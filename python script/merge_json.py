#-*- coding:utf-8 -*-
# merge two json files generated by LABELME to avoid repeated tags.

import os
import json
from types import *

PREVIOUS_DIRECTORY = '.'
CURRENT_DIRECTORY = '.'
COLORMAP={"yellow_cube":{"lineColor": [0, 255, 0, 128], "fillColor": [255, 0, 0, 128]}
}

for file in os.listdir(CURRENT_DIRECTORY):
    if(os.path.splitext(file)[1] != '.json'):
        continue
    else:
        previous_file_name = os.path.join(PREVIOUS_DIRECTORY, file)
        current_file_name = os.path.join(CURRENT_DIRECTORY, file)

        previous_file = json.loads(open(previous_file_name, 'r').read())
        current_file = json.loads(open(current_file_name, 'r').read())

        previous_file['shapes'].extend(current_file['shapes'])
        current_file['shapes']  = previous_file['shapes']

        with open(current_file_name, 'w') as f:
            json.dump(current_file_name, f, indent=1)
            print(current_file_name + " Finished!")

