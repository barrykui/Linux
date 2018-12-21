# API example for SUMO challenge

# import sys
# sys.path.append('/mnt/lustre/sunjiankai/App/sumo-challenge/sumo-api')

import sumo
from libfb.py import parutil

# colored_category_tests
from sumo.base.colored_category import ColoredCategory
import matplotlib.pyplot as plt

CSV_PATH = parutil.get_file_path('/mnt/lustre/sunjiankai/Dataset/sample_data/metadata/categories.csv')
colored_category = ColoredCategory(CSV_PATH)
print('colored_category.category_id_to_rgb(133):\n', colored_category.category_id_to_rgb(133))
print('colored_category.category_name_to_rgb(\'shoes\'):\n', colored_category.category_name_to_rgb('shoes'))
print('colored_category.LUT:\n', colored_category.LUT)
lut = colored_category.LUT
print('lut.shape[0]: ', lut.shape[0], 'lut.shape[1]: ', lut.shape[1])

from sumo.base.vector import Vector2, Vector2f, Vector3, Vector3f, on_left, unitize
print('unitize(Vector3(100, 201, 50)): ', unitize(Vector3(100, 201, 50)))

# rot3_tests
from sumo.geometry.rot3 import Rot3, ENU_R_CAMERA
import numpy as np 
wRc = np.transpose(
            np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], dtype=float)
        )
rot = Rot3(wRc)
print(rot.matrix())

# MultiImageTiff
from sumo.geometry.inverse_depth import depth_image_of_inverse_depth_map
from sumo.images.multi_image_tiff import MultiImageTiff, MultiImagePageType

tiff_path = parutil.get_file_path('/mnt/lustre/sunjiankai/Dataset/sample_data/sumo-input/sumo-input.tif')
multi = MultiImageTiff.load(tiff_path)
print('multi.rgb.shape: ', multi.rgb.shape, 'multi.range.shape (Depth): ', multi.range.shape, 'multi.category.shape (Category): ', multi.category.shape, 'multi.instance.shape (Instance): ', multi.instance.shape)
# multi.rgb.shape:  (1024, 6144, 3) multi.range.shape:  (1024, 6144) multi.category.shape:  (1024, 6144) multi.instance.shape:  (1024, 6144)

from sumo.semantic.project_converter import ProjectConverter
from sumo.semantic.project_scene import ProjectScene

glb_path = parutil.get_file_path('/mnt/lustre/sunjiankai/Dataset/sample_data/sumo-output')
meshes_model = ProjectScene.load(glb_path, "bounding_box_sample")
bbox_model = ProjectConverter().run(meshes_model, "bounding_box")
print('bbox_model.elements[\'1087\'].bounds.corners():\n', bbox_model.elements['1087'].bounds.corners())
print('bbox_model.elements[\'1087\'].pose.t', bbox_model.elements['1087'].pose.t)

