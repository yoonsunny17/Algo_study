dwarfs = list(int(input()) for _ in range(9))
dwarfs.sort()  # 오름차순으로 정렬
cnt = sum(dwarfs)  # 아홉 난쟁이 키 다 더해줘 일단
fake_1, fake_2 = 0, 0  # 두 가짜 난쟁이 구해줄 변수 초기화

for i in range(9):
    for j in range(i+1, 9):
        # 두 난쟁이 키 뺐을 때 합이 100이 된다면, 빠진 놈들이 가짜다!
        if cnt - (dwarfs[i] + dwarfs[j]) == 100:
            fake_1, fake_2 = dwarfs[i], dwarfs[j]
            break

dwarfs.remove(fake_1)
dwarfs.remove(fake_2)

# for dwarf in dwarfs:
#     print(dwarf, end=' ')
for dwarf in dwarfs:
    print(dwarf)