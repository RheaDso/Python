class Vehicle:
  def __init__(self, name, engine):
    self.name = name
    self.engine = engine

v1 = Vehicle("Audi", "V8")

print(v1.name)
print(v1.engine)