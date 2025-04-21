# array_operations.py

def list_operations_demo():
    # リストの作成
    numbers = [1, 2, 3, 4, 5]
    print(f"作成したリスト: {numbers}")
    
    # リストの要素へのアクセス
    print(f"インデックス2の要素: {numbers[2]}")
    
    # リストへの要素追加
    numbers.append(6)
    print(f"要素追加後: {numbers}")
    
    # リストからの要素削除
    numbers.remove(3)  # 値が3の要素を削除
    print(f"要素削除後: {numbers}")
    
    # リストの長さ
    print(f"リストの長さ: {len(numbers)}")
    
    # リスト内に要素が存在するかの確認
    print(f"値4はリスト内に存在するか: {4 in numbers}")
    print(f"値10はリスト内に存在するか: {10 in numbers}")

if __name__ == "__main__":
    list_operations_demo()
