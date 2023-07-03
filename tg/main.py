from aiogram import types,executor,Dispatcher,Bot
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from TOKEN import Token
from api import create_feedback
from order import *
from buttons import *
from text import *

bot = Bot(token=Token)
dp = Dispatcher(bot=bot,storage=MemoryStorage())

many_count = ['1','2','3','4','5','6','7','8','9','10']
users_list = []
order_prize = {
  'Mushroom soup':2,
  'Onion rings':1,
  'Chicken wings':5,
  'Caesar salad':1,
  'Chef salad':5,
  'Tomato salad':1,
  'Steak and Chips':10,
  'Pizza':5,
  'Club sandwich':5,
  'Pasta':3,
  'Apple pie':6,
  'Cheesecake':5,
  'Ice cream':0.8,
  'Water 0.5':0.2,
  'Water 1':0.3,
  'Water 1.5':0.4,
  'Pepsi 0.5':0.5,
  'Pepsi 1':0.9,
  'Pepsi 1.5':1.1,
  'Coca Cola 0.5':0.5,
  'Coca Cola 1':0.9,
  'Coca Cola 1.5':1.1,
  'Fanta 0.5':0.6,
  'Fanta 1':1,
  'Fanta 1.5':1.2,
  'Tea':1.2,
}
users = {}

menu = ['Appetisers','Salads','Main courses','Desserts','Beverages']
menu_item = ['Mushroom soup','Onion rings','Chicken wings','Caesar salad','Chef salad','Tomato salad','Steak and Chips','Pizza','Club sandwich','Pasta','Apple pie','Cheesecake','Ice cream','Water 0.5','Water 1','Water 1.5','Pepsi 0.5','Pepsi 1','Pepsi 1.5','Coca Cola 0.5','Coca Cola 1','Coca Cola 1.5','Fanta 0.5','Fanta 1','Fanta 1.5','Tea']

@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
  photo = open('logo.png','rb')
  await message.answer_photo(photo=photo)
  await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\nBu Roziqbek RestaurantBot\nMenu bilan tanishish uchun /menu bosing\nBuyurtma berish uchun /order bosing")

@dp.message_handler(commands=['menu'])
async def menu_command(message:types.Message):
  photo = open('234.jpg','rb')
  await message.answer_photo(photo=photo,caption='Bizning /menu',reply_markup=inkeyboard1)

@dp.message_handler(text=['Appetisers','Salads','Main courses','Desserts','Beverages'])
async def menu_items(message:types.Message):
  if message.text == 'Appetisers':
    await message.answer(text=Appetisers,reply_markup=keyboard1,parse_mode="HTML")
  elif message.text == 'Salads':
    await message.answer(text=Salads,reply_markup=keyboard2,parse_mode="HTML")
  elif message.text == 'Main courses':
    await message.answer(text=Main_courses,reply_markup=keyboard3,parse_mode="HTML")
  elif message.text == 'Desserts':
    await message.answer(text=Desserts,reply_markup=keyboard4,parse_mode="HTML")
  elif message.text == 'Beverages':
    await message.answer(text=Beverages,reply_markup=keyboard5,parse_mode="HTML")

