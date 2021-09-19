class Car:
  def __init__(self,brand_name,model_no):
    self.brand_name = brand_name
    self.model_no = model_no

  def turn_ac(self,flag):
    print('AC is :'+ flag)

  def start_engine(self):
    print("Engine Started")

  def stop_engine(self):
    print("Engine Stopped")

  def get_info(self):
    print("Brand Name: "+self.brand_name)
    print("Model No.: "+self.model_no)


c = Car("BMW","X4")
c.get_info()

# This is also changeddd