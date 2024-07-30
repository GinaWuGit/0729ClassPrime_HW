#利用class (類別) 設計一質數判斷: 使用者輸入一數字，列出2~該數間所包含的所有質數併計算質數總數
class PrimeChecker:
    def __init__(self, number):
        self.number = number        #self.number 存入使用者輸入數字
        self.prime_sum = 0          #self.prime_sum 計算質數總數
    
    def is_prime(self, N):
        if N <= 1:
            return False
        for i in range (2, N):
            if N % i == 0:
                return False
        return True

    def count_prime(self):
        for i in range (2, self.number+1):
            if self.is_prime(i):
                print(i)
                self.prime_sum += 1
        print("質數總數為:", self.prime_sum)

if __name__ == '__main__':
    number = int(input("Please enter a number:"))
    UserNum = PrimeChecker(number)
    UserNum.count_prime()
