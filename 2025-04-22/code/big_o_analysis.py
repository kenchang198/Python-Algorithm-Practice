# big_o_analysis.py

def analyze_linear_search():
    """線形探索アルゴリズムの計算量分析"""
    print("線形探索アルゴリズムの計算量分析:")
    print("----------------------------------")
    print("最良の場合 (Best Case):")
    print("  目的の要素が配列の先頭にある場合")
    print("  計算量: O(1)")
    print()
    print("平均的な場合 (Average Case):")
    print("  目的の要素が配列内のランダムな位置にある場合")
    print("  計算量: O(n/2) ≈ O(n)")
    print()
    print("最悪の場合 (Worst Case):")
    print("  目的の要素が配列の末尾にある場合、または配列内に存在しない場合")
    print("  計算量: O(n)")
    print()
    print("空間計算量 (Space Complexity):")
    print("  追加のメモリ使用がほとんどない")
    print("  計算量: O(1)")

def analyze_operations():
    """様々な操作の計算量分析"""
    print("\n様々な操作の計算量分析:")
    print("----------------------------------")
    
    print("1. 配列の先頭に要素を挿入する操作:")
    print("   計算量: O(n)")
    print("   理由: すべての既存要素をシフトする必要があるため")
    print()
    
    print("2. 配列の末尾に要素を追加する操作:")
    print("   計算量: O(1) [償却]")
    print("   理由: 通常は定数時間だが、配列の再割り当てが必要な場合はO(n)になる")
    print()
    
    print("3. 配列内のすべての要素を2倍にする操作:")
    print("   計算量: O(n)")
    print("   理由: 各要素を1回ずつ処理する必要があるため")
    print()
    
    print("4. 2つの配列を結合する操作:")
    print("   計算量: O(n + m)")
    print("   理由: nとmは各配列のサイズで、すべての要素をコピーする必要があるため")
    print()
    
    print("5. 入れ子の2つのfor文の中で配列要素を処理する操作:")
    print("   計算量: O(n²)")
    print("   理由: 外側のループがn回、内側のループがそれぞれn回実行されるため")

def analyze_mystery_function():
    """Mystery関数の計算量分析"""
    print("\nMystery関数の計算量分析:")
    print("----------------------------------")
    print("関数コード:")
    print("""
    def mystery_function(n):
        result = 0
        for i in range(n):
            for j in range(i, n):
                result += i * j
        return result
    """)
    
    print("分析:")
    print("  外側のループは n 回実行")
    print("  内側のループは、iの値に応じて (n-i) 回実行")
    print("  合計の実行回数: n + (n-1) + (n-2) + ... + 1 = n(n+1)/2")
    print("  計算量: O(n²)")

if __name__ == "__main__":
    analyze_linear_search()
    analyze_operations()
    analyze_mystery_function()