@dp.message_handler(text=['Back','Mushroom soup','Onion rings','Chicken wings','Caesar salad','Chef salad','Tomato salad','Steak and Chips','Pizza','Club sandwich','Pasta','Apple pie','Cheesecake','Ice cream','Water 0.5','Water 1','Water 1.5','Pepsi 0.5','Pepsi 1','Pepsi 1.5','Coca Cola 0.5','Coca Cola 1','Coca Cola 1.5','Fanta 0.5','Fanta 1','Fanta 1.5','Tea'])
async def items(message:types.Message):
  if message.text == 'Mushroom soup':
    photo = open('mushroom_soup.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Mushroom soup prize ${order_prize["Mushroom soup"]}\nMushroom soup recipe\n\n{mushroom}')
  elif message.text == 'Onion rings':
    photo = open('Onion_rings.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Onion rings prize ${order_prize["Onion rings"]}\nOnion rings recipe\n\n{onion}')
  elif message.text == 'Chicken wings':
    photo = open('Chicken_wings.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Chicken wings prize ${order_prize["Chicken wings"]}\nChicken wings recipe\n\n{chicken}')
  elif message.text == 'Caesar salad':
    photo = open('Caesar_salad.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Caesar salad prize ${order_prize["Caesar salad"]}\nCaesar salad recipe\n\n{Caesar}')
  elif message.text == 'Chef salad':
    photo = open('Chef_salad.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Chef salad prize ${order_prize["Chef salad"]}\nChef salad recipe\n\n{Chef}')
  elif message.text == 'Tomato salad':
    photo = open('Tomato_salad.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Tomato salad prize ${order_prize["Tomato salad"]}\nTomato salad recipe\n\n{Tomato}')
  elif message.text == 'Steak and Chips':
    photo = open('Steak_and_Chips.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Steak and Chips prize ${order_prize["Steak and Chips"]}\nSteak and Chips recipe\n\n{Steak}')
  elif message.text == 'Pizza':
    photo = open('Pizza.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Pizza prize ${order_prize["Pizza"]}\nPizza recipe\n\n{Pizza}')
  elif message.text == 'Club sandwich':
    photo = open('Club_sandwich.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Club sandwich prize ${order_prize["Club sandwich"]}\nClub sandwich recipe\n\n{Club}')
  elif message.text == 'Pasta':
    photo = open('Pasta_of_the_day.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Pasta prize ${order_prize["Pasta"]}\nPasta recipe\n\n{Pasta}')
  elif message.text == 'Apple pie':
    photo = open('Apple_pie.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Apple pie prize ${order_prize["Apple pie"]}\nApple pie recipe\n\n{Apple}')
  elif message.text == 'Cheesecake':
    photo = open('Cheesecake.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Cheesecake prize ${order_prize["Cheesecake"]}\nCheesecake recipe\n\n{Cheesecake}')
  elif message.text == 'Ice cream':
    photo = open('Ice_cream.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Ice cream prize ${order_prize["Cheesecake"]}')
  elif message.text == 'Water 0.5':
    photo = open('Water.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Water 0.5 prize ${order_prize["Water 0.5"]}')
  elif message.text == 'Water 1':
    photo = open('Water.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Water 1 prize ${order_prize["Water 1"]}')
  elif message.text == 'Water 1.5':
    photo = open('Water.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Water 1.5 prize ${order_prize["Water 1.5"]}')
  elif message.text == 'Pepsi 0.5':
    photo = open('Pepsi.png','rb')
    await message.answer_photo(photo=photo,caption=f'Pepsi 0.5 prize ${order_prize["Pepsi 0.5"]}')
  elif message.text == 'Pepsi 1':
    photo = open('Pepsi.png','rb')
    await message.answer_photo(photo=photo,caption=f'Pepsi 1 prize ${order_prize["Pepsi 1"]}')
  elif message.text == 'Pepsi 1.5':
    photo = open('Pepsi.png','rb')
    await message.answer_photo(photo=photo,caption=f'Pepsi 1.5 prize ${order_prize["Pepsi 1.5"]}')
  elif message.text == 'Coca Cola 0.5':
    photo = open('Coca_Cola.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Coca Cola 0.5 prize ${order_prize["Coca Cola 0.5"]}')
  elif message.text == 'Coca Cola 1':
    photo = open('Coca_Cola.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Coca Cola 1 prize ${order_prize["Coca Cola 1"]}')
  elif message.text == 'Coca Cola 1.5':
    photo = open('Coca_Cola.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Coca Cola 1.5 prize ${order_prize["Coca Cola 1.5"]}')
  elif message.text == 'Fanta 0.5':
    photo = open('Fanta.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Fanta 0.5 prize ${order_prize["Fanta 0.5"]}')
  elif message.text == 'Fanta 1':
    photo = open('Fanta.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Fanta 1 prize ${order_prize["Fanta 1"]}')
  elif message.text == 'Fanta 1.5':
    photo = open('Fanta.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Fanta 1.5 prize ${order_prize["Fanta 1.5"]}')
  elif message.text == 'Tea':
    photo = open('Tea.jpg','rb')
    await message.answer_photo(photo=photo,caption=f'Tea prize ${order_prize["Tea"]}')
  elif message.text == 'Back':
    photo = open('234.jpg','rb')
    await message.answer_photo(photo=photo,caption='Bizning /menu',reply_markup=inkeyboard1)

