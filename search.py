def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)


def serch_index(sorted_array, target_number):

    # ここから記述
    low = 0
    high = len(sorted_array)-1

    while(low <= high):
        mid = low + int((high-low)/2)
        if sorted_array[mid] == target_number:
            return mid
        elif sorted_array[mid] < target_number:
            low = mid+1
        else:
            high = mid - 1
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1


if __name__ == '__main__':
    main()


# 探索対象の配列から、探索する数値のindexを返却するメソッドを実装してください
# 探索対象の配列は「1つ以上の要素を持つ、昇順にソートされた重複のない整数の配列」です
# ただし、以下の条件を満たすアルゴリズムを用いて実装してください
# 「配列の中間の値」と「探索対象の数値」の大小を比較し、中間から前後のどちらかに探索範囲を絞りながら探索を繰り返してください
# 一探索毎に探索範囲が半分になるので、データ個数がnの時の計算量がO(log2n)となります
# 探索対象の配列に探索する数値が存在しない場合は、-1 を出力してください
# 再帰を使用せず記述してください
