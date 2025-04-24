# mystery_function_analysis.py
# ミステリー関数の計算量分析

import time
import matplotlib.pyplot as plt

def measure_time(func, *args, **kwargs):
    """関数の実行時間を計測する"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

# ==== ミステリー関数1 ====
def mystery_function_1(n):
    """
    Mystery関数1の計算量分析
    - 外側のループは n 回実行
    - 内側のループは、iの値に応じて (n-i) 回実行
    - 合計の実行回数: n + (n-1) + (n-2) + ... + 1 = n(n+1)/2
    - 計算量: O(n²)
    """
    result = 0
    operations = 0
    
    for i in range(n):
        for j in range(i, n):
            # 実際の操作（ここでは単純な加算）
            result += i * j
            operations += 1
    
    return result, operations

def test_mystery_function_1():
    print("\n===== ミステリー関数1の計算量分析 =====")
    print("コード:")
    print("""
    def mystery_function_1(n):
        result = 0
        for i in range(n):
            for j in range(i, n):
                result += i * j
        return result
    """)
    print("理論的計算量: O(n²)")
    print("理由: 外側のループがn回、内側のループがiの値に依存して(n-i)回実行される")
    print("操作回数の総和: n(n+1)/2 ≈ O(n²)")
    
    sizes = [10, 100, 1000, 3000]
    times = []
    operations_counts = []
    theoretical_counts = []
    
    for size in sizes:
        # 実行時間と操作回数の計測
        result, execution_time = measure_time(mystery_function_1, size)
        _, operations = result
        
        # 理論的な操作回数（n(n+1)/2）
        theoretical_count = size * (size + 1) // 2
        
        times.append(execution_time)
        operations_counts.append(operations)
        theoretical_counts.append(theoretical_count)
        
        print(f"サイズ {size}:")
        print(f"  操作回数: {operations}")
        print(f"  理論値: {theoretical_count}")
        print(f"  実行時間: {execution_time:.8f} 秒")

# ==== ミステリー関数2 ====
def mystery_function_2(arr):
    """
    Mystery関数2の計算量分析
    - 外側のループは n 回実行
    - 内側のループは条件が満たされた場合のみ n 回実行
    - 最悪の場合（すべての要素が偶数）: O(n²)
    - 平均的な場合（約半数の要素が偶数）: O(n²/2) ≈ O(n²)
    - 最良の場合（すべての要素が奇数）: O(n)
    """
    result = 0
    operations = 0
    
    for i in range(len(arr)):
        operations += 1  # 比較操作
        if arr[i] % 2 == 0:  # 偶数の場合
            for j in range(len(arr)):
                # 実際の操作
                result += arr[i] * arr[j]
                operations += 1
    
    return result, operations

def test_mystery_function_2():
    print("\n===== ミステリー関数2の計算量分析 =====")
    print("コード:")
    print("""
    def mystery_function_2(arr):
        result = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:  # 偶数の場合
                for j in range(len(arr)):
                    result += arr[i] * arr[j]
        return result
    """)
    print("理論的計算量:")
    print("- 最悪の場合（すべての要素が偶数）: O(n²)")
    print("- 平均的な場合（約半数の要素が偶数）: O(n²/2) ≈ O(n²)")
    print("- 最良の場合（すべての要素が奇数）: O(n)")
    
    size = 1000
    
    # 最良のケース: すべて奇数
    all_odd = [i * 2 + 1 for i in range(size)]
    result_best, time_best = measure_time(mystery_function_2, all_odd)
    _, operations_best = result_best
    
    # 平均的なケース: 半分が偶数
    half_even = [i for i in range(size)]
    result_avg, time_avg = measure_time(mystery_function_2, half_even)
    _, operations_avg = result_avg
    
    # 最悪のケース: すべて偶数
    all_even = [i * 2 for i in range(size)]
    result_worst, time_worst = measure_time(mystery_function_2, all_even)
    _, operations_worst = result_worst
    
    print(f"配列サイズ: {size}")
    print(f"最良のケース (すべて奇数):")
    print(f"  操作回数: {operations_best}")
    print(f"  実行時間: {time_best:.8f} 秒")
    print(f"平均的なケース (半分が偶数):")
    print(f"  操作回数: {operations_avg}")
    print(f"  実行時間: {time_avg:.8f} 秒")
    print(f"最悪のケース (すべて偶数):")
    print(f"  操作回数: {operations_worst}")
    print(f"  実行時間: {time_worst:.8f} 秒")

# ==== ミステリー関数3（ソート済み行列の探索） ====
def search_sorted_matrix(matrix, target):
    """
    ソート済み行列での探索
    - 行は左から右へ増加
    - 列は上から下へ増加
    - 右上から開始して、左下へ進む
    - 計算量: O(n + m)、nは行数、mは列数
    """
    operations = 0
    
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    row, col = 0, cols - 1
    while row < rows and col >= 0:
        operations += 1  # 比較操作
        
        if matrix[row][col] == target:
            return True, operations
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
            
    return False, operations

def create_sorted_matrix(n):
    """ソート済み行列を作成（各行が左から右へ、各列が上から下へ増加）"""
    matrix = []
    for i in range(n):
        row = [i * n + j + 1 for j in range(n)]
        matrix.append(row)
    return matrix

def test_search_sorted_matrix():
    print("\n===== ソート済み行列の探索 =====")
    print("コード:")
    print("""
    def search_sorted_matrix(matrix, target):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
    """)
    print("理論的計算量: O(n + m)、nは行数、mは列数")
    print("理由: 各ステップで行または列の位置が1つ減少し、最大でも行数+列数回の操作で終了")
    
    # 様々なサイズでテスト
    sizes = [10, 50, 100, 500]
    
    for size in sizes:
        # ソート済み行列を作成
        matrix = create_sorted_matrix(size)
        
        # 存在する値（行列の中央付近）
        target_exists = size * size // 2
        
        # 存在しない値（行列の最大値より大きい）
        target_not_exists = size * size + 100
        
        # 存在する値の探索
        result_exists, time_exists = measure_time(search_sorted_matrix, matrix, target_exists)
        found_exists, operations_exists = result_exists
        
        # 存在しない値の探索
        result_not_exists, time_not_exists = measure_time(search_sorted_matrix, matrix, target_not_exists)
        found_not_exists, operations_not_exists = result_not_exists
        
        print(f"行列サイズ: {size}x{size}")
        print(f"存在する値の探索 ({target_exists}):")
        print(f"  結果: {'見つかりました' if found_exists else '見つかりませんでした'}")
        print(f"  操作回数: {operations_exists}")
        print(f"  実行時間: {time_exists:.8f} 秒")
        print(f"存在しない値の探索 ({target_not_exists}):")
        print(f"  結果: {'見つかりました' if found_not_exists else '見つかりませんでした'}")
        print(f"  操作回数: {operations_not_exists}")
        print(f"  実行時間: {time_not_exists:.8f} 秒")

# メイン実行部分
if __name__ == "__main__":
    print("ミステリー関数の計算量分析を開始します...")
    
    # 各関数のテスト
    test_mystery_function_1()
    test_mystery_function_2()
    test_search_sorted_matrix()
    
    print("\n分析が完了しました。")
