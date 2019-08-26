# 190826_algorithm study day 3

## 03 순열,조합, 중복 순열, 중복 조합

**순열**

약 12~14!을 넘어가게되면 1초 이상 걸리기 때문에 완전탐색 보다는 중간에 걸러내는 방식이 좋다.

순열

조합

중복 순열 n Pi r = n ^ r

중복 조합 n H r = n+r-1 C r

1,1 1,2 1,3 2,2 2,3 3,3





순열 생성 재귀적 알고리즘: depth도 함께 고려해야 한다.

```
visited[n-1]
perm(k)
	if k==R print arr
	else
		for i: 0 ~ n-1
			if visited[i] continue
			t[k] = a[i]
			visited[i] = true
			perm(k+1)
			visited[i] = false
```

백트래킹, 가지치기: 구성 요소가 조건을 만족하는지 여부를 다음 단계로 넘어가기 전에 판단하여 가지치기를 한다. 중간중간 break요소를 판단하는 것이 중요.

조합

중복 순열

```
pi(k)
	if k == r print arr
	else 
		for i: 0 ~ n-1
		t[k]=a[i]
		pi(k+1)
```

중복 조합

```
h(k, s) //깊이, 시작 숫자
	if k==r print arr
	else
		for int i: s ~ n
			t[k] = a[i]
			h(k+1, i)
```

ex) 동전 조합하는 문제.

​	1, 4, 6원 동전으로 8원 만들기

​	앞에서 탐색한 조합에 대해 생략하도록.

생성은 완전검색으로 검색하면서 해당 요소에 대하여 DFS / BFS

itertools의 단점: 상태공간트리를 전부 탐색하고 나서 작업을 진행하기 때문에 느리다.

TSP(travelling salesman problem) 