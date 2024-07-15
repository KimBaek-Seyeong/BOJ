'''
n=1 일 때 최소 1회
n=2 일 때 최소 3회
n=3 일 때 최소 7회
n=4 일 때 최소 15회
n=5 일 때 최소 31회
... (2^n - 1)회
'''

def move(n, start, middle, end):
    if n == 1:
        print(start, end)
    else:
        move(n - 1, start, end, middle)
        print(start, end)
        move(n - 1, middle, start, end)
    
def main():
    n = int(input())
    
    # 첫번째 줄에는 최소 횟수
    print(2 ** n - 1)
    # 이동 경로 출력
    move(n, 1, 2, 3)

if __name__ == '__main__':
    main()
