 # definiamo una classe Person
class Person:
 # definiamo un __init__ che assegna nome e cognome all'istanza
 def __init__(self, name, surname):
  self.name = name
  self.surname = surname
# definiamo uno __str__ che restituisce nome e cognome
 def __str__(self):
  return '{} {}'.format(self.name, self.surname)
# definiamo uno __repr__ che restituisce il tipo dell'istanza
 def __repr__(self):
  return '<Person object ({} {})>'.format(self.name, self.surname)

# creiamo un'istanza di Person
p = Person('Ezio', 'Melotti')
# l'interprete stampa automaticamente il repr() dell'oggetto
# e il metodo p.__repr__() viene invocato


print(repr(p))
print(str(p))

# se usiamo str(), print(), o format(), p.__str__() viene chiamato
# automaticamente e il nome completo viene restituito


print('Welcome {}!'.format(p))
