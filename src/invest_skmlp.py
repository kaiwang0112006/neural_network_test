import pandas as pd
import numpy as np
from sklearn import datasets, metrics, preprocessing
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_squared_error
import time

ts = time.time()
LABEL_COLUMN = 'loss'
df_train_ori = pd.read_csv('train_head.csv')
features = df_train_ori.columns
continuous_features = [feature for feature in features if 'cont' in feature]
categorical_features = [feature for feature in features if 'cat' in feature]

xf = continuous_features+categorical_features

df_train_x = df_train_ori[xf]
df_train_y = df_train_ori[LABEL_COLUMN]

x_train = pd.get_dummies(df_train_x)

x_train_scale = MinMaxScaler().fit_transform(x_train)

r = []
for step in [1000,5000,10000,50000,100000]:
    print(step)
    nn = MLPRegressor(hidden_layer_sizes=(10,10,10,),max_iter=step)
    nn.fit(x_train_scale,df_train_y)
    pred = nn.predict(x_train_scale)
    
    mse = mean_squared_error(df_train_y,  pred)
    te = (time.time()-ts)
    r.append([mse,te])

print(r)

with open("result_skmlp",'w') as f:
    for eachline in r:
        f.write("%s\t%s\n" % (str(eachline[0]),str(eachline[1])))