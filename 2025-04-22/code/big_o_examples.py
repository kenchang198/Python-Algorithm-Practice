# big_o_examples.py (修正版)

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
    """時間計算量のデモンストレーション - 修正版"""
    # すべての計算量タイプで使用できる適切なサイズ
    sizes = [10, 100, 1000, 5000]
    
    constant_times = []
    linear_times = []
    quadratic_times = []
    logarithmic_times = []
    
    print("各計算量タイプの実行時間比較\n")
    print("サイズ | O(1) 定数時間 | O(n) 線形時間 | O(n²) 二次時間 | O(log n) 対数時間")
    print("-" * 75)
    
    for size in sizes:
        arr = list(range(size))
        sorted_arr = arr.copy()  # 二分探索用のソート済み配列
        
        # O(1) の測定
        time_taken, _ = measure_execution_time(constant_time_example, arr)
        constant_times.append(time_taken)
        
        # O(n) の測定
        time_taken, _ = measure_execution_time(linear_time_example, arr)
        linear_times.append(time_taken)
        
        # O(n²) の測定 - 同じサイズで測定
        time_taken, _ = measure_execution_time(quadratic_time_example, arr)
        quadratic_times.append(time_taken)
        
        # O(log n) の測定
        target = size // 2  # 配列の中央付近の値を探索
        time_taken, _ = measure_execution_time(logarithmic_time_example, sorted_arr, target)
        logarithmic_times.append(time_taken)
        
        # 結果の表示
        print(f"{size:5d} | {constant_times[-1]:.8f}秒 | {linear_times[-1]:.8f}秒 | {quadratic_times[-1]:.8f}秒 | {logarithmic_times[-1]:.8f}秒")
    
    # 相対的な増加率の分析
    print("\n入力サイズの増加に伴う実行時間の増加率")
    print("-" * 50)
    
    for i in range(1, len(sizes)):
        size_ratio = sizes[i] / sizes[i-1]
        
        # 各計算量タイプの増加率を計算（0で割ることを防ぐため小さな値を加える）
        constant_ratio = constant_times[i] / (constant_times[i-1] + 1e-10)
        linear_ratio = linear_times[i] / (linear_times[i-1] + 1e-10)
        quadratic_ratio = quadratic_times[i] / (quadratic_times[i-1] + 1e-10)
        logarithmic_ratio = logarithmic_times[i] / (logarithmic_times[i-1] + 1e-10)
        
        print(f"サイズ {sizes[i-1]} → {sizes[i]} (サイズ比: {size_ratio:.1f}倍)")
        print(f"  O(1): {constant_ratio:.2f}倍 (理論値: 1倍)")
        print(f"  O(n): {linear_ratio:.2f}倍 (理論値: {size_ratio:.1f}倍)")
        print(f"  O(n²): {quadratic_ratio:.2f}倍 (理論値: {size_ratio**2:.1f}倍)")
        print(f"  O(log n): {logarithmic_ratio:.2f}倍")
    
    return sizes, constant_times, linear_times, quadratic_times, logarithmic_times

if __name__ == "__main__":
    sizes, constant_times, linear_times, quadratic_times, logarithmic_times = demonstrate_time_complexity()
    
    # オプション: 結果をグラフで表示
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, constant_times, 'o-', label='O(1) - 定数時間')
    plt.plot(sizes, linear_times, 's-', label='O(n) - 線形時間')
    plt.plot(sizes, logarithmic_times, '^-', label='O(log n) - 対数時間')
    
    # O(n²)はスケールが異なるため別軸で表示
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax2.plot(sizes, quadratic_times, 'D-', color='red', label='O(n²) - 二次時間 (右軸)')
    
    ax1.set_xlabel('入力サイズ (n)')
    ax1.set_ylabel('実行時間 (秒) - O(1), O(n), O(log n)')
    ax2.set_ylabel('実行時間 (秒) - O(n²)', color='red')
    
    # 凡例を追加
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    plt.title('異なる計算量の実行時間比較')
    plt.grid(True)
    plt.tight_layout()
    
    # グラフを保存
    plt.savefig('time_complexity_comparison_actual.png')
    print("\nグラフを'time_complexity_comparison_actual.png'として保存しました")
    
    # オプション: グラフを表示（Jupyter環境でのみ動作）
    # plt.show()
