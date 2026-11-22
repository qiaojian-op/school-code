marks = [
 [78, 85, 90, 66],
 [55, 70, 60, 75],
 [92, 88, 95, 90],
 [45, 50, 55, 60],
 [80, 75, 85, 95]
]
Tot_stu=[]
tot=0
below_50=0
print("Student\tsub1\tsub2\tsub3\tsub4")
id=1
for i in marks:
    print(id,end="\t")
    id+=1
    for j in i:
        print(j,end="\t")
        tot+=j
        if j < 50:
            below_50+=1
    Tot_stu.append(tot)
    tot=0
    print("")

for i in Tot_stu:
    print(f"Student {Tot_stu.index(i)}: Totle: {i}\t average: {i/4:.2f}")

ave_sub=[0]*4
for i in range(4):
    for j in range(5):
        ave_sub[i]+=marks[j][i]
    ave_sub[i]/=5

for i in ave_sub:
    print(f"Subject {ave_sub.index(i)+1} Average: {i:.2f}")

Highest_ID=Tot_stu.index(max(Tot_stu))
print(f"Highest performing student: Student {Highest_ID+1}")
print(f"Highest total marks: {Tot_stu[Highest_ID]}")

print(f"Subject with highest average: Subject {ave_sub.index(max(ave_sub))+1}")
print(f"Number of marks below 50: {below_50}")
