from kitchen import Rosemary
from kitchen.utensils import Bowl, Oven, Fridge
from kitchen.ingredients import Water, Flour, Salt, Butter, Apple, Lemon, Sugar, Cornstarch, Cinnamon

flour = Flour.take(grams =300)
butter = Butter.take(grams = 250)
sugar = Sugar.take(grams = 150)

fridge = Fridge.use()


bowl = Bowl.use(name = 'flour')
bowl.add(Flour.take(grams = 300))
bowl.add(Salt.take ('teaspoon of salt'))
for i in range(5)
butter.take(grams = 50)




pie_oven = Oven.use()
pie_oven.preheat(degrees = 180)
