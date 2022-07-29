#モジュールインポート：xgboost回帰
import xgboost as xgb
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd
import pickle

# 3.4.1で作成したX, yの読み込み
X = pd.read_csv('./materials/X.csv')[:7]
y = np.load('./materials/y.npy')[:7]


#Xgboost回帰
model_xgb = xgb.XGBRegressor()
model_xgb.fit(X,y)

#RMSEとR2の計算と表示
y_pred = model_xgb.predict(X)

print('==== xgboost回帰計算結果 ====')
print('RMSE:{:6.4f}'.format(np.sqrt(mean_squared_error(y,y_pred))),'R2-score:{:6.4f}'.format(r2_score(y,y_pred)))


#特徴量重要度ランキング
df3 = pd.DataFrame()

df3['記述子'] = X.columns
df3['特徴量重要度'] = model_xgb.feature_importances_

print('')
print('==== 重要な項目ランキング ====')
print(df3.sort_values('特徴量重要度', ascending=False)[0:5])