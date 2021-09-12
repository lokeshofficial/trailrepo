class Car:
  def __init__(self,brand_name,model_no):
    self.brand_name = brand_name
    self.model_no = model_no

  def start_engine(self):
    print("Engine Started")

  def stop_engine(self):
    print("Engine Stopped")

  def get_info(self):
    print("Brand Name: "+self.brand_name)
    print("Model No.: "+self.model_no)


c = Car("Benz","C2")
c.get_info()
