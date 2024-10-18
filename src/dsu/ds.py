
class Stack:
  def __init__(self):
    self.stack_ =[]

  def is_empty(self):
    return len(self.stack_)==0
    
  def peek(self):
    if not self.is_empty():
      return self.stack_[-1] 
    return "Empty stack"


  def push(self,value):
    self.stack_.append(value)
  
  def pop(self):
    self.stack_.pop()

  def show(self):
    print ("Stack: " , self.stack_)

def test_stack():
  
  s = Stack()
  s.is_empty()
  s.push(1)
  s.push(10)
  s.push(100)
  s.show()
  s.pop()
  print(s.peek())
  print(s.is_empty())

if __name__=="__main__":
  test_stack();
