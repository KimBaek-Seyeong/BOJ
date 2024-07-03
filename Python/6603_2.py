def dfs(depth, index, inputCnt, numList):
    global outList
 
    if depth == 6:
        print(*outList)
        return
    for i in range(index, inputCnt):
        outList.append(numList[i])
        dfs(depth + 1, i + 1, inputCnt, numList)
        outList.pop()
 
def main():
    global inputCnt, numList, outList
 
    while True:
        inputList = list(map(int, input().split()))
 
        inputCnt = inputList[0]
        numList = inputList[1:]
 
        outList = []
        dfs(0, 0, inputCnt, numList)
 
        if inputCnt == 0:
            exit()
        print()
 
if __name__ == '__main__':
    main()
