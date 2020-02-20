import numpy as np
import os
import workfunction

def getT(e):
    return e[1]

def getScore(e):
    return e[1]

def score(indexes_of_books, books):
    result = 0
    for i in indexes_of_books:
        result += books[i]
    return result

bo = []

def readInput(path_data):
    with open(path_data) as f:
        lines = f.readlines()
        n_books, n_libraries, n_days = np.asarray(lines[0].split()).astype(int)
        scores_of_books = np.asarray(lines[1].split(), int)

        st = [(i,s) for i,s in enumerate(scores_of_books)]

        ss = sorted(st,key=getScore,reverse=True)
        bo = [i[0] for i in ss]
        s = [i[1] for i in ss]
        main_dict = {idx: val for idx, val in enumerate(scores_of_books)}
        line_index = 2
        libraries = {}
        for lib_index in range(int(n_libraries)):
            bs = np.asarray(lines[line_index + 1].split(), int)
            bs = sorted(bs, key=lambda x: bo.index(x))
            libraries[lib_index] = [np.asarray(lines[line_index].split(), int),
                                    bs ,
                                    score(np.asarray(lines[line_index + 1].split(), int), scores_of_books)]
            line_index += 2
    return (n_books,n_libraries,n_days),libraries,s

p,d,s = readInput(os.path.join("datasets", "a_example.txt"))

days = p[2]

count = 1

z = []
ls = []

f = ''

liblines=[]
booklines=[]

for day in range(days):
    scores = []
    dzs = []
    if len(ls) == len(d):
        break
    for lib_i,lib in d.iteritems():
        if lib_i in ls:
            continue
        Tj = lib[0][1]
        Mj = lib[0][2]
        score,dZ = workfunction.maxScore(s,lib[1],z,days,day,Tj,Mj)
        scores.append((lib_i,score,dZ))
        dzs.append(dZ)
    scores= sorted(scores,key=getScore,reverse=True)

    libsubm = '{} {}\n'.format(scores[0][0],len(dZ))
    booksubm = ''
    for b in dZ:
        booksubm+=str(b)+' '
    booksubm+='\n'
    liblines.append(libsubm)
    booklines.append(booksubm)
    ls.append(scores[0][0])
    z += scores[0][2]
    

f+='{}\n'.format(len(ls))

for i,v in enumerate(liblines):
    f+=liblines[i]
    f+=booklines[i]

print f

outfile = 'out_a.txt'

with open(outfile,'w+') as file:
    file.write(f)

# Ts = []

# worklist = []

# for i,v in d.iteritems():
#     Ts.append((i,v[0][1]))

# Ts = sorted(Ts,key=getT)





# outfile_b = 'b_out.txt'

# with open(outfile_b,'w+') as f:

#     header = '{}'.format(len(Ts))
#     print header
#     f.write(header+'\n')

#     for i,v in enumerate(Ts):
#         libsubm = ''
#         booksubm = ''

#         libsubm = '{} {}'.format(v[0],np.min([days-count,len(d[v[0]][1])]))

#         for b in d[v[0]][1][:days-count]:
#             booksubm += str(b) + ' '
        
#         count+=1
#         f.write(libsubm+'\n')
#         f.write(booksubm+'\n')



