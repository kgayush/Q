class Base:

    def __init__(self, color = 'Black', filled = False):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        try:
            if type(new_color) != str:
                raise ValueError
            else:
                self.color = new_color
                return self.color

        except ValueError:
            print("Input must be string.")

    def get_filled(self):
        return self.filled

    def set_filled(self, filled):
        try:
            if type(filled) != bool:
                raise ValueError
            else :
                self.filled = filled
                return self.filled

        except ValueError:
            print("Input must be Boolean.")


class Triangle(Base):
    def __init__(self, area = 12):
        self.area = area 
        self.filled = True

    def get_area(self):
        return self.area

    def set_area(self, new_area):
        try:
            if type(new_area) != int:
                raise ValueError
            else:
                self.area = new_area
                return self.area

        except ValueError:
            print("Input must be an integer.")


    def set_color(self, new_color = 'White'):
        self.color = new_color
        return self.color


class Quadilateral(Base):
    def __init__(self, area = 20):
        self.area = area 
        self.filled = True

    def get_area(self):
        return self.area

    def set_area(self, new_area):
        try:
            if type(new_area) != int:
                raise ValueError
            else:
                self.area = new_area
                return self.area

        except ValueError:
            print("Input must be an integer.")


    def set_color(self, new_color = 'Yellow'):
        self.color = new_color
        return self.color

class ChildTriangle(Triangle):
    def __init__(self, angle = 90, height = 10):
        self.angle = angle
        self.height = height

    def name_of_triangle(self):
        if self.angle == 90:
            print("Right angle triangle.")
        elif self.angle < 90:
            print("Acute angle triangle.")
        else:
            print("Obtuse angle triangle.")


class ChildQuadilateral(Quadilateral):
    def __init__(self, length = 20, height = 20):
        self.length = length
        self.height = height

    def type_of_quadilateral(self):
        print("Square.")


    



        

    


base = Base()
print(f'Color: {base.get_color()}')
print(f'New color: {base.set_color("Red")}')
print(f'Is filled? {base.get_filled()}')
print(f'Now? {base.set_filled(True)}')

triangle = Triangle()
print(f'Triangle area: {triangle.get_area()}')
print(f'New area: {triangle.set_area(15)}')
print(f'Color: {triangle.set_color()}')
print(f'Parent method: {triangle.get_color()}')

quadilateral = Quadilateral()
print(f'Quadilateral area: {quadilateral.get_area()}')
print(f'New area: {quadilateral.set_area(25)}')
print(f'Color: {quadilateral.set_color()}')
print(f'Parent method: {quadilateral.get_color()}')

child_triangle = ChildTriangle()
child_triangle.name_of_triangle()
child_triangle.set_area(35)
print(child_triangle.get_area())
child_triangle.set_color("Brown")
print(child_triangle.get_color())

child_quadilateral = ChildQuadilateral()
child_quadilateral.type_of_quadilateral()
child_quadilateral.set_area(40)
print(child_quadilateral.get_area())
child_quadilateral.set_color("Cyan")
print(child_quadilateral.get_color())