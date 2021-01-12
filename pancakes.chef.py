from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Flour, Egg, Milk, Salt, Butter

flour = Flour.take(grams = 250) 
egg = Egg.take(2)
milk = Milk.take(ml = 500)
salt = Salt.take('a dash of salt')

# Whisking the eggs in a bowl
bowl = Bowl.use(name ='eggs')
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)

bowl.mix()

Salt.take('a dash of salt')
for i in range (5): 
    flour.take(grams = 50)

bowl.add(Flour.take(grams = 50))
bowl.add(Milk.take(ml = 250))
bowl.mix()

bowl.add(milk.take(ml =250))
bowl.mix()

plate = Plate.use (name = 'pancake')
#Baking 8 pancakes on each side 
pancake_pan = Pan.use (name = 'pancake')
for i in range (8):
#Make a single pancake
    pancake_pan.add(Butter.take('slice'))
    pancake_pan.add(bowl.take('1/8'))
    pancake_pan.cook(minutes = 1)
    pancake_pan.flip()
    pancake_pan.cook(minutes = 1)
    plate.add(pancake_pan.take())
 
Rosemary.serve(plate)



