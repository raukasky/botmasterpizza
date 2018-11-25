from telebot import types

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_sets = types.KeyboardButton('💥Сеты')
btn_pizza = types.KeyboardButton('🍕Пицца')
btn_snack = types.KeyboardButton('🍗Закуски')
btn_salad = types.KeyboardButton('🥗Салаты')
btn_dessert = types.KeyboardButton('🍰Десерты')
btn_drinks = types.KeyboardButton('🥤Напитки')
markup_menu.add(btn_sets,btn_pizza,btn_snack,btn_salad,btn_dessert,btn_drinks)