@dp.message_handler(commands=['info'])
async def info_command(message:types.Message):
  data = users[message.from_user.id]
  i1 = data['food']
  f1 = order_prize[i1]
  m1 = int(data['many'])*f1
  zakaz_info = f"""
  Sizning buyurtmangiz

name: {message.from_user.full_name}
telefon: +{data['tel']}
location: {data['location']}
1st food: {data['food']} ${m1}

TOTAL: ${m1}
  """
  if 'food2' in data:
    i2 = data['food2']
    f2 = order_prize[i2]
    m2 = int(data['many2'])*f2
    s2 = m1+m2
    zakaz_info = f"""
  Sizning buyurtmangiz

name: {message.from_user.full_name}
telefon: +{data['tel']}
location: {data['location']}
1st food: {data['food']} ${m1}
2nd food: {data['food2']} ${m2}

TOTAL: ${s2}
    """
  if 'food2' and 'food3' in data:
    i3 = data['food3']
    f3 = order_prize[i3]
    m3 = int(data['many3'])*f3
    s3 = s2+m3
    zakaz_info = f"""
    Sizning buyurtmangiz

name: {message.from_user.full_name}
telefon: +{data['tel']}
location: {data['location']}
1st food: {data['food']} ${m1}
2nd food: {data['food2']} ${m2}
3rd food: {data['food3']} ${m3}

TOTAL: ${s3}
    """
  if 'food2' and 'food3' and 'food4' in data:
    i4 = data['food4']
    f4 = order_prize[i4]
    m4 = int(data['many4'])*f4
    s4 = s3+m4
    zakaz_info = f"""
    Sizning buyurtmangiz

name: {message.from_user.full_name}
telefon: +{data['tel']}
location: {data['location']}
1st food: {data['food']} ${m1}
2nd food: {data['food2']} ${m2}
3rd food: {data['food3']} ${m3}
4th food: {data['food4']} ${m4}

TOTAL: ${s4}
    """
  if 'food2' and 'food3' and 'food4' and 'food5' in data:
    i5 = data['food5']
    f5 = order_prize[i5]
    m5 = int(data['many5'])*f5
    s5 = s4+m5
    zakaz_info = f"""
    Sizning buyurtmangiz

name: {message.from_user.full_name}
telefon: +{data['tel']}
location: {data['location']}
1st food: {data['food']} ${m1}
2nd food: {data['food2']} ${m2}
3rd food: {data['food3']} ${m3}
4th food: {data['food4']} ${m4}
5th food: {data['food5']} ${m5}

TOTAL: ${s5}
    """
  await message.answer(zakaz_info)

@dp.message_handler(commands=['order'])
async def order_command(message:types.Message):
  state = dp.current_state(user=message.from_user.id)
  await message.answer("iltimos telefon nomeringizni kiriting\n(Masalan: 998912345678)")
  # await state.get_state(Order.tel)
  await Order.tel.set()

@dp.message_handler(state=Order.tel)
async def tel_command(message: types.Message,state:FSMContext):
  tel = message.text
  if len(str(tel))==12 and str(tel[:3])=='998':
    await state.update_data({'tel':tel})
    await message.answer('Iltimos location bering')
    await Order.next()
  else:
    await message.answer('Iltimos telefon nomeringizni tugri kiriting!!!\n(Masalan: 998912345678)')

