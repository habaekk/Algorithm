num_people, m2 = map(int, input().split())
people_sum = num_people * m2
a, b, c, d, e = map(int, input().split())
print(f"%d %d %d %d %d" %(a - people_sum, b-people_sum, c-people_sum, d-people_sum, e-people_sum))