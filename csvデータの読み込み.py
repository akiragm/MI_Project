#モジュールインポート
import chardet
import pandas as pd

#ファイル名
file='materials/name_and_tg_data.csv'

#ファイルオープン
f=open(file, 'rb')

#推定されるエンコードの表示
enc = chardet.detect(f.read())['encoding']

print('推定されるエンコード形式：',enc)

#ファイルのクローズ
f.close()

#pandasのデータフレーム(df)に格納と先頭5行の表示
df = pd.read_csv(file,encoding=enc)
print('====',file,'====')
print(df.head())