n, k = map(int, input().split())
words = [input() for _ in range(k)]

basic = {'a', 'n', 't', 'i', 'c'}
remain_alpha = set(chr(i) for i in range(97, 123) if chr(i) not in basic)

print(remain_alpha)