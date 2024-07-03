from itertools import combinations
 
def printfunction(numList):
    # 6개의 숫자의 조합을 출력
    for i in combinations(numList, 6):
        print(*i)
 
def main():
    # 0이 입력될 때까지 반복해서 수행
    while True:
 
        # 입력된 전체 값을 배열로 받는다
        inputList = list(map(int, input().split()))
 
        # 0번째는 뒤의 몇 개의 숫자가 입력되었는지
        inputCnt = inputList[0]
        # 1~N번째는 입력된 숫자
        numList = inputList[1:]
 
        # 출력 함수 호출
        printfunction(numList)
 
        # inputCnt가 0일 때 종료
        if inputCnt == 0:
            exit()
        # 구분을 위한 빈 줄 출력
        print()
 
if __name__ == '__main__':
    main()
