from FizzBuzzBase import FizzBuzzBase

class FizzBuzz(FizzBuzzBase):
    __DEFAULT_LOOP_TIME = 20

    def __init__(self, max_count=__DEFAULT_LOOP_TIME):
        super().__init__(max_count)

    def __convert(self, input : int) -> str:
        if input%15==0:
            return 'FizzBuzz'
        elif input%3==0:
            return 'Fizz'
        elif input%5==0:
            return 'Buzz'
        else:
            return str(input)

    def print_fizzbuzz(self, max_count : int) -> None:
        for i in range(max_count):
            print(self.__convert(i+1))

if __name__ == '__main__':
    app = FizzBuzz(20)