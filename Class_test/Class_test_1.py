class Car:
    def __init__(self, model, year):    ## 클래스에서 정의된 함수를 '메서드'라 한다.(생성자)
        self.model = model          ## 입력받은 값을 바인딩 하기 위한 과정1
        self.year = year            ## 과정2

sonata = Car("SONATA", 2017)
g80 = Car("G80", 2018)

print(sonata.model,sonata.year)
print(g80.model, g80.year)
