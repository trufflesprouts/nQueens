def nQueens(n):
    valid_boards = []
    def find_valid_boards(row, cols, diags, anti_diags):
        if row == n:
            # e.g. when adding a queen in column index 1, add 1 ".", then 1 "Q", then (n-2) "."s
            valid_boards.append(["."*c + "Q" + "."*(n-c-1) for c in cols])
            return 
        for col in range(n):
            diag = row-col
            anti_diag = row+col
            if col not in cols and diag not in diags and anti_diag not in anti_diags:
                find_valid_boards(row+1, cols + [col], diags + [diag], anti_diags + [anti_diag])
    find_valid_boards(0, [], [], [])
    return valid_boards

def runtest(n, expected):
    actual = nQueens(n)
    if expected == actual:
        print(str(n) + ":" + "success")
    else:
        print(str(n) + ":" + "fail")
        print("expected:", expected)
        print("actual:", actual)

def main():
    runtest(1, [["Q"]])
    runtest(2, [])
    runtest(3, [])
    runtest(4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
    runtest(5, [["Q....","..Q..","....Q",".Q...","...Q."],["Q....","...Q.",".Q...","....Q","..Q.."],[".Q...","...Q.","Q....","..Q..","....Q"],[".Q...","....Q","..Q..","Q....","...Q."],["..Q..","Q....","...Q.",".Q...","....Q"],["..Q..","....Q",".Q...","...Q.","Q...."],["...Q.","Q....","..Q..","....Q",".Q..."],["...Q.",".Q...","....Q","..Q..","Q...."],["....Q",".Q...","...Q.","Q....","..Q.."],["....Q","..Q..","Q....","...Q.",".Q..."]])

if __name__ == '__main__':
    main()