import sys
input = sys.stdin.readline

grade = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}
tcrd = 0
score = 0
for i in range(20):
    sub, credit, grd = input().split()
    if grd == 'P':
        continue
    tcrd+=float(credit)
    score+=(float(credit)*grade[grd])

print(f"{round(score/tcrd,6):.6f}")