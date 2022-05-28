def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]


def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    left = []
    right = []
    pivot_count = 0

    for element in array:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            pivot_count += 1
    left = sort(left)
    right = sort(right)

    return left + [pivot] * pivot_count + right
    # ここまで記述


if __name__ == '__main__':
    main()

# 整数の配列を昇順にソートするアルゴリズムを実装してください
# ソート対象の配列は「1つ以上の要素を持つ、ランダムに並べられた重複のない整数の配列」です
# ただし、以下の条件を満たすアルゴリズムを用いて実装してください

# 配列の先頭を基準値とします
# 先頭から末端に向かって、基準値以上の値の探索、逆方向から基準値の値未満の探索をし、見つかったらそれらの値同士を交換します
# 先頭からの探索と、末端からの探索がぶつかった時点で探索を終了し、データを二つ（基準値以上のグループ、基準値未満のグループ）に分けます
# 分けられたそれぞれのグループで、同様の処理を再帰的に繰り返し、交換する部分がなくなるまで処理を続けます
# ※　先述の通り、問題３に関しては採点基準の1 ~ 4のルールを満たしていなくても
# 　　部分点が獲得できるので是非チャレンジしてみてください。
