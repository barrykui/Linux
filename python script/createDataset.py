#!/usr/bin/env python3
'''
This code is used for convert Dataset (RGB, mask) to COCO Style Dataset
Usage: 
pip install pycocotools
python createDataset.py
'''

import datetime
import json
import os
import re
import fnmatch
from PIL import Image
import numpy as np
from pycococreatortools import pycococreatortools
import re
import scipy

import matplotlib.pyplot as plt

ROOT_DIR = '/media/sdc/seg3d/full_new/IORD_train_2018/'
IMAGE_DIR = os.path.join(ROOT_DIR, "train2014")
ANNOTATION_DIR = os.path.join(ROOT_DIR, "masks")
DEPTH_DIR = os.path.join(ROOT_DIR, "depth/")

INFO = {
    "description": "Instance Occlusion Recognition Dataset (IORD)",
    "url": "https://github.com/MVIG",
    "version": "0.1.0",
    "year": 2018,
    "contributor": "MVIG",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}

LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License",
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
    }
]

CATEGORIES = [
    {
        'id': 1,
        'name': 'cube',
        'supercategory': 'shape',
    },
    {
        'id': 2,
        'name': 'stapler',
        'supercategory': 'shape',
    },
    {
        'id': 3,
        'name': 'cup',
        'supercategory': 'shape',
    },
    {
        'id': 4,
        'name': 'orange',
        'supercategory': 'shape',
    },
    {
        'id': 5,
        'name': 'tape',
        'supercategory': 'shape',
    },
    {
        'id': 6,
        'name': 'bowl',
        'supercategory': 'shape',
    },
    {
        'id': 7,
        'name': 'box',
        'supercategory': 'shape',
    },
    {
        'id': 8,
        'name': 'cola',
        'supercategory': 'shape',
    },
    {
        'id': 9,
        'name': 'chip_jar',
        'supercategory': 'shape',
    },
    {
        'id': 10,
        'name': 'juice',
        'supercategory': 'shape',
    },
    {
        'id': 11,
        'name': 'sugar_jar',
        'supercategory': 'shape',
    },
    {
        'id': 12,
        'name': 'spoon',
        'supercategory': 'shape',
    },
    {
        'id': 13,
        'name': 'triangle',
        'supercategory': 'shape',
    },
    {
        'id': 14,
        'name': 'knife',
        'supercategory': 'shape',
    },
    {
        'id': 15,
        'name': 'notebook',
        'supercategory': 'shape',
    },
    {
        'id': 16,
        'name': 'rubik_cube',
        'supercategory': 'shape',
    },
    {
        'id': 17,
        'name': 'laundry_liquid',
        'supercategory': 'shape',
    },
]


def filter_for_jpeg(root, files):
    file_types = ['*.jpeg', '*.jpg']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]

    return files


def filter_for_annotations(root, files, image_filename):
    file_types = ['*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    basename_no_extension = os.path.splitext(os.path.basename(image_filename))[0]
    file_name_prefix = basename_no_extension + '.*'
    # files = [os.path.join(root, f) for f in files]
    # files = [f for f in files if re.match(file_types, f)]
    # files = [f for f in files if re.match(file_name_prefix, os.path.splitext(os.path.basename(f))[0])]
    files = [os.path.join(root, basename_no_extension+'_direct_mask.png')]

    return files


def main():
    coco_output = {
        "info": INFO,
        "licenses": LICENSES,
        "categories": CATEGORIES,
        "images": [],
        "annotations": [],
        "depths": []
    }

    image_id = -1
    segmentation_id = -1

    # filter for jpeg images
    for root, _, files in os.walk(IMAGE_DIR):
        image_files = filter_for_jpeg(root, files)
        
        # go through each image
        for image_filename in image_files:
            image_id += 1
            print('Image file %s' % image_filename)
            image = Image.open(image_filename)
              
#             plt.imshow(image)
#             plt.show()
            
            image_info = pycococreatortools.create_image_info(
                image_id, os.path.basename(image_filename), image.size)
            coco_output["images"].append(image_info)
            
#            depth = np.load(DEPTH_DIR + re.sub("RGB", "depth", image_filename).split("/")[-1].split(".")[0] + ".npy").tolist()
            depth = DEPTH_DIR + re.sub("RGB", "depth", image_filename).split("/")[-1].split(".")[0] + ".npy"
            coco_output["depths"].append(depth)

            # filter for associated png annotations
            for root, _, files in os.walk(ANNOTATION_DIR):
                annotation_files = filter_for_annotations(root, files, image_filename)

                # go through each associated annotation
                for annotation_filename in annotation_files:

                    print(annotation_filename)
                    semantic = scipy.misc.imread(annotation_filename)
                    
#                     plt.imshow(semantic)
#                     plt.show()

                    for category_id in range(1, 18):
                        category_info = {'id': category_id, 'is_crowd': 'crowd' in image_filename}
                    
                      
                        binary_mask = (semantic == category_id)
                
                        if np.sum(binary_mask) < 50:
                            continue
                        segmentation_id += 1
#                         print(category_id)
#                         plt.imshow(binary_mask)
#                         plt.show()
#                         binary_mask = binary_mask.astype(np.uint8)
                        
#                         plt.imshow(binary_mask)
#                         plt.show()
                        annotation_info = pycococreatortools.create_annotation_info(
                            segmentation_id, image_id, category_info, binary_mask,
                            image.size, tolerance=2)
#                         print(annotation_info)
                        """
                        annotation_info = None
                        """
                        if annotation_info is not None:
                            coco_output["annotations"].append(annotation_info)
#             print(image_id)
            # if image_id == 20:
            #     break            
    with open('{}/instances_train2014.json'.format(ROOT_DIR), 'w') as output_json_file:
        json.dump(coco_output, output_json_file)


if __name__ == "__main__":
    main()