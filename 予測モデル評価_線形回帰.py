##########################3.4.1 線形回帰による評価#####################################################################
#モジュールのインポート
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import pandas as pd

# 3.3.1で作成したデータフレーム(df2)の読み込み
df2= pd.read_csv('./materials/3_3_1.csv')
# 3.3.2で作成したデータフレーム(df_descriptors)の読み込み
df_descriptors = pd.read_csv('./materials/3_3_2.csv')

#説明変数
X=pd.DataFrame()

#0-1の値に変換
for col in df_descriptors.columns:
    if df_descriptors[col].var() != 0.0:
        X[col] = (df_descriptors[col]-df_descriptors[col].min())/(df_descriptors[col].max()-df_descriptors[col].min())
        
#目的変数
y = df2['tg'].values.astype('float32')

#線形回帰計算
model = LinearRegression()
model.fit(X,y)

#RMSEとR2の計算と表示
y_pred = model.predict(X)

print('==== 線形回帰計算結果 ====')
print('RMSE:{:6.4f}'.format(np.sqrt(mean_squared_error(y,y_pred))),'R2-score:{:6.4f}'.format(r2_score(y,y_pred)))

#結果の解釈は切片と係数を参照する

#切片の表示
print('==== 切片 ====')
print(model.intercept_)

#係数は数が多いため、記述子と係数と係数の絶対値をデータフレーム(df3)に格納し、
#係数の絶対値が大きい順に並び替え、上位５つを表示する

df3 = pd.DataFrame()

df3['記述子'] = X.columns
df3['係数'] = model.coef_
df3['係数絶対値'] = abs(model.coef_)

print('')
print('==== 重要な項目ランキング ====')
print(df3.sort_values('係数絶対値', ascending=False)[0:5])