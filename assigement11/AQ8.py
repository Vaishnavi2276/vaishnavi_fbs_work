size=10
board = [[0]* size for _ in range(size)]


num = 1
for i in range(size-1, -1, -1):  
    if (size-1-i) % 2 == 0:      
        for j in range(size):
            board[i][j] = num
            num += 1
    else:                         
            board[i][j] = num
            num += 1


for row in board:
    for cell in row:
        print(f"{cell:3}", end=" ")
    print()