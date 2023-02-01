# from heapq import heappop, heappush

# q = []

# heappush(q, 3)
# heappush(q, 10)
# heappush(q, 1)
# heappush(q, 0)
# heappush(q, 4)

# # print(heappop(q))
# heappop(q)
# print(q)

#############

# import heapq

# q = [9, 20, 1, 8, 5, 0]

# heapq.heapify(q)
# print(q)

##############

# import heapq

# q = []

# heapq.heappush(q, 3)
# heapq.heappush(q, 10)
# heapq.heappush(q, 1)
# heapq.heappush(q, 0)
# heapq.heappush(q, 4)

# print(q)  # [0, 1, 3, 10, 4]

# # q에서 가장 큰 3개의 원소가 담긴 리스트
# print(heapq.nlargest(n=3, iterable=q))  # [10, 4, 3]

# # q에서 가장 작은 3개의 원소가 담긴 리스트
# print(heapq.nsmallest(n=3, iterable=q))  # [0, 1, 3]

##############

import heapq

q = []

heapq.heappush(q, -3)
heapq.heappush(q, -10)
heapq.heappush(q, -1)
heapq.heappush(q, -0)
heapq.heappush(q, -4)

print(-1 * heapq.heappop(q))
