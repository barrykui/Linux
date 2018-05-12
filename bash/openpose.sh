# Run CMU OpenPose to get the output result
cd /home/wuweilin/openpose
DIR=/Disk1/UCFdataset/rgb
TARGET=/Disk1/UCFdataset/pose
for subdir in `ls ${DIR}`
do
  if [ ! -d "${TARGET}/img/${subdir}" ];then
    mkdir -p ${TARGET}/img/${subdir}
    mkdir -p ${TARGET}/json/${subdir}
    mkdir -p ${TARGET}/yml/${subdir}
    echo ${TARGET}/img/${subdir}
  fi
  CUDA_VISIBLE_DEVICES=1 /home/wuweilin/openpose/build/examples/openpose/openpose.bin --image_dir ${DIR}/${subdir} --write_images ${TARGET}/img/${subdir} --write_keypoint_json ${TARGET}/json/${subdir} --write_keypoint ${TARGET}/yml/${subdir} --display 0
done

