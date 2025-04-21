# extended_search.py

def search_multiple_values(arr, targets):
    """
    複数の値（リスト）を受け取り、それぞれが元のリスト内に存在するかどうかを調べる関数
    
    Parameters:
        arr (list): 探索対象の配列
        targets (list): 探索する値のリスト
    
    Returns:
        dict: キーが探索値、値が存在するかどうかのブール値の辞書
    """
    result = {}
    for target in targets:
        result[target] = target in arr
    
    return result

def find_max_value(arr):
    """
    リスト内の最大値を線形探索で見つける関数
    
    Parameters:
        arr (list): 探索対象の配列
    
    Returns:
        tuple: (最大値, そのインデックス)、配列が空の場合は (None, -1)
    """
    if not arr:
        return (None, -1)
    
    max_value = arr[0]
    max_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
    
    return (max_value, max_index)

def extended_search_demo():
    # テスト用のデータセット
    numbers = [10, 25, 3, 14, 42, 19, 7, 36]
    
    print("元のリスト:", numbers)
    
    # 複数の値の検索
    targets = [14, 50, 42, 100]
    results = search_multiple_values(numbers, targets)
    
    print("\n--- 複数の値の検索結果 ---")
    for target, exists in results.items():
        status = "存在します" if exists else "存在しません"
        print(f"値 {target} はリスト内に {status}")
    
    # 最大値の検索
    max_value, max_index = find_max_value(numbers)
    
    print("\n--- 最大値の検索結果 ---")
    print(f"最大値: {max_value}")
    print(f"インデックス: {max_index}")
    
    # 空のリストでのテスト
    empty_list = []
    max_value, max_index = find_max_value(empty_list)
    
    print("\n--- 空のリストでの検索結果 ---")
    if max_value is None:
        print("空のリストには最大値が存在しません")
    else:
        print(f"最大値: {max_value}")
        print(f"インデックス: {max_index}")

if __name__ == "__main__":
    extended_search_demo()
