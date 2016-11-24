# Introduction

It's a test of different neural network tools for regression. training file is from [kaggle](https://www.kaggle.com/c/allstate-claims-severity), but only extract first 5000 rows of the 
traning set. So we have 848 features and 4999 samples in the data.

I built three neural networks with DNNRegressor from tensorflow, MLPRegressor from sklearn and SGDRegressor from sklearn. 
For DNNRegressor and MLPRegressor, there're two hidden layers and 10 nodes in each layer (layers = [10,10,]). All three Regressor will run 1000, 5000, 10000, 50000 and 100000 steps separately.

RMSE-step relation ship can be found at [here](https://plot.ly/~kaiwang0112006/6/rmse-step/)

<p align="center">
  <img src="https://plot.ly/~kaiwang0112006/6.png" alt="not found"/>
</p>

time-step relation ship can be found at [here](https://plot.ly/~kaiwang0112006/8/time-step/)

<p align="center">
  <img src="https://plot.ly/~kaiwang0112006/8.png" alt="not found"/>
</p>


