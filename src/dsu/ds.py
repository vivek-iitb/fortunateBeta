
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


class queue:
  def __init__(self):
    self.queue_ =[]

  def is_empty(self):
    return len(self.queue_)==0
    
  def peek(self):
    if not self.is_empty():
      return self.queue_[0] 
    return "Empty queue"

  def push(self,value):
    self.queue_.append(value)
  
  def pop(self):
    self.queue_.pop(0)

  def show(self):
    print ("queue: " , self.queue_)

   

def test_stack():
  s = Stack()
  q = Queue()
  for a in [s,q]:
    s.is_empty()
    s.push(1)
    s.push(10)
    s.push(100)
    s.push(100)
    s.show()
    s.pop()
    print(s.peek())
    print(s.is_empty())




if __name__=="__main__":
  test_stack();
