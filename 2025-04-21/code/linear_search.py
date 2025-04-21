# linear_search.py

def linear_search(arr, target):
    """
    線形探索アルゴリズム
    
    Parameters:
        arr (list): 探索対象の配列
        target: 探索する値
    
    Returns:
        int: 見つかった場合はそのインデックス、見つからなかった場合は-1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # 見つかった場合、インデックスを返す
    
    return -1  # 見つからなかった場合、-1を返す

def linear_search_all(arr, target):
    """
    線形探索アルゴリズム（すべての一致を検出）
    
    Parameters:
        arr (list): 探索対象の配列
        target: 探索する値
    
    Returns:
        list: 見つかった場合はそのインデックスのリスト、見つからなかった場合は空リスト
    """
    found_indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            found_indices.append(i)
    
    return found_indices

def linear_search_demo():
    # テスト用のデータセット
    numbers = [10, 25, 3, 14, 42, 19, 7, 36]
    
    # 配列内の値を探す
    target = 14
    result = linear_search(numbers, target)
    
    if result != -1:
        print(f"値 {target} はインデックス {result} で見つかりました。")
    else:
        print(f"値 {target} は配列内に存在しません。")
    
    # 配列内に存在しない値を探す
    target = 100
    result = linear_search(numbers, target)
    
    if result != -1:
        print(f"値 {target} はインデックス {result} で見つかりました。")
    else:
        print(f"値 {target} は配列内に存在しません。")
    
    # linear_search_all のデモ
    print("\n--- linear_search_all のデモ ---")
    # 重複した要素を含むリスト
    numbers_with_duplicates = [5, 10, 15, 20, 10, 25, 30, 10]
    
    # 値10のすべての出現位置を検索
    target = 10
    all_results = linear_search_all(numbers_with_duplicates, target)
    
    if all_results:
        print(f"値 {target} は以下のインデックスで見つかりました: {all_results}")
    else:
        print(f"値 {target} は配列内に存在しません。")
    
    # 存在しない値を検索
    target = 100
    all_results = linear_search_all(numbers_with_duplicates, target)
    
    if all_results:
        print(f"値 {target} は以下のインデックスで見つかりました: {all_results}")
    else:
        print(f"値 {target} は配列内に存在しません。")

if __name__ == "__main__":
    linear_search_demo()
