# coding:utf-8
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES'] = "0"

def wgn(sequence, snr):
    Ps = np.sum(abs(sequence)**2)/len(sequence)
    Pn = Ps/(10**((snr/10)))
    noise = np.random.randn(len(sequence)) * np.sqrt(Pn)
    signal_add_noise = sequence + noise
    return signal_add_noise

for kv in range(8):
    snr = 30
    dir_path = "nor_data"

    x_train = np.loadtxt( "nor_data/" +str(kv) + ".csv", delimiter=",",dtype=float)
    # print(x_train.shape)
    ne = np.empty(shape=[x_train.shape[0], x_train.shape[1]])

    for ik in range(int(x_train.shape[0] // 80)):
        leg = ik * 80
        x_t = x_train[leg: leg + 80]

        for i in range(x_t.shape[1]):
            ne[leg:leg + 80, i] = wgn(x_t[:, i], snr=snr)

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    data1 = pd.DataFrame(ne)
    data1.to_csv(dir_path + "/" + str(kv) + ".csv", index=False, header=False)
    # np.savetxt(dir_path  + "/"  + "_TEST.txt", test_data)

