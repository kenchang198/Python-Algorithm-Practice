# linear_search_analysis.py
import time
import matplotlib.pyplot as plt
import numpy as np
import random

def linear_search(arr, target):
    """
    線形探索アルゴリズム
    
    Parameters:
        arr (list): 探索対象の配列
        target: 探索する値
    
    Returns:
        int: 見つかった場合はそのインデックス、見つからなかった場合は-1
    """
    comparisons = 0  # 比較回数をカウント
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons  # インデックスと比較回数を返す
    
    return -1, comparisons  # 見つからなかった場合と比較回数を返す

def measure_time(func, *args, **kwargs):
    """関数の実行時間を計測"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

def simulate_cases(size):
    """最良、平均、最悪のケースをシミュレーション"""
    arr = list(range(size))
    
    # 最良のケース: 最初の要素を探す
    best_case_target = arr[0]
    best_case_result, best_case_time = measure_time(linear_search, arr, best_case_target)
    best_case_index, best_case_comparisons = best_case_result
    
    # 平均的なケース: ランダムな位置の要素を探す
    random_index = random.randint(0, size - 1)
    average_case_target = arr[random_index]
    average_case_result, average_case_time = measure_time(linear_search, arr, average_case_target)
    average_case_index, average_case_comparisons = average_case_result
    
    # 最悪のケース: 最後の要素を探す
    worst_case_target = arr[-1]
    worst_case_result, worst_case_time = measure_time(linear_search, arr, worst_case_target)
    worst_case_index, worst_case_comparisons = worst_case_result
    
    # 存在しない要素を探す場合（これも最悪のケース）
    not_found_target = size + 1
    not_found_result, not_found_time = measure_time(linear_search, arr, not_found_target)
    not_found_index, not_found_comparisons = not_found_result
    
    return {
        "size": size,
        "best_case": {
            "index": best_case_index,
            "comparisons": best_case_comparisons,
            "time": best_case_time
        },
        "average_case": {
            "index": average_case_index,
            "comparisons": average_case_comparisons,
            "time": average_case_time
        },
        "worst_case": {
            "index": worst_case_index,
            "comparisons": worst_case_comparisons,
            "time": worst_case_time
        },
        "not_found": {
            "index": not_found_index,
            "comparisons": not_found_comparisons,
            "time": not_found_time
        }
    }

def analyze_linear_search_with_real_data():
    """様々なサイズで線形探索を分析"""
    sizes = [100, 1000, 10000, 100000]
    results = []
    
    for size in sizes:
        print(f"サイズ {size} での分析...")
        result = simulate_cases(size)
        results.append(result)
        
        print(f"  最良のケース: {result['best_case']['comparisons']} 回の比較, {result['best_case']['time']:.8f} 秒")
        print(f"  平均的なケース: {result['average_case']['comparisons']} 回の比較, {result['average_case']['time']:.8f} 秒")
        print(f"  最悪のケース: {result['worst_case']['comparisons']} 回の比較, {result['worst_case']['time']:.8f} 秒")
        print(f"  要素が存在しない場合: {result['not_found']['comparisons']} 回の比較, {result['not_found']['time']:.8f} 秒")
        print()
    
    return results

def plot_comparisons(results):
    """比較回数のグラフを作成"""
    sizes = [result["size"] for result in results]
    best_comparisons = [result["best_case"]["comparisons"] for result in results]
    average_comparisons = [result["average_case"]["comparisons"] for result in results]
    worst_comparisons = [result["worst_case"]["comparisons"] for result in results]
    not_found_comparisons = [result["not_found"]["comparisons"] for result in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, best_comparisons, 'o-', label='最良のケース (O(1))')
    plt.plot(sizes, average_comparisons, 's-', label='平均的なケース (O(n/2))')
    plt.plot(sizes, worst_comparisons, '^-', label='最悪のケース (O(n))')
    plt.plot(sizes, not_found_comparisons, 'D-', label='要素が存在しない場合 (O(n))')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('配列サイズ (n)')
    plt.ylabel('比較回数')
    plt.title('線形探索の計算量分析 - 比較回数')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('linear_search_comparisons.png')
    print("比較回数のグラフを 'linear_search_comparisons.png' として保存しました")

def plot_execution_times(results):
    """実行時間のグラフを作成"""
    sizes = [result["size"] for result in results]
    best_times = [result["best_case"]["time"] for result in results]
    average_times = [result["average_case"]["time"] for result in results]
    worst_times = [result["worst_case"]["time"] for result in results]
    not_found_times = [result["not_found"]["time"] for result in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, best_times, 'o-', label='最良のケース (O(1))')
    plt.plot(sizes, average_times, 's-', label='平均的なケース (O(n/2))')
    plt.plot(sizes, worst_times, '^-', label='最悪のケース (O(n))')
    plt.plot(sizes, not_found_times, 'D-', label='要素が存在しない場合 (O(n))')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('配列サイズ (n)')
    plt.ylabel('実行時間 (秒)')
    plt.title('線形探索の計算量分析 - 実行時間')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('linear_search_execution_times.png')
    print("実行時間のグラフを 'linear_search_execution_times.png' として保存しました")

def compare_theory_with_practice(results):
    """理論値と実測値の比較"""
    sizes = [result["size"] for result in results]
    best_comparisons = [result["best_case"]["comparisons"] for result in results]
    average_comparisons = [result["average_case"]["comparisons"] for result in results]
    worst_comparisons = [result["worst_case"]["comparisons"] for result in results]
    
    # 理論値の計算
    theoretical_best = [1 for _ in sizes]  # O(1) - 常に1回の比較
    theoretical_average = [size / 2 for size in sizes]  # O(n/2) - 平均的に半分の要素を比較
    theoretical_worst = [size for size in sizes]  # O(n) - すべての要素を比較
    
    plt.figure(figsize=(12, 8))
    
    # 実測値のプロット
    plt.plot(sizes, best_comparisons, 'o-', label='実測: 最良のケース')
    plt.plot(sizes, average_comparisons, 's-', label='実測: 平均的なケース')
    plt.plot(sizes, worst_comparisons, '^-', label='実測: 最悪のケース')
    
    # 理論値のプロット
    plt.plot(sizes, theoretical_best, 'o--', alpha=0.5, label='理論: 最良のケース (O(1))')
    plt.plot(sizes, theoretical_average, 's--', alpha=0.5, label='理論: 平均的なケース (O(n/2))')
    plt.plot(sizes, theoretical_worst, '^--', alpha=0.5, label='理論: 最悪のケース (O(n))')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('配列サイズ (n)')
    plt.ylabel('比較回数')
    plt.title('線形探索 - 理論値と実測値の比較')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('linear_search_theory_vs_practice.png')
    print("理論値と実測値の比較グラフを 'linear_search_theory_vs_practice.png' として保存しました")

if __name__ == "__main__":
    print("線形探索アルゴリズムの計算量分析を開始します...")
    
    # 様々なサイズでの分析
    results = analyze_linear_search_with_real_data()
    
    # 結果のグラフ化
    plot_comparisons(results)
    plot_execution_times(results)
    compare_theory_with_practice(results)
    
    print("\n分析が完了しました。")
