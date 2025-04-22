# Python アルゴリズム学習記録

## 学習進捗

| 日付       | テーマ             | コード                       |
| ---------- | ------------------ | ---------------------------- |
| 2025-04-21 | 配列操作と線形探索 | [コード](./2025-04-21/code/) |
| 2025-04-22 | Big O記法の基礎    | [コード](./2025-04-22/code/) |

## Day 1: 配列操作と線形探索 (2025-04-21)

### 学習内容

- Python のリスト（配列）の基本操作の理解
- 線形探索アルゴリズムの実装
- 拡張課題への取り組み

### 実装したファイル

- [array_operations.py](./2025-04-21/code/array_operations.py) - Python のリスト操作の基本
- [linear_search.py](./2025-04-21/code/linear_search.py) - 線形探索と複数一致の検索
- [extended_search.py](./2025-04-21/code/extended_search.py) - 発展的な検索関数の実装

### 主な実装関数

- `linear_search(arr, target)` - 基本的な線形探索
- `linear_search_all(arr, target)` - すべての一致を検索
- `search_multiple_values(arr, targets)` - 複数の値を一度に検索
- `find_max_value(arr)` - 最大値とそのインデックスを検索

## Day 2: Big O記法の基礎 (2025-04-22)

### 学習内容

- アルゴリズムの効率性を評価するためのBig O記法
- 各種アルゴリズムの計算量分析
- 時間計算量の可視化

### 実装したファイル

- [big_o_examples.py](./2025-04-22/code/big_o_examples.py) - 各計算量クラスの実装例
- [big_o_analysis.py](./2025-04-22/code/big_o_analysis.py) - アルゴリズム操作の計算量分析
- [time_complexity_visualizer.py](./2025-04-22/code/time_complexity_visualizer.py) - 計算量の可視化ツール

### 主な内容

- 定数時間 O(1)、線形時間 O(n)、二次時間 O(n²)、対数時間 O(log n) の例とデモ
- 線形探索アルゴリズムの計算量詳細分析
- 配列操作（挿入、追加、結合等）の計算量分析
- 計算量の成長率をグラフで可視化

次回は「二分探索（バイナリサーチ）アルゴリズム」について学習予定です。
