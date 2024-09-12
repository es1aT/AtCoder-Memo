"""
二次元配列に特化した幅優先探索。
「.」は未訪問、「*」は訪問済みを表す。「#」は壁を表す。
"""
from collections import deque

# 入力を受け取る
H, W = map(int, input().split())
sy, sx = map(int, input().split()) # スタートの座標
gy, gx = map(int, input().split()) # ゴールの座標

# 二次元配列の作成（#で囲う）
A = []
for i in range(H):
    A.append(list(input()))

# 幅優先探索
A[sy][sx] = "*" # スタート地点を訪問済みに設定
direction = [[1,0], [-1,0], [0,1], [0,-1]]
queue = deque([[sy, sx, 0]]) # キューの作成とスタートの座標の追加

while queue: # キューに探索すべき座標がある間
    y, x, dist = queue.popleft() # 現在の座標と移動距離を取得
    
    # ゴール判定
    if y == gy and x == gx:
        print(dist) # ゴールまでの最短距離を表示
        break
    
    # 現在の座標の隣接マスをチェック
    for dy, dx in direction:
        next_y, next_x = y+dy, x+dx # 四方向の移動後の座標
        if 0 <= next_y < H and 0 <= next_x < W: # グリッド範囲外へのアクセスを防ぐ
            if A[next_y][next_x] == ".":
                A[next_y][next_x] = "*"
                queue.append([next_y, next_x, dist+1])
else: # whileがbreakされなかった（ゴールに到達できなかった）とき
    print("No")

# # 実行結果を表示
# for i in range(H):
#     print(*A[i], sep="")

"""
グラフに特化した幅優先探索。
未訪問か訪問済みかはvisitedリストで表す。
"""
from collections import deque

# 入力を受け取る
N, X, Y = map(int, input().split())
graph = {}

# グラフの作成
for i in range(N-1):
    a, b = map(int, input().split())
    
    # グラフに頂点番号を追加
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    
    # 無向グラフであるため両方に追加
    graph[a].append(b)
    graph[b].append(a)

# 幅優先探索
queue = deque([[X, 0]]) # キューの作成とスタートの座標の追加
visited = set([X]) # 訪問済みのノードを管理
parent = {} # 親ノードを保存する辞書

while queue: # キューに探索すべき座標がある間
    node, dist = queue.popleft() # 現在のノードと移動距離を取得
    
    # ゴール判定
    if node == Y:
        path = [] # 経路を復元するためのリスト 
        while node != X: # YからXまで親をたどる
            path.append(node)
            node = parent[node]
        path.append(X)
        print(*path[::-1], sep="\n")
        break
    
    # 現在のノードの隣接ノードをチェック
    for nbr in graph[node]:
        if nbr not in visited:
            visited.add(nbr)
            queue.append([nbr, dist+1])
            parent[nbr] = node # 親ノードを記録
