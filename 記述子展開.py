from mordred import Calculator,descriptors
from rdkit import Chem
import pandas as pd

# 3.3.1で作成したデータフレーム(df2)の読み込み
df2 = pd.read_csv('./materials/3_3_1.csv')
df2 = df2.loc[0:5]

#SMILESからMolオブジェクトに変換したものをカラム名MOLとして追加
df2['MOL'] = df2['SMILES'].apply(Chem.MolFromSmiles).values

#df2の最初の５行を表示、MOLが追加されたことを確認
print('==== df2 ====')
print(df2.head())

# 記述子を計算して結果をdf_mordredに格納し最初の５行を表示
calc = Calculator(descriptors, ignore_3D=True)
df_mordred = calc.pandas(df2['MOL'])

print('==== df_mordred ====')
print(df_mordred.head())

#df_mordred内のデータを文字列に変換してdf_descriptorsに格納
df_descriptors = df_mordred.astype(str)

#記述子展開に失敗している箇所（数字ではなく文字になっている部分）をNaにする
mask = df_descriptors.apply(lambda x: x.str.contains('[a-zA-Z]' ,na=False))
df_descriptors = df_descriptors[~mask]

#文字列をfloat32型に変換し、数字がない項目を削除する
df_descriptors = df_descriptors.astype('float32')
df_descriptors = df_descriptors.dropna(axis=1)

#記述子展開した内容の最初の５行を表示
print('==== df_descriptors 数字がない項目削除後 ====')
print(df_descriptors.head())