import os
import shutil

train2014_PATH = '/media/sdc/seg3d/full_new/IORD_train_2018/train2014'
val2014_PATH = '/media/sdc/seg3d/full_new/IORD_train_2018/val2014'

if not os.path.exists(val2014_PATH):
    os.makedirs(val2014_PATH)

rgb_file_list = sorted(os.listdir(train2014_PATH))
rgb_to_move = rgb_file_list[-300:]
for rgb_file_name in rgb_to_move:
    print(rgb_file_name)
    shutil.move(os.path.join(train2014_PATH, rgb_file_name), os.path.join(val2014_PATH, rgb_file_name))

