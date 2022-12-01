'''
    (يوسف عصام فؤاد محمد - 20191701269)
    (أحمد ناصر أحمد حسن - 20191701016)
    (ضحى عبدالفتاح محمد حسن - 20191701116)
    (عبدالرحمن يسرى إبراهيم البابلى - 20191701124)
    (عبدالرحمن طلبة محمد أحمد - 20191701121)
'''


def SingleReadFn(singleRead):
    Right, Left, Result = [], [], []
    Start, End, N = 0, 0, 1
    Size = int(singleRead[0])
    singleRead.pop(0)

    for read in singleRead:
        Right.append(read[1:])
        Left.append(read[:len(read)-1])
    for j in range(len(Left)):
        if Left[j] not in Right:
            Start = j
            break
    for j in range(len(Right)):
        if Right[j] not in Left:
            End = j
            break

    Result.append(Left[Start])
    Result.append(Right[Start])
    
    for i in range(len(Left)):
        if Result[N] in Left:
            if Result[N] == Result[N-1]:
                Left.remove(Result[N])
                Right.remove(Result[N])
            Result.append(Right[Left.index(Result[N])])
        N += 1
        if Result[N]==Right[End]: break

    holder = Result[0]
    for i in range(1, len(Result)):
        holder += Result[i][-1]
    return holder


def PairReadFn(pairRead):
    prefix, Prefixes1, Prefixes2, suffix, Suffixes1, Suffixes2  = [], [], [], [], [], []
    K, D = pairRead[0].split()
    size, Gap = int(K), int(D)
    pairRead.pop(0)
    
    for line in pairRead:
        p = line.split('|')
        prefix.append(p[0])
        suffix.append(p[1])
    for i in range(len(prefix)):
        Prefixes1.append(prefix[i][:size-1])
        Prefixes2.append(prefix[i][1:])
        Suffixes1.append(suffix[i][:size-1])
        Suffixes2.append(suffix[i][1:])
    
    flag = 0
    for x in range(len(Prefixes1)):
        if (Prefixes1[x] not in Prefixes2) or (Suffixes1[x] not in Suffixes2):
            Start = x
            flag +=1
        if (Prefixes2[x] not in Prefixes1) or (Suffixes2[x] not in Suffixes1):
            End = x
            flag+=1
        if flag == 2: break
    
    Result = [[Prefixes1[Start],Suffixes1[Start]],[Prefixes2[Start],Suffixes2[Start]]]
    for i in range(1, len(Prefixes1)):
        for j in range(len(Prefixes1)):
            if (Result[i][0]==Prefixes1[j]) and (Result[i][1]==Suffixes1[j]):
                Result.append([Prefixes2[j], Suffixes2[j]])
                break
        if (Result[i][0]==Prefixes2[End]) and (Result[i][1]==Suffixes2[End]): break    

    p, s = Result[0][0][0], Result[0][1][0]
    for i in range(1, len(Result)-1):
        p += Result[i][0][0]
        s += Result[i][1][0]
    p += Result[len(Result)-1][0][:]
    s += Result[len(Result)-1][1][:]
    return (p + s[(len(s)-(size+Gap)):])


if __name__ == '__main__':
    while True:   
        SorP = (input('Enter <S> for SingleRead or <P> for PairRead: ')).upper()
        singleRead = []
        Infile = (input('Write the Name of inputFile: ')).upper()
        
        try:
            with open(Infile, 'r') as fh:
                Input = [line for line in fh]
            for sub in Input:
                singleRead.append(sub.replace('\n', ''))
        except:
            print('File not Found!\n')
        
        if SorP == 'S':
            assembly = SingleReadFn(singleRead)
            print('\n >>Genome>> ' ,assembly)
        elif SorP == 'P':
            assembly = PairReadFn(singleRead)
            print('\n >>Genome>> ' ,assembly)
        else :
            print('Enter valid choice!')
            continue
   
        exit = (input('Press (Y) to assemble again: ')).upper()
        if exit == 'Y':
            continue
        else:
            break
    
    print('Thank You!\n')
