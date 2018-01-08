#!/usr/bin/env sh

CAFFE_HOME=../..

SOLVER=./gnet_solver_kitti.prototxt
WEIGHTS=./model_kitti/gnet_yolo_kitti.caffemodel

$CAFFE_HOME/build/tools/caffe train \
    --solver=$SOLVER --weights=$WEIGHTS --gpu=0
