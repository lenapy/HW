def check_input(func):
    def wrapper(*args):
        allowed_numbers = ['1', '2', '3', '4']
        if args[1] not in allowed_numbers:
            raise Exception('Invalid input!')
        res = func(*args)
        return res
    return wrapper


class Square:
    def __init__(self, side_len):
        self.side_len = side_len if isinstance(side_len, int) and side_len >= 4 else 4

    def create_square(self):
        square = [[0] * self.side_len for i in range(self.side_len)]
        return square

    @staticmethod
    def print_square(square):
        for sides in square:
            print(' '.join(str(side) for side in sides))

    @check_input
    def draw_new_square(self, choice):
        square = self.create_square()
        for i in range(self.side_len):
            for j in range(self.side_len):
                if choice == '1':
                    if i <= j:
                        square[i][j] = '*'
                elif choice == '2':
                    if i >= j:
                        square[i][j] = '*'
                elif choice == '3':
                    if i + j >= self.side_len - 1:
                        square[i][j] = '*'
                elif choice == '4':
                    if i + j <= self.side_len - 1:
                        square[i][j] = '*'
        self.print_square(square)


def user_choice():
        choice = input('select which part of square will be paint in * :\n'
                       '1. top right corner\n'
                       '2. bottom left corner\n'
                       '3. bottom right corner\n'
                       '4. top left corner\n'
                       )
        return choice


def user_side_len():
    user_input = input("Choice len of square sides:\n")
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        print("You must choose a number!")
        user_side_len()


if __name__ == '__main__':
    len_of_sides = user_side_len()
    s = Square(len_of_sides)
    number_choice = user_choice()
    s.draw_new_square(number_choice)
