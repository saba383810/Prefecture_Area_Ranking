import csv
fd = open('KEN_ALL_1.csv')
csv_f = csv.reader(fd)
it = iter(csv_f)
bango = next(it)
ken = next(it)
chiho = next(it)
menseki = next(it)
jinko = next(it)
#面積の降順に順位を数え、指定した順位の都道府県名と面積を返却する関数」
def get_ken_and_value_from_ranking(keys,values,rank):
    valuesInt = [int(i) for i in values] #面積をint型に変更。
    dict_keys_values = dict(zip(keys,valuesInt))#面積と都道府県を辞書型に変更
    Sorted_dict = sorted(dict_keys_values.items(), reverse=True)# 
    number_List = list(range(1, 48))
    dict_Ranking = dict(zip(number_List, Sorted_dict)) #辞書の中に辞書
    ans = list(dict_Ranking[rank])
    return ans
print("都道府県の面積の降順ランキングを作成しました。")
while True:
    rank =  100  #初期化
    while rank<1 or rank>47: # 1〜47以外の数字が入ったらループ
        rank = int(input("何番目の都道府県が知りたいですか？> "))
    ans = get_ken_and_value_from_ranking(ken,menseki,rank)  
    print("\n",ans[0], " 面積 :" , ans[1] , "km^2 " , rank , "位\n" )
    quit_Flug = input("もういちどお調べしますか？(yes or no)> ")
    if quit_Flug[0] == "n" or quit_Flug[0] == "N": #先頭の文字が n か Nの時処理を終了する。
        break
