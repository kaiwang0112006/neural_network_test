import pandas as pd
import numpy as np
from sklearn import datasets, metrics, preprocessing
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_squared_error
import tensorflow as tf
import time
tf.logging.set_verbosity(tf.logging.ERROR)

def input_fn(data_set, FEATURES, LABEL):
    feature_cols = {k: tf.constant(data_set[k].values) for k in FEATURES}
    labels = tf.constant(data_set[LABEL].values)
    return feature_cols, labels

ts = time.time()
label = 'loss'
df_train_ori = pd.read_csv('train_head.csv')
y = df_train_ori[label]
# one hot encode
features = df_train_ori.columns
continuous_features = [feature for feature in features if 'cont' in feature]
categorical_features = [feature for feature in features if 'cat' in feature]
one_hot = pd.get_dummies(df_train_ori[categorical_features])
training_set = df_train_ori.drop(categorical_features, axis=1)
training_set = training_set.join(one_hot)

features = [f for f in training_set.columns if f != label]

# Feature cols
feature_cols = [tf.contrib.layers.real_valued_column(k) for k in features if k != label]

# scale
scaler = MinMaxScaler()
training_set[features] = scaler.fit_transform(training_set[features])

r = []
for step in [1000,5000,10000,50000,100000]:
    ts = time.time()
    # Build 2 layer fully connected DNN with 10, 10 units respectively.
    regressor = tf.contrib.learn.DNNRegressor(feature_columns=feature_cols, hidden_units=[10, 10])
    
    # Fit
    regressor.fit(input_fn=lambda: input_fn(training_set, features, label), steps=step)
    
    pred = regressor.predict(input_fn=lambda: input_fn(training_set, features, label),as_iterable=False)
    #print(y)
    #pred = gener_to_list(y)
    rmse = mean_squared_error(pred,  y)
    te = (time.time()-ts)
    r.append([rmse,te])

print(r)

with open("result_tf",'w') as f:
    for eachline in r:
        f.write("%s\t%s\n" % (str(eachline[0]),str(eachline[1])))