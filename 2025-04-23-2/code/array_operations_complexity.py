# array_operations_complexity.py
# 様々な配列操作の計算量分析

import time
import sys

def measure_time(func, *args, **kwargs):
    """関数の実行時間を計測する"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

# ==== 配列の先頭に要素を挿入する操作（O(n)） ====
def insert_at_beginning(arr, element):
    """配列の先頭に要素を挿入する"""
    # Python のリストでは、insert メソッドを使用
    arr.insert(0, element)
    return arr

def test_insert_at_beginning():
    print("\n===== 配列の先頭に要素を挿入する操作 =====")
    print("理論的計算量: O(n)")
    print("理由: すべての既存要素をシフトする必要があるため")
    
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        # テスト用の配列を作成
        arr = list(range(size))
        
        # 実行時間の計測
        _, execution_time = measure_time(insert_at_beginning, arr.copy(), -1)
        
        print(f"配列サイズ {size}: {execution_time:.8f} 秒")

# ==== 配列の末尾に要素を追加する操作（O(1)償却） ====
def append_to_end(arr, element):
    """配列の末尾に要素を追加する"""
    # Python のリストでは、append メソッドを使用
    arr.append(element)
    return arr

def test_append_to_end():
    print("\n===== 配列の末尾に要素を追加する操作 =====")
    print("理論的計算量: O(1) [償却]")
    print("理由: 通常は定数時間だが、配列の再割り当てが必要な場合はO(n)になる")
    
    sizes = [1000, 10000, 100000, 1000000]
    
    for size in sizes:
        # テスト用の配列を作成
        arr = list(range(size))
        
        # 実行時間の計測
        _, execution_time = measure_time(append_to_end, arr.copy(), size)
        
        print(f"配列サイズ {size}: {execution_time:.8f} 秒")

# ==== 配列内のすべての要素を2倍にする操作（O(n)） ====
def double_all_elements(arr):
    """配列内のすべての要素を2倍にする"""
    for i in range(len(arr)):
        arr[i] = arr[i] * 2
    return arr

def test_double_all_elements():
    print("\n===== 配列内のすべての要素を2倍にする操作 =====")
    print("理論的計算量: O(n)")
    print("理由: 各要素を1回ずつ処理する必要があるため")
    
    sizes = [1000, 10000, 100000, 1000000]
    
    for size in sizes:
        # テスト用の配列を作成
        arr = list(range(size))
        
        # 実行時間の計測
        _, execution_time = measure_time(double_all_elements, arr.copy())
        
        print(f"配列サイズ {size}: {execution_time:.8f} 秒")

# ==== 2つの配列を結合する操作（O(n + m)） ====
def combine_arrays(arr1, arr2):
    """2つの配列を結合する"""
    # Python のリストでは、+ 演算子または extend メソッドを使用
    return arr1 + arr2

def test_combine_arrays():
    print("\n===== 2つの配列を結合する操作 =====")
    print("理論的計算量: O(n + m)")
    print("理由: nとmは各配列のサイズで、すべての要素をコピーする必要があるため")
    
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        # テスト用の配列を作成
        arr1 = list(range(size))
        arr2 = list(range(size, size * 2))
        
        # 実行時間の計測
        _, execution_time = measure_time(combine_arrays, arr1.copy(), arr2.copy())
        
        print(f"配列サイズ {size} + {size}: {execution_time:.8f} 秒")

# ==== 入れ子になった2つのfor文での処理（O(n²)） ====
def nested_loops_processing(arr):
    """入れ子になった2つのfor文での処理"""
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            # 単純な演算でカウント
            count += 1
    return count

def test_nested_loops_processing():
    print("\n===== 入れ子になった2つのfor文での処理 =====")
    print("理論的計算量: O(n²)")
    print("理由: 外側のループがn回、内側のループがそれぞれn回実行されるため")
    
    sizes = [100, 500, 1000, 2000]
    
    for size in sizes:
        # テスト用の配列を作成
        arr = list(range(size))
        
        # 実行時間の計測
        result, execution_time = measure_time(nested_loops_processing, arr.copy())
        
        print(f"配列サイズ {size} (処理回数 {result}): {execution_time:.8f} 秒")

# ==== 配列要素へのアクセス（O(1)） ====
def access_element(arr, index):
    """配列の特定のインデックスにアクセスする"""
    return arr[index]

def test_access_element():
    print("\n===== 配列要素へのアクセス =====")
    print("理論的計算量: O(1)")
    print("理由: インデックスが分かっていれば、サイズに関わらず直接アクセスできるため")
    
    sizes = [1000, 10000, 100000, 1000000, 10000000]
    
    for size in sizes:
        # テスト用の配列を作成
        arr = list(range(size))
        
        # 実行時間の計測
        _, execution_time = measure_time(access_element, arr, size // 2)
        
        print(f"配列サイズ {size}: {execution_time:.8f} 秒")

# ==== メモリ使用量の計測 ====
def measure_memory_usage(arr):
    """配列のメモリ使用量を計測する（バイト単位）"""
    return sys.getsizeof(arr)

def test_memory_usage():
    print("\n===== 配列のメモリ使用量 =====")
    
    sizes = [0, 10, 100, 1000, 10000, 100000, 1000000]
    
    for size in sizes:
        # テスト用の配列を作成
        arr = list(range(size))
        
        # メモリ使用量の計測
        memory_usage = measure_memory_usage(arr)
        
        print(f"配列サイズ {size}: {memory_usage} バイト")

# メイン実行部分
if __name__ == "__main__":
    print("様々な配列操作の計算量分析を開始します...")
    
    # 各操作のテスト
    test_insert_at_beginning()
    test_append_to_end()
    test_double_all_elements()
    test_combine_arrays()
    test_nested_loops_processing()
    test_access_element()
    test_memory_usage()
    
    print("\n分析が完了しました。")
