import sys
import pprint
f=open(sys.argv[1], encoding="utf-8")
seq1=f.read()
f.close()

f=open(sys.argv[2],encoding="utf-8")
seq2=f.read()
f.close()

gap=int(sys.argv[3])
match=int(sys.argv[4])
mismatch=int(sys.argv[5])

m=len(seq1)
n=len(seq2)

matrix=[[0 for a in range(m+1)for b in range(n+1)]]

for c in range(m+1):
    matrix[0][c]=gap*c

for d in range(n+1):
    matrix[d][0]=gap*d

x=0
y=0
z=0

for m in range(len(seq1)):
    for n in range(len(seq2)):
        if seq1[m]==seq2[n]:
            x=matrix[n][m]+match
            y=matrix[n+1][m]+gap
            z=matrix[n][m+1]+gap
            matrix[n+1][m+1]=max(x,y,z)
        else:
            w=matrix[n][m]+mismatch
            u=matrix[n+1][m]+gap
            v=matrix[n][m+1]+gap
            matrix[n+1][m+1]=max(w,u,v)

reseq1=[]
reseq2=[]

while m>=0 or n>=0:
    if seq1[m]==seq2[n]:
        if matrix[n+1][m+1]==matrix[n][m]+match:
            reseq1.append(seq1[m])
            reseq2.append(seq2[n])
            m=-1
            n=-1
        elif matrix[n+1][m+1]==matrix[n+1][m]+gap:
            reseq1.append(seq1[m])
            reseq2.append("-")
            m=-1
        else:
            reseq1.append("-")
            reseq2.append(seq2[n])
            n=-1
    else:
        if matrix[n+1][m+1]==matrix[n][m]+mismatch:
            reseq1.append(seq1[m])
            reseq2.append(seq2[n])
            m=-1
            n=-1
        elif matrix[n+1][m+1]==matrix[n+1][m]+match:
            reseq1.append(seq1[m])
            reseq2.append("-")
            m=-1
        else:
            reseq1.append("-")
            reseq2.append(seq2[n])
            n=-1

reseq1.reverse()
reseq2.reverse()

result=str(reseq1)+'¥n'+str(reseq2)

f=open(sys.argv[6],'w',encoding='utf-8')
f.write(result)
f.close

print(matrix)
print(result)