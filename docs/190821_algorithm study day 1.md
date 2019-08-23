# 190821_algorithm study day 01

## Orientation

**Rule**

**효율적인 코드를 생각하면 안된다.**

**AD는 TC를 마치고 제출시 Pass/Fail을 알려주지 않는다.**

문제를 먼저 읽고 디자인/ 분석 먼저. 이후 psuedocode를 만든 다음 코딩.

AD: 완전검색, 시뮬레이션

### 완전검색

#### 비선형 자료형

DFS: 스택, 반복 / 재귀

BFS: 반복, 큐

ex) 미로탐색, 레벨 문제

#### 조합론

순열, 부분집합, 조합

반복문, 재귀

백트래킹, 상태공간트리+가지치기



## 01 DFS

**깊이우선탐색**

**비선형 자료구조의 중복 없는 완전탐색**

* 방문한 노드에 대하여 처리
* 방문한 노드의 이웃에 대한 정보를 가지고 탐색.

stack: 처리해야 할 데이터가 남아있는가?

---

**반복**

```pseudocode
visited = []
STACK stack

stack.push(v) 			# push: stack <- v

DFS(v)
	while not isEmpty(stack)
		v <- pop(s)
		if not visited[v]
			visit(v)		# 필요한 작업 수행
			for each w in adjacency(v)
				if not visited[w]
					stack.push(w)
```

**재귀**

```pseudocode
DFS(G, v)

	visited[v] = True
	
	for each all w in adjacency(G, v)
		if not visited[w]
			DFS(G, w)
```