@dp.message_handler(state=Order.location)
async def location_command(message: types.Message,state:FSMContext):
  location = message.text
  await state.update_data({'location':location})
  await message.answer('Iltimos zakaz bering',reply_markup=inkeyboard1)
  await Order.next()

@dp.message_handler(state=Order.food)
async def food_command(message:types.Message,state:FSMContext):
  if message.text == 'Appetisers':
    await message.answer(text=Appetisers,reply_markup=keyboard1_1,parse_mode='HTML')
  elif message.text == 'Salads':
    await message.answer(text=Salads,reply_markup=keyboard2_2,parse_mode='HTML')
  elif message.text == 'Main courses':
    await message.answer(text=Main_courses,reply_markup=keyboard3_3,parse_mode='HTML')
  elif message.text == 'Desserts':
    await message.answer(text=Desserts,reply_markup=keyboard4_4,parse_mode='HTML')
  elif message.text == 'Beverages':
    await message.answer(text=Beverages,reply_markup=keyboard5_5,parse_mode='HTML')
  if message.text in menu_item:
    food = message.text
    await state.update_data({'food':food})
    await message.answer('Qancha olasiz ?',reply_markup=keyboard6)
    await Order.next()

@dp.message_handler(state=Order.many)
async def many_command(message: types.Message,state:FSMContext):
  if message.text in many_count:
    many = message.text
    await state.update_data({'many':many})
    await message.answer('Yana nimadir hohlaysizmi ?',reply_markup=check_keyboard)
    await Order.next()

@dp.message_handler(state=Order.check1)
async def check_command(message:types.Message,state:FSMContext):
  check1 = message.text
  if check1 == ('Ha' or 'ha'):
    await state.update_data({'check':check1})
    await message.answer('Yana nima hohlaysiz',reply_markup=inkeyboard1)
    await Order.next()
  elif check1 == ("Yo'q" or "yo'q"):
    data = await state.get_data()
    users[message.from_user.id] = data
    await state.finish()
    await message.answer(create_feedback(user_id=message.from_user.full_name,tel=data['tel'],location=data['location'],food=data['food'],many=data['many'],check1='-----',food2='-----',many2='-----',check2='-----',food3='-----',many3='-----',check3='-----',food4='-----',many4='-----',check4='-----',food5='-----',many5='-----'))
    await message.answer('Sizning buyurtmangiz qabul qilindi /info')
    print(users)
  else:
    await message.answer("""Iltimos "Ha" yoki "Yo'q" tugmalorni bosing!""")

@dp.message_handler(state=Order.food2)
async def food_command2(message:types.Message,state:FSMContext):
  if message.text == 'Appetisers':
    await message.answer(text=Appetisers,reply_markup=keyboard1_1,parse_mode='HTML')
  elif message.text == 'Salads':
    await message.answer(text=Salads,reply_markup=keyboard2_2,parse_mode='HTML')
  elif message.text == 'Main courses':
    await message.answer(text=Main_courses,reply_markup=keyboard3_3,parse_mode='HTML')
  elif message.text == 'Desserts':
    await message.answer(text=Desserts,reply_markup=keyboard4_4,parse_mode='HTML')
  elif message.text == 'Beverages':
    await message.answer(text=Beverages,reply_markup=keyboard5_5,parse_mode='HTML')
  if message.text in menu_item:
    food2 = message.text
    await state.update_data({'food2':food2})
    # await message.answer('Yana nimadir hohlaysizmi ?',reply_markup=check_keyboard)
    await message.answer('Qancha olasiz ?',reply_markup=keyboard6)
    await Order.next()

@dp.message_handler(state=Order.many2)
async def many_command(message: types.Message,state:FSMContext):
  if message.text in many_count:
    many2 = message.text
    await state.update_data({'many2':many2})
    await message.answer('Yana nimadir hohlaysizmi ?',reply_markup=check_keyboard)
    await Order.next()

