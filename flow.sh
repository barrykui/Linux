#!bin/sh
# script for using https://github.com/Jiankai-Sun/dense_flow
VIDEO_DIR=/Disk1/20bn-datasets/tmp/20bn-something-something/*
RGB_DEST=/Disk1/20bn-something-something/20bn-something-something-v1_rgb/
FLOW_DEST=/Disk1/20bn-something-something/20bn-something-something-v1_flow/
DENSE_FLOW=/home/jack/dense_flow/build/extract_gpu
if [ ! -d "${RGB_DEST}" ]; then
  mkdir -p ${RGB_DEST}
  echo ${RGB_DEST}' is created.'
fi
if [ ! -d "${FLOW_DEST}" ]; then
  mkdir -p ${FLOW_DEST}
  echo ${FLOW_DEST}' is created.'
fi
for video in ${VIDEO_DIR};do
    echo ${video}
    if test -f ${video}
    then
        video=${video##*/}
        video=${video%%.*}
        echo ${video}
        mkdir ${RGB_DEST}${video}
        mkdir ${FLOW_DEST}${video}
        ${DENSE_FLOW} -f ${VIDEO_DIR}${video}.mp4 -x ${FLOW_DEST}${video}/${video}-x -y ${FLOW_DEST}${video}/${video}-y -i ${RGB_DEST}${video}/${video} -b 20 -t 1 -d 0 -s 1 -o dir
    fi
done
