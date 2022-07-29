#モジュールインポート
import re
import pubchempy as pcp
import pandas as pd
import chardet

#ファイル名
file='./materials/name_and_tg_data.csv'
#ファイルオープン
f=open(file, 'rb')
#推定されるエンコードの表示
enc = chardet.detect(f.read())['encoding']
df = pd.read_csv(file,encoding=enc)

# 実行環境の都合上、データの読み込み数に制限
df = df [:10]

#空のリスト
temp_list = []

#モノマー情報の取り出し
print('==== 括弧内の化合物名を取り出し ====')

for i in range(len(df)):
    
    #正規表現を使って括弧内の文字列を抽出
    temp = re.search('(?<=\().*?(?=\))',df['name'][i]) 

    if temp != None:
        #はじめの10件だけを表示
        if i < 10: 
            print(i,df['name'][i],'=>',temp.group())

        #抽出内容をリストに追加
        temp_list.append(temp.group())
    else:
        #はじめの10件だけを表示
        if i < 10: 
            print(i,df['name'][i],'=> None')
        #名前がない場合はNoneに
        temp_list.append(None)

#name2として追加
df['name2'] = temp_list


#pandasのデータフレーム(df)に格納と先頭10行の表示
print('')
print('====','モノマー情報(name2)を追加したdf','====')
print(df[0:10])


#テンポラリに利用したリストと文字列を削除
del temp_list

#PubChemからSMILESを取得

#空のリスト
temp_list = []

for i in range(len(df)):
    try:
        temp_list.append(pcp.get_properties('CanonicalSMILES',df['name2'][i],'name')[0].get('CanonicalSMILES'))
        if i < 10: 
            print(i,'検索キー:',df['name2'][i],'SMILES:',temp_list[i])
    except:
        temp_list.append(None)
        if i < 10: 
            print(i,'検索キー:',df['name2'][i],'SMILES: None')

df['SMILES'] = temp_list

#pandasのデータフレーム(df)に格納と先頭5行の表示
print('')
print('====','SMILESを追加したdf','====')
print(df[0:10])

#テンポラリに利用したリストと文字列を削除
del temp_list