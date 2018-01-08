import caffe
import lmdb
import numpy as np
import cv2
from caffe.proto import caffe_pb2

lmdb_env = lmdb.open('lmdb/trainval_lmdb')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe_pb2.Datum()

for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    float_data = datum.float_data
    float_label = np.array(float_data).astype(float)
    label = datum.label
    #continue
    #data = caffe.io.datum_to_array(datum)

    #CxHxW to HxWxC in cv2
    #image = np.transpose(data, (1,2,0))
    image = cv2.imdecode(np.fromstring(datum.data, np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow('cv2', image)
    cv2.waitKey(1)
    print('{},{}'.format(key, label))