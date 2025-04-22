# logarithmic_time_demo.py
# 二分探索（対数時間 O(log n)）のロジックを理解するためのデモ

def logarithmic_time_example_with_debug(arr, target):
    """
    二分探索アルゴリズム（デバッグプリント付き）
    元のlogarithmic_time_exampleと同じロジックに
    デバッグ情報を追加しています。
    
    Parameters:
        arr (list): ソート済みの探索対象配列
        target: 探索する値
    
    Returns:
        int: 見つかった場合はそのインデックス、見つからなかった場合は-1
    """
    # 探索の開始インデックスと終了インデックス
    left, right = 0, len(arr) - 1
    
    # 探索対象の配列とターゲット値を表示
    print(f"\n探索対象配列: {arr}")
    print(f"探索値: {target}")
    print("\n各ステップの探索範囲:")
    print("-" * 50)
    
    step = 1
    
    # left <= right の間、探索を続ける
    while left <= right:
        # 中央のインデックスを計算
        mid = (left + right) // 2
        
        # 現在の探索範囲とmidの位置を表示
        print(f"ステップ {step}:")
        
        # 配列の表示
        array_viz = []
        for i in range(len(arr)):
            if i < left or i > right:
                # 探索範囲外
                array_viz.append(f" {arr[i]} ")
            elif i == mid:
                # 中央値（現在チェック中）
                array_viz.append(f"[{arr[i]}]")
            else:
                # 探索範囲内
                array_viz.append(f"<{arr[i]}>")
        
        print("配列: " + " ".join(array_viz))
        print(f"探索範囲: left={left} (値={arr[left] if left < len(arr) else 'なし'}), "
              f"right={right} (値={arr[right] if right < len(arr) else 'なし'})")
        print(f"中央: mid={mid} (値={arr[mid]})")
        
        # ターゲットが見つかった場合
        if arr[mid] == target:
            print(f"一致! arr[{mid}] == {target}")
            return mid
        
        # ターゲットが中央値より小さい場合、右側を捨てる
        elif arr[mid] > target:
            print(f"arr[{mid}] > {target} なので、右側を捨てて左側を探索")
            right = mid - 1
        
        # ターゲットが中央値より大きい場合、左側を捨てる
        else:
            print(f"arr[{mid}] < {target} なので、左側を捨てて右側を探索")
            left = mid + 1
        
        step += 1
        print("-" * 50)
    
    # ターゲットが見つからなかった場合
    print("要素が見つからないため探索終了")
    return -1

def demonstrate_binary_search():
    """二分探索のデモンストレーション"""
    
    # 小さな配列での二分探索
    small_array = [1, 3, 5, 7, 9, 11, 13, 15]
    
    print("=== 小さな配列での二分探索 ===")
    
    # 配列内に存在する値を探す
    print("\n例1: 配列内に存在する値を探す")
    target = 7
    result = logarithmic_time_example_with_debug(small_array, target)
    print(f"結果: 値 {target} はインデックス {result} で見つかりました。")
    
    # 配列内に存在しない値を探す
    print("\n例2: 配列内に存在しない値を探す")
    target = 8
    result = logarithmic_time_example_with_debug(small_array, target)
    print(f"結果: 値 {target} は配列内に存在しません（戻り値: {result}）。")
    
    # 配列の先頭にある値を探す
    print("\n例3: 配列の先頭にある値を探す")
    target = 1
    result = logarithmic_time_example_with_debug(small_array, target)
    print(f"結果: 値 {target} はインデックス {result} で見つかりました。")
    
    # 配列の末尾にある値を探す
    print("\n例4: 配列の末尾にある値を探す")
    target = 15
    result = logarithmic_time_example_with_debug(small_array, target)
    print(f"結果: 値 {target} はインデックス {result} で見つかりました。")
    
    # 少し大きな配列での二分探索
    print("\n=== より大きな配列での二分探索 ===")
    medium_array = list(range(0, 32, 2))  # 0, 2, 4, ..., 30
    
    print("\n例5: より大きな配列での探索")
    target = 20
    result = logarithmic_time_example_with_debug(medium_array, target)
    print(f"結果: 値 {target} はインデックス {result} で見つかりました。")
    
    # 計算量の説明
    print("\n=== 二分探索の計算量 O(log n) の説明 ===")
    print("二分探索では各ステップで探索範囲が半分になります。")
    print("したがって、n個の要素を持つ配列では最大log₂(n)ステップで探索が完了します。")
    
    # サイズごとの最大ステップ数を表示
    sizes = [8, 16, 32, 64, 128, 256, 1024, 1048576]  # 2^3, 2^4, 2^5, 2^6, 2^7, 2^8, 2^10, 2^20
    
    print("\nサイズごとの最大ステップ数:")
    print("サイズ | 最大ステップ数")
    print("-" * 25)
    
    import math
    for size in sizes:
        max_steps = math.ceil(math.log2(size))
        print(f"{size:7d} | {max_steps}")
    
    print("\n例えば、1,048,576 (2^20) 個の要素がある配列でも、")
    print("最大で20ステップしか必要ありません。これが対数時間 O(log n) の特徴です。")

if __name__ == "__main__":
    demonstrate_binary_search()
