from kitchen import Rosemary
from kitchen.utensils import Bowl, Plate, BakingTray, Oven
from kitchen.ingredients import Sugar, Egg, Butter, Salt, Flour, ChocolateChips, BakingPowder

sugar =Sugar.take(grams = 200)
flour = Flour.take(grams =300)
chocolatechips = ChocolateChips.take(grams =200)
butter = Butter.take(grams = 50)
bakingpowder = BakingPowder.take('some')

#Mixing ingredients 
bowl = Bowl.use(name ='sugar')
bowl.add(Sugar.take(grams = 200))

for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)

bowl.add(Salt.take('a pinch of salt'))

for i in range (6): 
    flour.take(grams = 50)

bowl.add(Flour.take(grams = 50))
bowl.add(ChocolateChips.take(grams = 200))
bowl.add(bakingpowder)
bowl.mix()

bakingtray = BakingTray.use(name ='Chocolate Chip Cookies')
bakingtray.add(bowl.take())

#Baking cookies
cookies_oven = Oven.use()
cookies_oven.preheat(degrees = 175)
cookies_oven.add(bakingtray)
cookies_oven.bake(minutes = 10)
cookies_oven_bakingtray = cookies_oven.take()


plate = Plate.use (name = 'Chocolate Chip Cookies')
plate.add(cookies_oven_bakingtray.take())

Rosemary.serve(plate)