@dp.message_handler(state=Order.check2)
async def check_command2(message:types.Message,state:FSMContext):
  check2 = message.text
  if check2 == ('Ha' or 'ha'):
    await state.update_data({'check2':check2})
    await message.answer('Yana nima hohlaysiz',reply_markup=inkeyboard1)
    await Order.next()
  elif check2 == ("Yo'q" or "yo'q"):
    data = await state.get_data()
    users[message.from_user.id] = data
    await state.finish()
    await message.answer(create_feedback(user_id=message.from_user.full_name,tel=data['tel'],location=data['location'],food=data['food'],many=data['many'],check1='-----',food2=data['food2'],many2=data['many2'],check2='-----',food3='-----',many3='-----',check3='-----',food4='-----',many4='-----',check4='-----',food5='-----',many5='-----'))
    await message.answer('Sizning buyurtmangiz qabul qilindi /info')
    print(users)
  else:
    await message.answer("""Iltimos "Ha" yoki "Yo'q" tugmalorni bosing!""")

@dp.message_handler(state=Order.food3)
async def food_command3(message:types.Message,state:FSMContext):
  if message.text == 'Appetisers':
    await message.answer(text=Appetisers,reply_markup=keyboard1_1,parse_mode='HTML')
  elif message.text == 'Salads':
    await message.answer(text=Salads,reply_markup=keyboard2_2,parse_mode='HTML')
  elif message.text == 'Main courses':
    await message.answer(text=Main_courses,reply_markup=keyboard3_3,parse_mode='HTML')
  elif message.text == 'Desserts':
    await message.answer(text=Desserts,reply_markup=keyboard4_4,parse_mode='HTML')
  elif message.text == 'Beverages':
    await message.answer(text=Beverages,reply_markup=keyboard5_5,parse_mode='HTML')
  if message.text in menu_item:
    food3 = message.text
    await state.update_data({'food3':food3})
    # await message.answer('Yana nimadir hohlaysizmi ?',reply_markup=check_keyboard)
    await message.answer('Qancha olasiz ?',reply_markup=keyboard6)
    await Order.next()

@dp.message_handler(state=Order.many3)
async def many_command(message: types.Message,state:FSMContext):
  if message.text in many_count:
    many3 = message.text
    await state.update_data({'many3':many3})
    await message.answer('Yana nimadir hohlaysizmi ?',reply_markup=check_keyboard)
    await Order.next()

@dp.message_handler(state=Order.check3)
async def check_command3(message:types.Message,state:FSMContext):
  check3 = message.text
  if check3 == 'Ha':
    await state.update_data({'check3':check3})
    await message.answer('Yana nima hohlaysiz',reply_markup=inkeyboard1)
    await Order.next()
  elif check3 == ("Yo'q" or "yo'q"):
    data = await state.get_data()
    users[message.from_user.id] = data
    await state.finish()
    await message.answer(create_feedback(user_id=message.from_user.full_name,tel=data['tel'],location=data['location'],food=data['food'],many=data['many'],check1='-----',food2=data['food2'],many2=data['many2'],check2='-----',food3=data['food3'],many3=data['many3'],check3='-----',food4='-----',many4='-----',check4='-----',food5='-----',many5='-----'))
    await message.answer('Sizning buyurtmangiz qabul qilindi /info')
    print(users)
  else:
    await message.answer("""Iltimos "Ha" yoki "Yo'q" tugmalorni bosing!""")

