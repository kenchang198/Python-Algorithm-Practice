# time_complexity_visualizer.py

import matplotlib.pyplot as plt
import numpy as np

def plot_time_complexities(max_n=100):
    """
    異なる時間計算量の成長率をプロットする
    
    Parameters:
        max_n (int): プロットする最大のn値
    """
    n = np.arange(1, max_n + 1)
    
    # 各計算量の関数
    constant = np.ones_like(n)  # O(1)
    logarithmic = np.log2(n)    # O(log n)
    linear = n                  # O(n)
    linearithmic = n * np.log2(n)  # O(n log n)
    quadratic = n ** 2          # O(n²)
    cubic = n ** 3              # O(n³)
    exponential = 2 ** n        # O(2^n)
    
    # 指数関数の値が大きすぎるため、表示用にスケーリング
    exponential = exponential / (2 ** max_n) * quadratic[-1] * 1.5
    
    # プロットの設定
    plt.figure(figsize=(12, 8))
    plt.plot(n, constant, label='O(1) - 定数時間')
    plt.plot(n, logarithmic, label='O(log n) - 対数時間')
    plt.plot(n, linear, label='O(n) - 線形時間')
    plt.plot(n, linearithmic, label='O(n log n) - 線形対数時間')
    plt.plot(n, quadratic, label='O(n²) - 二次時間')
    plt.plot(n, cubic, label='O(n³) - 三次時間')
    plt.plot(n, exponential, label='O(2^n) - 指数時間 (スケーリング済み)')
    
    plt.xlabel('入力サイズ (n)')
    plt.ylabel('操作回数')
    plt.title('異なる時間計算量の成長率比較')
    plt.legend()
    plt.grid(True)
    
    # 保存
    plt.savefig('time_complexity_comparison.png')
    plt.close()
    
    print("グラフが 'time_complexity_comparison.png' として保存されました")

def plot_specific_comparison(max_n=100):
    """
    特定の計算量を比較するプロット（O(n) vs O(n²)）
    
    Parameters:
        max_n (int): プロットする最大のn値
    """
    n = np.arange(1, max_n + 1)
    
    # 計算量関数
    linear = n                  # O(n)
    quadratic = n ** 2          # O(n²)
    
    # プロットの設定
    plt.figure(figsize=(10, 6))
    plt.plot(n, linear, label='O(n) - 線形時間', linewidth=2)
    plt.plot(n, quadratic, label='O(n²) - 二次時間', linewidth=2)
    
    plt.xlabel('入力サイズ (n)')
    plt.ylabel('操作回数')
    plt.title('線形時間 vs 二次時間の比較')
    plt.legend()
    plt.grid(True)
    
    # 保存
    plt.savefig('linear_vs_quadratic.png')
    plt.close()
    
    print("グラフが 'linear_vs_quadratic.png' として保存されました")

if __name__ == "__main__":
    plot_time_complexities()
    plot_specific_comparison()
