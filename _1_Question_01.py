#  Challenge 1: Square Numbers and Return Their Sum.
class Point:

    def __init__(self,x,y,z):
        self.x=x
        self.y = y
        self.z = z

    def sqSum(self):
        self.x **=2
        self.y **=2
        self.z **=2
        return (self.x+self.y+self.z)

x=int (input("Enter the 1st number for square sum "))
y=int (input("Enter the 2st number for square sum "))
z=int (input("Enter the 3st number for square sum "))
point=Point(x,y,z)
res=point.sqSum()
print(f"The squred sum is :- {res}")