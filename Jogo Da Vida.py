from random import randint
c=0
j=7
while j > 6 or j < 2:
    j=int(input('\033[1;30mQuantos jogadores iram participar?\033[m'))
    if j > 6 or j < 2:print('Esse Jogo Pode Ser Jogado De 2 até 6 Pessoas.')
j1='off'
j2='off'
j3='off'
j4='off'
j5='off'
j6='off'
if j>=1:j1='on'
if j>=2:j2='on'
if j>=3:j3='on'
if j>=4:j4='on'
if j>=5:j5='on'
if j>=6:j6='on'

if j1=='on':n1=input('\033[1;31mQual é o nome do jogador 1?\033[m').strip()
if j2=='on':n2=input('\033[1;32mQual é o nome do jogador 2?\033[m').strip()
if j3=='on':n3=input('\033[1;35mQual é o nome do jogador 3?\033[m').strip()
if j4=='on':n4=input('\033[1;34mQual é o nome do jogador 4?\033[m').strip()
if j5=='on':n5=input('\033[1;33mQual é o nome do jogador 5?\033[m').strip()
if j6=='on':n6=input('\033[1;36mQual é o nome do jogador 6?\033[m').strip()
d1=0
d2=0
d3=0
d4=0
d5=0
d6=0
if j1=='on':d1+=10000
if j2=='on':d2+=10000
if j3=='on':d3+=10000
if j4=='on':d4+=10000
if j5=='on':d5+=10000
if j6=='on':d6+=10000
pj=randint(1,j)
if pj==1:print('\033[1;31m{} Começa!\033[m'.format(n1))
if pj==2:print('\033[1;32m{} Começa!\033[m'.format(n2))
if pj==3:print('\033[1;35m{} Começa!\033[m'.format(n3))
if pj==4:print('\033[1;34m{} Começa!\033[m'.format(n4))
if pj==5:print('\033[1;33m{} Começa!\033]m'.format(n5))
if pj==6:print('\033[1;36m{} Começa!\033[m'.format(n6))
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
while True:
    co=input('\033[1;30mO que você deseja?\033[m').strip()
    if co=='girar':print(randint(1,10))
    if co=='add':
        pq=input('\033[1;30mPara quem?\033[m').strip()
        if j1=='on':
            if pq == n1:
                q=int(input('\033[1;30mQuanto?\033[m'))
                d1+=q
        if j2=='on':
            if pq == n2:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d2 += q
        if j3=='on':
            if pq == n3:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d3 += q
        if j4=='on':
            if pq == n4:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d4 += q
        if j5=='on':
            if pq == n5:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d5 += q
        if j6=='on':
            if pq == n6:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d6 += q
    if co == 'mostrar':
        m=input('\033[1;30mDe quem?\033[m').strip()
        if j1 == 'on':
            if m == n1: print('\033[31m{} tem {}R$\033[m'.format(n1,d1))
        if j2 == 'on':
            if m == n2: print('\033[32m{} tem {}R$\033[m'.format(n2,d2))
        if j3 == 'on':
            if m == n3: print('\033[35m{} tem {}R$\033[m'.format(n3,d3))
        if j4 == 'on':
            if m == n4: print('\033[34m{} tem {}R$\033[m'.format(n4,d4))
        if j5 == 'on':
            if m == n5: print('\033[33m{} tem {}R$\033[m'.format(n5,d5))
        if j6 == 'on':
            if m == n6: print('\033[36m{} tem {}R$\033[m'.format(n6,d6))
    if co == 'tirar':
        pq=input('\033[1;30mDe quem?\033[m').strip()
        if j1=='on':
            if pq == n1:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d1-=q
        if j2=='on':
            if pq == n2:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d2 -= q
        if j3=='on':
            if pq == n3:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d3 -= q
        if j4=='on':
            if pq == n4:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d4 -= q
        if j5=='on':
            if pq == n5:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d5 -= q
        if j6=='on':
            if pq == n6:
                q = int(input('\033[1;30mQuanto?\033[m'))
                d6 -= q
    if co == 'presente':
        p=input('\033[1;30mDe quem?\033[m').strip()
        pr=input('\033[1;30mPara quem?\033[m').strip()
        q=int(input('\033[1;30mQuanto?\033[m'))
        if j1 == 'on':
            if p == n1: d1 -= q
            if pr == n1 and p != 'todos': d1 +=q
            if p == 'todos' and pr != n1:
                d1 -= q
                if j2 == 'on':
                    if pr == n2 : d2 += q
                if j3 == 'on':
                    if pr == n3 : d3 += q
                if j4 == 'on':
                    if pr == n4 : d4 += q
                if j5 == 'on':
                    if pr == n5 : d5 += q
                if j6 == 'on':
                    if pr == n6 : d6 += q
        if j2 == 'on':
            if p == n2: d2 -= q
            if pr == n2 and p != 'todos': d2 += q
            if p == 'todos' and pr != n2:
                d2 -= q
                if j1 == 'on':
                    if pr == n1: d1 += q
                if j3 == 'on':
                    if pr == n3 : d3 += q
                if j4 == 'on':
                    if pr == n4 : d4 += q
                if j5 == 'on':
                    if pr == n5 : d5 += q
                if j6 == 'on':
                    if pr == n6 : d6 += q
        if j3 == 'on':
            if p == n3: d3 -= q
            if pr == n3 and p != 'todos': d3 += q
            if p == 'todos' and pr != n3:
                d3 -= q
                if j2 == 'on':
                    if pr == n2 : d2 += q
                if j1 == 'on':
                    if pr == n1 : d1 += q
                if j4 == 'on':
                    if pr == n4 : d4 += q
                if j5 == 'on':
                    if pr == n5 : d5 += q
                if j6 == 'on':
                    if pr == n6 : d6 += q
        if j4 == 'on':
            if p == n4: d4 -= q
            if pr == n4 and p != 'todos': d4 += q
            if p == 'todos' and pr != n4:
                d4 -= q
                if j2 == 'on':
                    if pr == n2 : d2 += q
                if j3 == 'on':
                    if pr == n3 : d3 += q
                if j1 == 'on':
                    if pr == n1 : d1 += q
                if j5 == 'on':
                    if pr == n5 : d5 += q
                if j6 == 'on':
                    if pr == n6 : d6 += q
        if j5 == 'on':
            if p == n5: d5 -= q
            if pr == n5 and p != 'todos': d5 += q
            if p == 'todos' and pr != n5:
                d5 -= q
                if j2 == 'on':
                    if pr == n2 : d2 += q
                if j3 == 'on':
                    if pr == n3 : d3 += q
                if j4 == 'on':
                    if pr == n4 : d4 += q
                if j1 == 'on':
                    if pr == n1 : d1 += q
                if j6 == 'on':
                    if pr == n6 : d6 += q
        if j6 == 'on':
            if p == n6: d6 -= q
            if pr == n6 and p != 'todos': d6 += q
            if p == 'todos' and pr != n6:
                d6 -= q
                if j2 == 'on':
                    if pr == n2 : d2 += q
                if j3 == 'on':
                    if pr == n3 : d3 += q
                if j4 == 'on':
                    if pr == n4 : d4 += q
                if j5 == 'on':
                    if pr == n5 : d5 += q
                if j1 == 'on':
                    if pr == n1 : d1 += q
    if co == 'addsalario':
        sa=(input('\033[1;30mDe quem?\033[m')).strip()
        q=int(input('\033[1;30mQuanto?\033[m'))
        if j1 == 'on':
            if sa == n1: s1 = q
        if j2 == 'on':
            if sa == n2: s2 = q
        if j3 == 'on':
            if sa == n3: s3 = q
        if j4 == 'on':
            if sa == n4: s4 = q
        if j5 == 'on':
            if sa == n5: s5 = q
        if j6 == 'on':
            if sa == n6: s6 = q
    if co == 'salario':
        sal=input('\033[1;30mDe quem?\033[m').strip()
        if j1 == 'on':
            if sal == n1: d1 += s1
        if j2 == 'on':
            if sal == n2: d2 += s2
        if j3 == 'on':
            if sal == n3: d3 += s3
        if j4 == 'on':
            if sal == n4: d4 += s4
        if j5 == 'on':
            if sal == n5: d5 += s5
        if j6 == 'on':
            if sal == n6: d6 += s6
    if co == 'vencedor':
        if j1 == 'on':
            if d1 > d2 and d1 > d3 and d1 > d4 and d1 > d5 and d1 > d6: print('\033[31m{} VENCEU!\033[m'.format(n1))
        if j2 == 'on':
            if d2 > d1 and d2 > d3 and d2 > d4 and d2 > d5 and d2 > d6: print('\033[32m{} VENCEU!\033[m'.format(n2))
        if j3 == 'on':
            if d3 > d2 and d3 > d1 and d3 > d4 and d3 > d5 and d3 > d6: print('\033[35m{} VENCEU!\033[m'.format(n3))
        if j4 == 'on':
            if d4 > d2 and d4 > d3 and d4 > d1 and d4 > d5 and d4 > d6: print('\033[34m{} VENCEU!\033[m'.format(n4))
        if j5 == 'on':
            if d5 > d2 and d5 > d3 and d5 > d4 and d5 > d1 and d5 > d6: print('\033[33m{} VENCEU!\033[m'.format(n5))
        if j6 == 'on':
            if d6 > d2 and d6 > d3 and d6 > d4 and d6 > d5 and d6 > d1: print('\033[36m{} VENCEU\033[m'.format(n6))