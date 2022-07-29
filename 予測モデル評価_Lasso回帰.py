###################################Lasso回帰による評価###########################################################
#モジュールインポート：Lasso回帰と交差検証
from sklearn.linear_model import Lasso
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd
import pickle

# 3.4.1で作成したX, yの読み込み
X = pd.read_csv('./materials/X.csv')
y = np.load('./materials/y.npy')

#Lasso回帰
model_Lasso =
model_Lasso.

#RMSEとR2の計算と表示
y_pred = model_Lasso.predict(X)

print('==== Lasso回帰計算結果 ====')
print('RMSE:{:6.4f}'.format(np.sqrt(mean_squared_error(y,y_pred))),'R2-score:{:6.4f}'.format(r2_score(y,y_pred)))

#結果の解釈は切片と係数を参照する

#切片の表示
print('==== 切片 ====')
print(model_Lasso.intercept_)


df3 = pd.DataFrame()

df3['記述子'] = X.columns
df3['係数'] = model_Lasso.coef_
df3['係数絶対値'] = abs(model_Lasso.coef_)

print('')
print('==== 重要な項目ランキング ====')
print(df3.sort_values('係数絶対値', ascending=False)[0:5])

# 3.4.1で作成したmodelを読み込み
with open('./materials/model.pkl', 'rb') as f:
    model = pickle.load(f)

#５分割交差検証
print('')
print('==== 交差検証 Lasso回帰 ====')
print(cross_val_score(model_Lasso, X, y, cv= , scoring='neg_mean_absolute_error'))
print('==== 交差検証 線形回帰  ====')
print(cross_val_score(model, X, y, cv= , scoring='neg_mean_absolute_error'))
