
class Point:
  def __init__(self, x,y):
    self.x_ = x
    self.y_ = y



class Box:
  def __init__(self, p1, p2):
    self.lb = Point(p1)
    self.rt = Point(p2) 
  
