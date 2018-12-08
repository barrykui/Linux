#/usr/bin/python3
'''
This python script use `dominate` package to generate static html file

Put `dominate_vis.py` together with 
.
├── dominate_vis.py
├── index.html
├── Camera_RGB_BACK
├── Camera_RGB_FRONT
├── Camera_RGB_LEFT
├── Camera_RGB_RIGHT
├── Camera_Semantic
└── Camera_Semantic_vis

run `python dominate_vis.py` to generate `index.html`, open `index.html` with browser
'''

import dominate
from dominate.tags import *
import os


web_path = '.'

with dominate.document('Data Visualization') as web:
    for mod in ['Camera_RGB_FRONT', 'Camera_RGB_RIGHT', 'Camera_RGB_BACK', 'Camera_RGB_LEFT', 'Camera_Semantic', 'Camera_Semantic_vis']:
        h2('Modality-{0}'.format(mod))
        with table(border=1, style='talbe-layout: fixed;'):
            with tr():
                num_img = len(os.listdir('{0}'.format(mod)))
                print('Number of images in folder {0}: {1}'.format(mod, num_img))
                for i in range(num_img):
                    path = '{0}/{1:0>6}.png'.format(mod, str(i))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src=path)
    
    # for mod in ['rgb_filled', 'semantics', 'depth']:
    #     h2('Topdown view')
    #     with table(border=1, style='table-layout: fixed;'):
    #         with tr():
    #             path = 'topdown-{}.png'.format(mod)
    #             with td(style='word-warp: break-world;', halign='center', valign='top'):
    #                 img(style='width:128px', src=path)

with open(os.path.join(web_path, 'index.html'), 'w') as fp:
    fp.write(web.render())

