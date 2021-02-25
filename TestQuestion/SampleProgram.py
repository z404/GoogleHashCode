import itertools
with open('b_little_bit_of_everything.in') as file:
    filedata = file.readlines()
    nop,t2,t3,t4 = [int(i) for i in filedata[0].split()]
    pizzalist = {i:filedata[i+1].split()[1:] for i in range(len(filedata[1:]))}
    print('File has been read')
    
def f(v, i, S, memo):
    if i >= len(v): return 1 if S == 0 else 0
    if (i, S) not in memo:  
        count = f(v, i + 1, S, memo)
        count += f(v, i + 1, S - v[i], memo)
        memo[(i, S)] = count 
    return memo[(i, S)]
    
def g(v, S, memo):
    subset = []
    for i, x in enumerate(v):
        if f(v, i + 1, S - x, memo) > 0:
            subset.append(x)
            S -= x
    return subset

memo = {}
v = [2]*t2+[3]*t3+[4]*t4

combos = []
for i in range(2,nop+1):
    print('Finding subsets')
    if f(v, 0, i, memo) == 0: print("There are no valid subsets.")
    else: combos.append(g(v, i, memo))
print('Combos found')

def perms(lst,lengtharr):
    total = sum(lengtharr)
    permlst = list(itertools.permutations(lst,total))
    memo = []
    for i in permlst:
        start,end,index = 0,lengtharr[0],1
        submission = []
        while end<=len(i):
            a = list(i[start:end])
            a.sort()
            submission.append(a)
            try:
                start,end = end,end+lengtharr[index]
            except:
                break
            index+=1
        if submission in memo:
            continue
        else:
            memo.append(submission)
    return memo
    
def chkscore(lst,dictverify,origin='outer'):
    unique = []
    score = 0
    for i in lst:
        if type(i) == type([]):
            score+=chkscore(i,dictverify,origin='inner')
        else:
            unique.extend(dictverify[i])
    if origin == 'inner':
        return score+len(set(unique))**2
    else:
        return score+len(set(unique))**2,lst


final_results = []
for i in combos[::-1]:
    print('Calculating permutations',i,sum(i))
    total_list = perms(pizzalist,i)
    for j in total_list:
        print('Calculating scores',j)
        final_results.append(chkscore(j,pizzalist))
        print(final_results[-1])
def returnfirstone(val):
    return val[0]

final = max(final_results,key=returnfirstone)[1]

with open('submission.txt','w+') as file:
    file.write(str(len(final))+'\n')
    for i in final:
        k = [str(j) for j in i]
        file.write(str(len(i))+' '+' '.join(k)+'\n')
        

