# # Reading Files
def Reading_Files():
    single_read = []
    Infile = input("Write your path of input file : \n")
    Outfile = input("Write your path of output file : \n")
    Infile +=".txt"
    Outfile +=".txt"
    with open(Infile, 'r') as fh:
        Input = [line for line in fh]
    #print(Input)

    with open(Outfile, 'r') as fh:
        Output = [line for line in fh]
    #print(Output)    

    for sub in Input:
        single_read.append(sub.replace("\n", ""))
    return single_read,Output


# # Single Read assembly
def Single_Read(single_read):
    Right, Left, Result = [], [], []
    Start, End, N = 0, 0, 1


    # # Finding Size
    Size = int(single_read[0])
    #print(Size)
    single_read.pop(0)
    #single_read

    # # Draw Graph
    for read in single_read:
        Right.append(read[1:])
        Left.append(read[:len(read)-1])

    # Finding Start & End of the path 
    for j in range(len(Left)):
        if Left[j] not in Right:
            Start = j
            break

    for j in range(len(Right)):
        if Right[j] not in Left:
            End = j
            break

    # # Draw Path
    Result.append(Left[Start])
    Result.append(Right[Start])
    for i in range(len(Left)):
        if Result[N] in Left:
            if Result[N] == Result[N-1]:
                Left.remove(Result[N])
                Right.remove(Result[N])
        
            P_index= Left.index(Result[N])
            Result.append(Right[P_index])
    
        N+= 1
        if Result[N] == Right[End]:
            break

    # # Assemble Genome
    concate = Result[0]
    for i in range(1,len(Result)):
        concate += Result[i][-1]
    #print(concate)
    return concate


# # Pair Read assembly
def Pair_read(pair_read):
    prefix, Prefixes1, Prefixes2  = [], [], []
    suffix, Suffixes1, Suffixes2  = [], [], []
    
    # Read size and gap
    K,D = pair_read[0].split()
    pair_read.pop(0)
    size = int(K)
    Gap = int(D)
        
    # # Split Prefixs and Suffixes using (|)
    for line in pair_read:
        p = line.split('|')
        prefix.append(p[0])
        suffix.append(p[1])
    
    # # Draw Graph
    for i in range(len(prefix)):
        Prefixes1.append(prefix[i][:size-1])
        Prefixes2.append(prefix[i][1:])
        Suffixes1.append(suffix[i][:size-1])
        Suffixes2.append(suffix[i][1:])
    
    flag = 0
    # # Find Start and End of the path
    for x in range(len(Prefixes1)):
        if (Prefixes1[x] not in Prefixes2) or (Suffixes1[x] not in Suffixes2):
            Start = x
            flag +=1
        if (Prefixes2[x] not in Prefixes1) or (Suffixes2[x] not in Suffixes1):
            End = x
            flag+=1
        if flag == 2:
            break
            
    # # Find Path
    Result = [[Prefixes1[Start],Suffixes1[Start]],[Prefixes2[Start],Suffixes2[Start]]]
    for i in range(1,len(Prefixes1)):
        for index in range(len(Prefixes1)):
            if (Result[i][0] == Prefixes1[index]) and (Result[i][1] == Suffixes1[index]):
                Result.append([Prefixes2[index],Suffixes2[index]])
                break
        if (Result[i][0] == Prefixes2[End]) and (Result[i][1]== Suffixes2[End]):
            break    

    # # Assemble genome        
    p = Result[0][0][0]
    s = Result[0][1][0]
    for i in range(1,len(Result)-1):
        p += Result[i][0][0]
        s += Result[i][1][0]
    p += Result[len(Result)-1][0][:]
    s += Result[len(Result)-1][1][:]
    idx = len(s)-(size+Gap)
    Genome = p + s[idx:]
    return Genome


# # Checking accuracy 
def check(Output,concate):

    if Output[0] == concate:
        print("\nTesting :Congrate")
    else:
        print("\nTesting :Fail")


# # Main 
if __name__ == "__main__":
    while True:   
        SORP = input("Write (S) if you want Single read && (P) if you want Pair read : \n")
        In , Out = Reading_Files()
        if SORP == "S" or SORP == "s":
            assembly = Single_Read(In)
            print("\nGenome : " ,assembly)
            c= check(Out,assembly)
        elif SORP == "P" or SORP == "p":
            assembly = Pair_read(In)
            print("\nGenome : " ,assembly)
            c= check(Out,assembly)
        #check(assembly,Out)
        else :
            print("Enter valid choose")
            continue
   
        exit = input("Write (Y) if you want to assemble again if no Write any thing else : \n")
        if exit == "Y" or exit == "y":
            continue
        else:
            break
    

