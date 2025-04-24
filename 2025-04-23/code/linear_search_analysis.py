# linear_search_analysis.py
# 線形探索アルゴリズムの計算量分析（シンプル版）

import time
import random

# 線形探索の基本実装
def linear_search(arr, target):
    """
    線形探索アルゴリズム
    
    Parameters:
        arr (list): 探索対象の配列
        target: 探索する値
    
    Returns:
        int: 見つかった場合はそのインデックス、見つからなかった場合は-1
        int: 比較回数
    """
    # 比較回数を数えるカウンター
    comparisons = 0
    
    # 配列の先頭から順に探索
    for i in range(len(arr)):
        # 比較回数をカウントアップ
        comparisons += 1
        
        # 現在の要素が探索対象と一致するか確認
        if arr[i] == target:
            # 一致したら、インデックスと比較回数を返す
            return i, comparisons
    
    # 見つからなかった場合、-1と比較回数を返す
    return -1, comparisons

# ========== 最良のケース（先頭の要素を探す）のテスト ==========
def test_best_case():
    print("\n===== 最良のケース（先頭の要素を探す）のテスト =====")
    
    # テスト用の配列を作成
    arr = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"配列: {arr}")
    
    # 最良のケース: 配列の先頭の要素を探す
    target = arr[0]  # 0
    print(f"探索値: {target} (先頭の要素)")
    
    # 探索実行（時間計測付き）
    start_time = time.time()
    index, comparisons = linear_search(arr, target)
    end_time = time.time()
    
    # 実行時間の計算
    execution_time = end_time - start_time
    
    # 結果の表示
    print(f"結果: インデックス {index} で見つかりました")
    print(f"比較回数: {comparisons} 回")
    print(f"実行時間: {execution_time:.8f} 秒")
    print(f"理論的計算量: O(1) (最良のケース)")

# ========== 平均的なケース（ランダムな位置の要素を探す）のテスト ==========
def test_average_case():
    print("\n===== 平均的なケース（ランダムな位置の要素を探す）のテスト =====")
    
    # テスト用の配列を作成
    arr = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"配列: {arr}")
    
    # 平均的なケース: 配列のランダムな位置の要素を探す
    random_index = random.randint(1, len(arr) - 2)  # 先頭と末尾を避けてランダムに選択
    target = arr[random_index]
    print(f"探索値: {target} (インデックス {random_index} の要素)")
    
    # 探索実行（時間計測付き）
    start_time = time.time()
    index, comparisons = linear_search(arr, target)
    end_time = time.time()
    
    # 実行時間の計算
    execution_time = end_time - start_time
    
    # 結果の表示
    print(f"結果: インデックス {index} で見つかりました")
    print(f"比較回数: {comparisons} 回")
    print(f"実行時間: {execution_time:.8f} 秒")
    print(f"理論的計算量: O(n/2) ≈ O(n) (平均的なケース)")

# ========== 最悪のケース（末尾の要素を探す）のテスト ==========
def test_worst_case():
    print("\n===== 最悪のケース（末尾の要素を探す）のテスト =====")
    
    # テスト用の配列を作成
    arr = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"配列: {arr}")
    
    # 最悪のケース: 配列の末尾の要素を探す
    target = arr[-1]  # 9
    print(f"探索値: {target} (末尾の要素)")
    
    # 探索実行（時間計測付き）
    start_time = time.time()
    index, comparisons = linear_search(arr, target)
    end_time = time.time()
    
    # 実行時間の計算
    execution_time = end_time - start_time
    
    # 結果の表示
    print(f"結果: インデックス {index} で見つかりました")
    print(f"比較回数: {comparisons} 回")
    print(f"実行時間: {execution_time:.8f} 秒")
    print(f"理論的計算量: O(n) (最悪のケース)")

