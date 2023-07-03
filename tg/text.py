from main import order_prize

Appetisers = f"""
<b>Appetisers</b>

<b>🥘 Mushroom soup</b> - ${order_prize['Mushroom soup']}💸

<b>🧅 Onion rings</b> - ${order_prize['Onion rings']}💸

<b>🍗 Chicken wings</b> - ${order_prize['Chicken wings']}💸
"""

Salads = f"""
<b>🥗 Salads</b>

<b>🥗 Caesar salad</b> - ${order_prize['Caesar salad']}💸

<b>🥗 Chef salad</b> - ${order_prize['Chef salad']}💸

<b>🥗 Tomato salad</b> - ${order_prize['Tomato salad']}💸
"""

Main_courses = f"""
<b>Main_courses</b>

<b>🥩 Steak and Chips</b> - ${order_prize['Steak and Chips']}💸

<b>🍕 Pizza</b> - ${order_prize['Pizza']}💸

<b>🥪 Club sandwich</b> - ${order_prize['Club sandwich']}💸

<b>🍜 Pasta</b> - ${order_prize['Pasta']}💸
"""

Desserts = f"""
<b>Desserts</b>

<b>🥧 Apple pie</b> - ${order_prize['Apple pie']}💸

<b>🍰 Cheesecake</b> - ${order_prize['Cheesecake']}💸

<b>🍦 Ice Cream</b> - ${order_prize['Ice cream']}💸
"""

Beverages = f"""
<b>Beverages</b>

<b>💧 Water 0.5</b> - ${order_prize['Water 0.5']}💸

<b>💧 Water 1</b> - ${order_prize['Water 1']}💸

<b>💧 Water 1.5</b> - ${order_prize['Water 1.5']}💸

<b>🥤 Pepsi 0.5</b> - ${order_prize['Pepsi 0.5']}💸

<b>🥤 Pepsi 1</b> - ${order_prize['Pepsi 1']}💸

<b>🥤 Pepsi 1.5</b> - ${order_prize['Pepsi 1.5']}💸

<b>🥤 Coca Cola 0.5</b> - ${order_prize['Coca Cola 0.5']}💸

<b>🥤 Coca Cola 1</b> - ${order_prize['Coca Cola 1']}💸

<b>🥤 Coca Cola 1.5</b> - ${order_prize['Coca Cola 1.5']}💸

<b>🥤 Fanta 0.5</b> - ${order_prize['Fanta 0.5']}💸

<b>🥤 Fanta 1</b> - ${order_prize['Fanta 1']}💸

<b>🥤 Fanta 1.5</b> - ${order_prize['Fanta 1.5']}💸

<b>☕️ Tea</b> - ${order_prize['Tea']}💸
"""

mushroom= '''
90 g sariyog',
2 o'rta piyoz,
1 bosh sarimsoq,
500 g qo'ziqorin,
2 osh qoshiq oddiy un,
1 l issiq tovuq suvi,
1 dafna yaprog'i,
4 osh qoshiq bitta krem.
'''
onion = """
1 katta piyoz,
yer yong'og'i yog'i,
150 g o'z-o'zidan ko'tariladigan un,
180 ml gazlangan suv.
"""
chicken = """
3 chinnigullar sarimsoq,
2 osh qoshiq zaytun moyi,
3 osh qoshiq sirka,
1 osh qoshiq paprika,
1 osh qoshiq Worcestershire sousi,
2 osh qoshiq selderey tuzi,
4 osh qoshiq qalampir sousi,
1 ½ kg tovuq qanotlari.
"""
Caesar = """
1 ta o'rta siabatta non,
3 osh qoshiq zaytun moyi,
1 katta kos yoki romain salatasi,
1 bosh sarimsoq,
5 osh qoshiq mayonez,
1 osh qoshiq oq sharob sirkasi,
"""
Chef = """
10 ta kichik pomidor
10 g salat bargi,
10 ta bodring,
20 g pishloq.
"""
Tomato = """
100 g pomidor,
20 g maydanoz.
"""
Steak = """
600 g o'rta kattalikdagi kartoshka,
2 x 200 g/8 oz mol go'shti bifteklari,
2 hovuch aralash barglar,
50 g sariyog ',
1 kichik sarimsoq chinnigullar.
"""
Pizza = """
300g strong bread flour,
1 tsp instant yeast,
1 tsp salt,
1 tbsp olive oil, plus extra for drizzling.
"""

Club = """
100 g mol gushti,
3 bo'lak oq non,
1 osh qoshiq mayonez,
1 qattiq qaynatilgan tuxum,
1 ta pomidor,
"""
Pasta = """
3 osh qoshiq zaytun moyi,
1 piyoz,
2 katta sarimsoq chinnigullar,
½ choy qoshiq chilli bo'laklari,
400 g maydalangan pomidor,
5 ta hamsi filetosi,
120 g maydalangan qora zaytun,
2 osh qoshiq kapari,
300 g quritilgan spagetti,
½ kichik shamlardan maydanoz.
"""
Apple = """
500 g un,
100 g olma,
200 g suv,
"""
Cheesecake = """
300 g ovqat hazm qilish pechenesi,
100 g tuzsiz sariyog ',
500 g to'liq yog'li yumshoq pishloq,
100 g shakar,
1 osh qoshiq vanil ekstrakti
300 ml er-xotin krem,
300 g shakar.
"""
Ice = """
Ice cream
"""