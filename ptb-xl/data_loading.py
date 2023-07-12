import pandas as pd
import numpy as np
import wfdb

def load_raw_data(df, sampling_rate, path):
    if sampling_rate == 100:
        data = [wfdb.rdsamp(path+f) for f in df.filename_lr]
    else:
        data = [wfdb.rdsamp(path+f) for f in df.filename_hr]
    data = np.array([signal for signal, meta in data])
    return data

path = "C:/Users/anas/OneDrive/Bureau/EMINES/stage à l'étranger/Work/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/"
sampling_rate=100

Y = pd.read_csv(path+'ptbxl_database.csv', index_col='ecg_id')

X = load_raw_data(Y, sampling_rate, path)

print(X.shape)