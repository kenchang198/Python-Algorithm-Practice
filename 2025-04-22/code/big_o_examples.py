# big_o_examples.py

import time
import matplotlib.pyplot as plt
import numpy as np

def constant_time_example(arr):
    """O(1) - 定数時間の例"""
    return arr[0] if arr else None

def linear_time_example(arr):
    """O(n) - 線形時間の例"""
    total = 0
    for item in arr:
        total += item
    return total

def quadratic_time_example(arr):
    """O(n²) - 二次時間の例"""
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append(arr[i] * arr[j])
    return result

def logarithmic_time_example(arr, target):
    """O(log n) - 対数時間の例（二分探索）"""
    # ソート済みの配列を前提とする
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def measure_execution_time(func, *args, **kwargs):
    """関数の実行時間を測定する"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return (end_time - start_time), result

def demonstrate_time_complexity():
    """時間計算量のデモンストレーション"""
    sizes = [100, 1000, 10000, 100000]
    constant_times = []
    linear_times = []
    quadratic_times = []
    
    for size in sizes:
        arr = list(range(size))
        
        # O(1) の測定
        time_taken, _ = measure_execution_time(constant_time_example, arr)
        constant_times.append(time_taken)
        print(f"O(1) - サイズ {size}: {time_taken:.6f} 秒")
        
        # O(n) の測定
        time_taken, _ = measure_execution_time(linear_time_example, arr)
        linear_times.append(time_taken)
        print(f"O(n) - サイズ {size}: {time_taken:.6f} 秒")
        
        # O(n²) の測定 - 大きなサイズは飛ばす
        if size <= 10000:
            time_taken, _ = measure_execution_time(quadratic_time_example, arr[:100])
            quadratic_times.append(time_taken)
            print(f"O(n²) - サイズ 100: {time_taken:.6f} 秒")
        else:
            quadratic_times.append(None)
    
    return sizes, constant_times, linear_times, quadratic_times

if __name__ == "__main__":
    demonstrate_time_complexity()
