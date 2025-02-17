import pandas as pd
import numpy as np
from scipy.stats import zscore

def z_score_manipulation(df):
    df_zscores = df.copy()
    df_zscores[df.select_dtypes(include='number').columns] = df.select_dtypes(include='number').apply(zscore)
    print(df_zscores)
    return df_zscores

def sigmoid_manipulation(df):
    def sigmoid(x):
        return 100 / (1 + np.exp(-x))
    
    df_sigmoid = df.copy()
    df_sigmoid[df.select_dtypes(include='number').columns] = df.select_dtypes(include='number').apply(sigmoid)
    print(df_sigmoid)
    return df_sigmoid


data = {
    'A': [12, 25, 31, 69],
    'B': [5.5, 6.5, 7.5, 11],
    'C': ['x', 'y', 'z', 'a']
}

df = pd.DataFrame(data)

sigmoid_manipulation(z_score_manipulation(df))
