# Script for rename files

import os

for file in os.listdir("."):
     if file.endswith("mp4"):
        os.rename(file,file.zfill(10))
