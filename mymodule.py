print("이 파일은 모듈 테스트용 파일입니다.")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
pi=5.14
print(__name__)
if __name__=="__main__":
    print("메인일때 출력되는 문장")
    print(add(pi,3))