@dp.message_handler(state=Order.food4)
async def food_command4(message:types.Message,state:FSMContext):
  if message.text == 'Appetisers':
    await message.answer(text=Appetisers,reply_markup=keyboard1_1,parse_mode='HTML',)
  elif message.text == 'Salads':
    await message.answer(text=Salads,reply_markup=keyboard2_2,parse_mode='HTML')
  elif message.text == 'Main courses':
    await message.answer(text=Main_courses,reply_markup=keyboard3_3,parse_mode='HTML')
  elif message.text == 'Desserts':
    await message.answer(text=Desserts,reply_markup=keyboard4_4,parse_mode='HTML')
  elif message.text == 'Beverages':
    await message.answer(text=Beverages,reply_markup=keyboard5_5,parse_mode='HTML')
  if message.text in menu_item:
    food4 = message.text
    await state.update_data({'food4':food4})
    # await message.answer('Yana nimadir hohlaysizmi ?',reply_markup=check_keyboard)
    await message.answer('Qancha olasiz ?',reply_markup=keyboard6)
    await Order.next()

@dp.message_handler(state=Order.many4)
async def many_command(message: types.Message,state:FSMContext):
  if message.text in many_count:
    many4 = message.text
    await state.update_data({'many4':many4})
    await message.answer('Yana nimadir hohlaysizmi ?',reply_markup=check_keyboard)
    await Order.next()

@dp.message_handler(state=Order.check4)
async def check_command3(message:types.Message,state:FSMContext):
  check4 = message.text
  if check4 == 'Ha':
    await state.update_data({'check4':check4})
    await message.answer('Yana nima hohlaysiz',reply_markup=inkeyboard1)
    await Order.next()
  elif check4 == ("Yo'q" or "yo'q"):
    data = await state.get_data()
    users[message.from_user.id] = data
    await state.finish()
    await message.answer(create_feedback(user_id=message.from_user.full_name,tel=data['tel'],location=data['location'],food=data['food'],many=data['many'],check1='-----',food2=data['food2'],many2=data['many2'],check2='-----',food3=data['food3'],many3=data['many3'],check3='-----',food4=data['food4'],many4=data['many4'],check4='-----',food5='-----',many5='-----'))
    await message.answer('Sizning buyurtmangiz qabul qilindi /info')
    print(users)
  else:
    await message.answer("""Iltimos "Ha" yoki "Yo'q" tugmalorni bosing!""")

@dp.message_handler(state=Order.food5)
async def food_command4(message:types.Message,state:FSMContext):
  if message.text == 'Appetisers':
    await message.answer(text=Appetisers,reply_markup=keyboard1_1,parse_mode='HTML')
  elif message.text == 'Salads':
    await message.answer(text=Salads,reply_markup=keyboard2_2,parse_mode='HTML')
  elif message.text == 'Main courses':
    await message.answer(text=Main_courses,reply_markup=keyboard3_3,parse_mode='HTML')
  elif message.text == 'Desserts':
    await message.answer(text=Desserts,reply_markup=keyboard4_4,parse_mode='HTML')
  elif message.text == 'Beverages':
    await message.answer(text=Beverages,reply_markup=keyboard5_5,parse_mode='HTML')
  if message.text in menu_item:
    food5 = message.text
    await state.update_data({'food5':food5})
    await message.answer('Qancha olasiz ?',reply_markup=keyboard6)
    await Order.next()

@dp.message_handler(state=Order.many5)
async def many_command(message: types.Message,state:FSMContext):
  if message.text in many_count:
    many5 = message.text
    await state.update_data({'many5':many5})
    # await message.answer('Yana nimadir hohlaysizmi ?',reply_markup=check_keyboard)
    data = await state.get_data()
    users[message.from_user.id] = data
    await message.answer(create_feedback(user_id=message.from_user.full_name,tel=data['tel'],location=data['location'],food=data['food'],many=data['many'],check1='-----',food2=data['food2'],many2=data['many2'],check2='-----',food3=data['food3'],many3=data['many3'],check3='-----',food4=data['food4'],many4=data['many4'],check4='-----',food5=data['food5'],many5=data['many5']))
    await message.answer('Sizning buyurtmangiz qabul qilindi /info')
    print(users)
    await state.finish()

if __name__ == '__main__':
  executor.start_polling(dp,skip_updates=True)