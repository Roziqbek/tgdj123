from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

inbutton1 = KeyboardButton(text='Appetisers')
inbutton2 = KeyboardButton(text='Salads')
inbutton3 = KeyboardButton(text='Main courses')
inbutton4 = KeyboardButton(text='Desserts')
inbutton5 = KeyboardButton(text='Beverages')

inkeyboard1 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(inbutton1).row(inbutton2).row(inbutton3).row(inbutton4).row(inbutton5)

button1 = KeyboardButton('Mushroom soup')
button2 = KeyboardButton('Onion rings')
button3 = KeyboardButton('Chicken wings')
back = KeyboardButton('Back')

keyboard1 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button1).row(button2).row(button3).row(back)
keyboard1_1 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button1).row(button2).row(button3)

button4 = KeyboardButton('Caesar salad')
button5 = KeyboardButton('Chef salad')
button6 = KeyboardButton('Tomato salad')

keyboard2 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button4).row(button5).row(button6).row(back)
keyboard2_2 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button4).row(button5).row(button6)

button7 = KeyboardButton('Steak and Chips')
button8 = KeyboardButton('Pizza')
button9 = KeyboardButton('Club sandwich')
button10 = KeyboardButton('Pasta')

keyboard3 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button7).row(button8).row(button9).row(button10).row(back)
keyboard3_3 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button7).row(button8).row(button9).row(button10)

button11 = KeyboardButton('Apple pie')
button12 = KeyboardButton('Cheesecake')
button13 = KeyboardButton('Ice cream')

keyboard4 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button11).row(button12).row(button13).row(back)
keyboard4_4 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button11).row(button12).row(button13)

button14 = KeyboardButton('Water 0.5')
button14_1 = KeyboardButton('Water 1')
button14_2 = KeyboardButton('Water 1.5')
button15 = KeyboardButton('Pepsi 0.5')
button15_1 = KeyboardButton('Pepsi 1')
button15_2 = KeyboardButton('Pepsi 1.5')
button16 = KeyboardButton('Coca Cola 0.5')
button16_1 = KeyboardButton('Coca Cola 1')
button16_2 = KeyboardButton('Coca Cola 1.5')
button17 = KeyboardButton('Fanta 0.5')
button17_1 = KeyboardButton('Fanta 1')
button17_2 = KeyboardButton('Fanta 1.5')
button18 = KeyboardButton('Tea')

keyboard5 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button14,button14_1,button14_2).row(button15,button15_1,button15_2).row(button16,button16_1,button16_2).row(button17,button17_1,button17_2).row(button18,back)
keyboard5_5 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button14,button14_1,button14_2).row(button15,button15_1,button15_2).row(button16,button16_1,button16_2).row(button17,button17_1,button17_2).row(button18)

check_button_1 = KeyboardButton('Ha')
check_button_2 = KeyboardButton("Yo'q")
check_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(check_button_1,check_button_2)

# hechta tanlash
button19 = KeyboardButton('1')
button20 = KeyboardButton('2')
button21 = KeyboardButton('3')
button22 = KeyboardButton('4')
button23 = KeyboardButton('5')
button24 = KeyboardButton('6')
button25 = KeyboardButton('7')
button26 = KeyboardButton('8')
button27 = KeyboardButton('9')
button28 = KeyboardButton('10')
keyboard6 = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).add(button19,button20,button21,button22,button23,button24,button25,button26,button27,button28)