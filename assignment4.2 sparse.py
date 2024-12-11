def TransposeSparseMatrix(sp_r, n, cl, nz_el):
    # Initialize transpose matrix and counts
    trans_sp = [None] * (nz_el + 1)
    ct = [0] * cl
    trans_sp[0] = [cl, n, nz_el]
    
    # Count non-zero elements in each column
    for i in range(1, nz_el + 1):
        ct[sp_r[i][1]] += 1
    
    # Compute the index positions
    index = [1] * (cl + 1)
    for i in range(1, cl + 1):
        index[i] = index[i - 1] + ct[i - 1]
    
    # Populate the transposed matrix
    for i in range(1, nz_el + 1):
        x = index[sp_r[i][1]]
        trans_sp[x] = [sp_r[i][1], sp_r[i][0], sp_r[i][2]]
        index[sp_r[i][1]] += 1
    
    # Display the transposed sparse matrix
    print("\nTranspose of the Sparse Matrix:")
    for row in trans_sp:
        print(row)
    
    return trans_sp

def SimpleTranspose(sp_r):
    trans_sp=[]
    trans_sp.append([sp_r[0][1],sp_r[0][0],sp_r[0][2]])
    
    for i in range(sp_r[0][1]):
        for j in range(1,sp_r[0][2]+1):
            if(sp_r[j][1]==i):
                trans_sp.append([sp_r[j][1],sp_r[j][0],sp_r[j][2]])
    return trans_sp
    
def addSparse(m1, m2):
    # Add two sparse matrices
    if m1[0][0] != m2[0][0] or m1[0][1] != m2[0][1]:
        print("Error: Matrices must have the same dimensions.")
        return
    
    m, n = m1[0][0], m1[0][1]
    c1, c2 = 1, 1
    result = [[m, n, 0]]
    count = 0
    
    while c1 < len(m1) and c2 < len(m2):
        if m1[c1][0] == m2[c2][0] and m1[c1][1] == m2[c2][1]:
            result.append([m1[c1][0], m1[c1][1], m1[c1][2] + m2[c2][2]])
            c1 += 1
            c2 += 1
            count += 1
        elif m1[c1][0] == m2[c2][0]:
            if m1[c1][1] < m2[c2][1]:
                result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
                c1 += 1
            else:
                result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
                c2 += 1
            count += 1
        elif m1[c1][0] < m2[c2][0]:
            result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
            c1 += 1
            count += 1
        else:
            result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
            c2 += 1
            count += 1
    
    while c1 < len(m1):
        result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
        c1 += 1
        count += 1
    while c2 < len(m2):
        result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
        c2 += 1
        count += 1
    
    result[0][2] = count
    
    print("\nSum of the Sparse Matrices:")
    for row in result:
        print(row)

def getMatrix():
    # Get a sparse matrix from user input
    try:
        m = int(input("Enter number of rows: "))
        n = int(input("Enter number of columns: "))
    except ValueError:
        print("Invalid input. Please enter integer values.")
        return None
    
    matrix = []
    count = 0
    print("Enter the non-zero elements (enter 0 for no element):")
    
    for i in range(m):
        for j in range(n):
            try:
                x = int(input(f"Element at position ({i},{j}): "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                return None
            if x != 0:
                matrix.append([i, j, x])
                count += 1
    
    return [[m, n, count]] + matrix

def main():
    while True:
        try:
            menu = int(input("Enter the number of times you want to run the program (0 to exit): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        if menu == 0:
            break
        
        while menu > 0:
            try:
                n = int(input("Enter the number of rows: "))
                cl = int(input("Enter the number of columns: "))
            except ValueError:
                print("Invalid input. Please enter integer values.")
                continue
            
            sp_r = [[n, cl, 0]]
            nz_el = 0
            
            print("\nEnter the sparse matrix:")
            for i in range(n):
                print(f"Row {i + 1}:")
                for j in range(cl):
                    try:
                        x = int(input(f"Element at position ({i},{j}): "))
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
                        continue
                    if x != 0:
                        sp_r.append([i, j, x])
                        nz_el += 1
            
            sp_r[0][2] = nz_el
            print("\nSparse matrix:")
            for row in sp_r:
                print(row)
            
            try:
                value = int(input("\nEnter the value of the function to be executed (1 for Transpose, 2 for Simple Transpose, 3 for Addition): "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            
            if value == 1:
                TransposeSparseMatrix(sp_r, n, cl, nz_el)
            elif value == 2:
                result = SimpleTranspose(sp_r)
                print("\nSimple Transpose of the Sparse Matrix:")
                for row in result:
                    print(row)
            elif value == 3:
                print("\nInput for Matrix 1:")
                m1 = getMatrix()
                if m1 is None:
                    continue
                print("\nMatrix 1:", m1)
                
                print("\nInput for Matrix 2:")
                m2 = getMatrix()
                if m2 is None:
                    continue
                print("\nMatrix 2:", m2)
                
                addSparse(m1, m2)
            else:
                print("Invalid choice. Please select a valid option.")
            
            menu -= 1

if __name__ == "__main__":
    main()
