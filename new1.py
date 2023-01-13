class turtle:

    def __init__(self, posx,posy,step):
        self.posx = posx
        self.posy = posy
        self.step = step

    def go_up(self):
        self.posy += self.step
        print(f'Новые координаты : {self.posx}, {self.posy}')
    def go_down(self):
        self.posy -= self.step
        print(f'Новые координаты : {self.posx}, {self.posy}')
    def go_right(self):
        self.posx += self.step
        print(f'Новые координаты : {self.posx}, {self.posy}')
    def go_left(self):
        self.posx -= self.step
        print(f'Новые координаты : {self.posx}, {self.posy}')

    def evolve(self):
        self.step += 1
        print(f'Шаг увеличен на 1 и теперь составляет : {self.step}')
    def degrade(self):
        s=0
        s= self.step-1
        if s<=0:
            print('ОШИБКА! Шаг не может быть <=0!!!')
        else:
            self.step -= 1
            print(f'Шаг уменьшен на 1 и теперь составляет : {self.step}')
    def count_moves(self,x2,y2):
        x=abs(x2-self.posx)/self.step
        y=abs(y2-self.posy)/self.step
        if x%1 !=0 or y%1 !=0:
            print('Черепашка не дойдет до этой клетки')
        else:
            print('Черепашка дойдёт за ', x+y,' шагов')


print('Начальные координаты черепашки и размер шага: ')
x=int(input())
y=int(input())
s=int(input())
tur=turtle(x,y,s)

command = 0
while command != 'stop':
    print("Введите команду(up, down, left, right, evolve, degrade, count, stop):")
    command = input()
    if command == 'left':
        tur.go_left()
    elif command == 'right':
        tur.go_right()
    elif command == 'up':
        tur.go_up()
    elif command == 'down':
        tur.go_down()
    elif command == 'evolve':
        tur.evolve()
    elif command == 'degrade':
        tur.degrade()
    elif command == 'count':
        print('Введи координаты точки, куда надо добраться черепашке')
        x2=int(input())
        y2=int(input())
        tur.count_moves(x2,y2)
    elif command == 'stop':
        print("Программа закончена!")
    else:
        print("Команду не удалось распознать!")

