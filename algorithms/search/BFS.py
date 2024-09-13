"""
幅優先探索（BFS）のコード
一般的には以下の用途で使用され、現時点では訪問順序のみ実装。

訪問順序：探索の際にノードがどの順番で訪問されたか。
最短距離：あるノード（start）から他のノード（goal）までの最短距離。
到達可能性：あるノードから特定のノードまで到達可能かどうか。
最短経路の復元：ノード間の最短経路そのもの（どのノードを通るか）を復元。
"""

from collections import deque

def bfs(li, S):
  visited = [False]*len(li) # ノードに訪問済みかを記録
  queue = deque([S]) # 探索するノードを格納するキュー
  visited[S] = True
  order = []　# 訪問順序を格納するリスト

  while queue: # キューにノードがある間
    i = queue.popleft()
    order.append(i)

    for neighbor in li[i]:
      if visited[neighbor] == False:
        visited[neighbor] = True
        queue.append(neighbor)
  return order


# 開始ノード S と、グラフの隣接リスト li を定義（テスト用）
S = 0
li = [
    [2, 1],       # ノード 0 の隣接ノード
    [0, 3, 4],    # ノード 1 の隣接ノード
    [0, 5, 6],    # ノード 2 の隣接ノード
    [1],          # ノード 3 の隣接ノード
    [1],          # ノード 4 の隣接ノード
    [2],          # ノード 5 の隣接ノード
    [2]           # ノード 6 の隣接ノード
]

print("訪問順序:", *bfs(li, 0))
