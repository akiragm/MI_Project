#モジュールインポート
import pandas as pd
# 3.2.2で作成したデータフレーム(df)の読み込み
df = pd.read_csv('./materials/3_2_2.csv')

#リストワイズ削除、NaNがあるレコードは消す
df2 = df.dropna()

#CC=CとC(CO)Oは消す、それ以外を残す
df2 = df2[df2['SMILES']!='CC=C']
df2 = df2[df2['SMILES']!='C(CO)O']

#リインデックス
df2 = df2.reset_index(drop=True)

#比較表示
print('==== df ====')
print(df[0:10])
print('')
print('==== df2 ====')
print(df2[0:10])