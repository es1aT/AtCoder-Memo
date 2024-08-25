def prime(x):  #素数探索
    if x < 2:  # 2より小さい数値は素数ではない
        print("No")
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            print("No")
    print("Yes")

def binary_search(arr, target):  #二分探索法
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

def bubble(A):  #バブルソート
    for i in range(len(A) - 1):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

stack = []  #スタック
stack.append('a')
stack.append('b')
print(stack.pop())

from collections import deque  #キュー
queue = deque()
queue.append('a')
queue.append('b')
print(queue.popleft())


def prefix_sum(li, L, R):  #累積和
    B = [0] * (len(li) + 1)
    for i in range(len(li)):
        B[i + 1] = B[i] + li[i]
    return B[R] - B[L - 1]

N = int(input()) #隣接リストのテンプレ
graph = [[] for _ in range(N)]
for _ in range(N):
  u, v = map(int, input().split())
  graph[u-1].append(v-1)
  graph[v-1].append(u-1)

def gcd(a, b):  #ユークリッドの互除法
    while b != 0:
        a, b = b, a % b
    return a

def fib(n):  #フィボナッチ数列（再帰型、直感的だが低効率）
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

def fib(n):  #フィボナッチ数列（反復型、抽象的だが高効率）
    a, b = 0, 1
    if n == 0:
        return a
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

class TreeNode:　# 木構造の作成
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def make_tree(tree, i=0):
    if i < len(tree) and tree[i] is not None:
        node = TreeNode(tree[i])
        node.left = make_tree(tree, 2 * i + 1)
        node.right = make_tree(tree, 2 * i + 2)
        return node
    return None
root = make_tree([1, 2, 3, 4, 5, 6, 7])
print(root.left.left.val, root.left.right.val, root.right.right.val)

from collections import deque
# ノード数 N と、グラフの隣接リスト E を定義
N = 7
li = [
    [1, 2],       # ノード 0 の隣接ノード
    [0, 3, 4],    # ノード 1 の隣接ノード
    [0, 5, 6],    # ノード 2 の隣接ノード
    [1],          # ノード 3 の隣接ノード
    [1],          # ノード 4 の隣接ノード
    [2],          # ノード 5 の隣接ノード
    [2]           # ノード 6 の隣接ノード
]

# 開始ノード S
S = 0
visited = [False]*N
Q = deque([S])
visited[S] = True
while len(Q) > 0:
  i = Q.popleft()
  for j in li[i]:
    if visited[j] == False:
      visited[j] = True
      Q.append(j)
