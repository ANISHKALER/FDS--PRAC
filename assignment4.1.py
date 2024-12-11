def TransposeSparseMatrix(sp_r,n,cl,nz_el):
    trans_sp=[0]*(nz_el+1)
    ct=[0]*cl
    trans_sp[0]=[cl,n,nz_el]
    for i in range(1,nz_el+1):
        ct[sp_r[i][1]]=ct[sp_r[i][1]]+1
    index=[1]*(cl+1)
    for i in range(1,cl+1):
        index[i]=index[i-1]+ct[i-1]
    for i in range(1,nz_el+1):
        x=index[sp_r[i][1]]
        trans_sp[x]=[sp_r[i][1],sp_r[i][0],sp_r[i][2]]
        index[sp_r[i][1]]=index[sp_r[i][1]]+1
    for i in range(0,nz_el+1):
        print(trans_sp[i])
    return trans_sp

def SimpleTranspose(sp_r):
    trans_sp=[]
    trans_sp.append([sp_r[0][1],sp_r[0][0],sp_r[0][2]])
    
    for i in range(sp_r[0][1]):
        for j in range(1,sp_r[0][2]+1):
            if(sp_r[j][1]==i):
                trans_sp.append([sp_r[j][1],sp_r[j][0],sp_r[j][2]])
    return trans_sp

#sparse matrix
def addSparse(m1, m2):
    if(m1[0][0] == m2[0][0] and m1[0][1] == m2[0][1]):
        m = m1[0][0]
        n = m1[0][1]
        c1 = c2 = 1
        result = [[m, n, 0]]
        count = 0
        while(c1 < len(m1) and c2 < len(m2)):
            if(m1[c1][0] == m2[c2][0] and m1[c1][1] == m2[c2][1]):
                result.append([m1[c1][0], m2[c2][0], m1[c1][0] + m2[c2][0]])
                c1 +=1
                c2 +=1
                count += 1
            elif(m1[c1][0] == m2[c2][0]):
                if(m1[c1][1] < m2[c2][1]):
                    result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
                    c1 +=1
                    count +=1
                else:
                    result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
                    c2 +=1
                    count +=1
            else:
                if(m1[c1][0] < m2[c2][0]):
                    result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
                    c1 +=1
                    count +=1
                else:
                    result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
                    c2 +=1
                    count +=1
        
        while(c1 < len(m1)):
            result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
            c1 +=1
            count +=1
        while(c2 < len(m2)):
            result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
            c2 +=1
            count +=1

        result[0][2] = count
        print(result)

def getMatrix():
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns:"))
    matrix = list();
    count = 0
    for i in range(m):
        for j in range(n):
            x = int(input("Enter element for a[%d][%d]: "%(i,j)))
            if(x != 0):
                matrix.append([i,j,x])
                count += 1

    return [[m,n,count]] + matrix;
   
menu=int(input("Enter the number of times you want to run the program-"))
while (menu!=0):
    n=int(input("Enter the number of row:"))
    cl=int(input("Enter the number of column:"))
    sp=[]
    nz_el=0
    sp_r=[]
    simpletranspose=[]
    sp_r.append([n,cl,0])
    
    for i in range(n):
        spl=[]
        print("enter the elements of",i+1,"the row")
        for j in range(cl):
            x=int(input(""))
            if(x!=0):
                sp_r.append([i,j,x])
                nz_el=nz_el+1
            spl.append(x)
        sp.append(spl)

    sp_r[0][2]=nz_el
    print("sparse matrix is:")
    for i in range(0,nz_el+1):
        print([sp_r[i]])   
    
    value=int(input("enter the value of the function to be executed-"))
    if value==1:
        print("The Transpose of the Sparse Matrix is-")
        TransposeSparseMatrix(sp_r,n,cl,nz_el)
        menu=menu-1
    elif value==2:
        result=SimpleTranspose(sp_r)
        print("The simple Transpose of sparse matrix is-",result)
        menu=menu-1
    elif value==3:
        print("Input matrix1-")
        m1 = getMatrix()
        print("First Sparce matrix is",m1)
        

        print("Input matrix2-")
        m2 = getMatrix()
        print("Second Sparce matrix is",m2)
        
        print("The addition of the sparse matrix is-")
        addSparse(m1, m2)
        menu=menu-1