# ========== 要素が存在しない場合のテスト ==========
def test_not_found_case():
    print("\n===== 要素が存在しない場合のテスト =====")
    
    # テスト用の配列を作成
    arr = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"配列: {arr}")
    
    # 存在しない要素: 配列の最大値よりも大きい値
    target = len(arr) + 5  # 15 (配列内に存在しない)
    print(f"探索値: {target} (配列内に存在しない)")
    
    # 探索実行（時間計測付き）
    start_time = time.time()
    index, comparisons = linear_search(arr, target)
    end_time = time.time()
    
    # 実行時間の計算
    execution_time = end_time - start_time
    
    # 結果の表示
    print(f"結果: インデックス {index} (見つからなかった)")
    print(f"比較回数: {comparisons} 回")
    print(f"実行時間: {execution_time:.8f} 秒")
    print(f"理論的計算量: O(n) (最悪のケース)")

# ========== 配列サイズによる比較回数の変化 ==========
def test_size_impact():
    print("\n===== 配列サイズによる比較回数の変化 =====")
    
    # テストする配列サイズ
    sizes = [10, 100, 1000, 10000]
    
    # 各サイズでテスト
    for size in sizes:
        # テスト用の配列を作成
        arr = list(range(size))
        
        print(f"\n配列サイズ: {size}")
        
        # 最良のケース: 先頭の要素を探す
        best_target = arr[0]
        _, best_comparisons = linear_search(arr, best_target)
        print(f"  最良のケース（先頭）: {best_comparisons} 回の比較 (理論値: 1)")
        
        # 平均的なケース: 中間付近の要素を探す
        avg_target = arr[size // 2]
        _, avg_comparisons = linear_search(arr, avg_target)
        print(f"  平均的なケース（中間）: {avg_comparisons} 回の比較 (理論値: {size/2})")
        
        # 最悪のケース: 末尾の要素を探す
        worst_target = arr[-1]
        _, worst_comparisons = linear_search(arr, worst_target)
        print(f"  最悪のケース（末尾）: {worst_comparisons} 回の比較 (理論値: {size})")
        
        # 存在しない要素を探す
        not_found_target = size + 5
        _, not_found_comparisons = linear_search(arr, not_found_target)
        print(f"  存在しない要素: {not_found_comparisons} 回の比較 (理論値: {size})")

# ========== 理論との比較分析 ==========
def theory_analysis():
    print("\n===== 線形探索の計算量分析 =====")
    print("線形探索アルゴリズムの計算量は以下のように特徴づけられます：")
    print()
    print("1. 最良のケース (Best Case):")
    print("   - 目的の要素が配列の先頭にある場合")
    print("   - 比較回数: 1回")
    print("   - 計算量: O(1)")
    print()
    print("2. 平均的なケース (Average Case):")
    print("   - 目的の要素が配列内のランダムな位置にある場合")
    print("   - 平均比較回数: n/2回")
    print("   - 計算量: O(n/2) ≈ O(n)")
    print()
    print("3. 最悪のケース (Worst Case):")
    print("   - 目的の要素が配列の末尾にある場合")
    print("   - 比較回数: n回")
    print("   - 計算量: O(n)")
    print()
    print("4. 要素が存在しない場合:")
    print("   - 最悪のケースと同様に、すべての要素を調べる必要がある")
    print("   - 比較回数: n回")
    print("   - 計算量: O(n)")
    print()
    print("5. 空間計算量 (Space Complexity):")
    print("   - 追加のメモリ使用がほとんどない")
    print("   - 計算量: O(1)")
    print()
    print("線形探索は実装が非常に単純なアルゴリズムですが、")
    print("大きなデータセットでは効率が悪くなる可能性があります。")
    print("ソート済みの配列では、二分探索のようなより効率的なアルゴリズムを使うことができます。")

# メイン実行部分
if __name__ == "__main__":
    print("線形探索アルゴリズムの計算量分析を開始します...")
    
    # 各ケースのテスト
    test_best_case()
    test_average_case()
    test_worst_case()
    test_not_found_case()
    
    # 配列サイズによる影響のテスト
    test_size_impact()
    
    # 理論分析
    theory_analysis()
    
    print("\n分析が完了しました。")
