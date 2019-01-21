gameBg = [[00,1,2],[10,11,12],[20,21,22]]
for row in gameBg:
    print(row)
# ----Proceed to play---


row = int(input("Enter row to change"))
col = int(input("Enter col to change"))
gameBg[row][col] = "x"
for row in gameBg:
    print(row)
