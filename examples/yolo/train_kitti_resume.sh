#!/usr/bin/env sh

CAFFE_HOME=../..

SOLVER=./gnet_solver_kitti.prototxt
SNAPSHOT=./model_kitti/gnet_yolo_kitti_iter_70000.solverstate

$CAFFE_HOME/build/tools/caffe train \
    --solver=$SOLVER --gpu=0 --snapshot=$SNAPSHOT
