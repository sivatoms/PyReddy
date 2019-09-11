from array import *

# Working with Dictionary
if __name__ == '__main__':

    lst = []
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
print(student_marks)
#print(query_name)

for name, scores in student_marks.items():
    if name == query_name:
        tt = scores
        #print(tt)
        #tt.tolist()

r=0.0
for i in range(len(tt)):
    r = r + tt[i]

result = "%0.2f" % float(r/len(tt))  # adding decimal place to a number using "%0.2f" % float()
print(result)



