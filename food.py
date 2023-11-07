import sqlite3

conn = sqlite3.connect('foodinfo.db')

cursor = conn.cursor()

west_dessert = ('''
CREATE TABLE IF NOT EXISTS west_dessert (
    Name TEXT PRIMARY KEY NOT NULL,
    Allergy TEXT,
    Popularity INTEGER NOT NULL,            
    Type TEXT);       ''')

west_main = ('''
CREATE TABLE IF NOT EXISTS west_main (
    Name TEXT PRIMARY KEY NOT NULL,
    Veg INTEGER NOT NULL,
    MeatSeafood TEXT, 
    Pasta INTEGER,
    Allergy TEXT,
    Popularity INTEGER NOT NULL,
    ProteinName TEXT);       ''')

west_starter = ('''
CREATE TABLE IF NOT EXISTS west_starter (
    Name TEXT PRIMARY KEY NOT NULL,
    Veg INTEGER NOT NULL,
    Warmth TEXT NOT NULL,
    Allergy TEXT,
    Popularity INTEGER NOT NULL,
    ProteinName TEXT);      ''')

korjan_dessert = ('''
CREATE TABLE IF NOT EXISTS korjan_dessert(
    Name TEXT PRIMARY KEY NOT NULL,
    Warmth TEXT NOT NULL,
    Allergy TEXT,
    Popularity INTEGER NOT NULL);              ''')


korjan_main = ('''
CREATE TABLE IF NOT EXISTS korjan_main(
    Name TEXT PRIMARY KEY NOT NULL,
    Soup INTEGER NOT NULL,
    Veg INTEGER NOT NULL,
    Spicy INTEGER NOT NULL,
    RiceNoodle TEXT NOT NULL,
    MeatSeafood TEXT,
    Allergy TEXT,
    Popularity INTEGER NOT NULL)    ''')

korjan_sidedish = ('''
CREATE TABLE IF NOT EXISTS korjan_sidedish(
    Name TEXT PRIMARY KEY NOT NULL,
    Veg INTEGER NOT NULL,
    Warmth TEXT NOT NULL,
    Spicy INTEGER NOT NULL,
    Raw INTEGER NOT NULL,
    Allergy TEXT,
    Popularity INTEGER NOT NULL)    ''')


insert_wd = '''
INSERT INTO west_dessert (Name, Allergy, Popularity, Type)
VALUES (?,?,?,?);
'''
insert_wm = '''
INSERT INTO west_main (Name,Veg,MeatSeafood,Pasta,Allergy,Popularity,ProteinName)
VALUES(?,?,?,?,?,?,?)
'''
insert_ws = '''
INSERT INTO west_starter (Name,Veg,Warmth,Allergy,Popularity,ProteinName)
VALUES(?,?,?,?,?,?)
'''

insert_kjm = '''
INSERT INTO korjan_main (Name,Soup,Veg,Spicy,RiceNoodle,MeatSeafood,Allergy,Popularity)
VALUES(?,?,?,?,?,?,?,?)
'''
insert_kjs = '''
INSERT INTO korjan_sidedish (Name,Veg,Warmth,Spicy,Raw,Allergy,Popularity)
VALUES(?,?,?,?,?,?,?)
'''
insert_kjd = '''
INSERT INTO korjan_dessert (Name,Warmth,Allergy,Popularity)
VALUES(?,?,?,?)
'''


#(Name, Allergy, Popularity, Type)
wdcontent = [
    ('Tiramisu','egg',1,'Cake'),
    ('Gelato_Icecream','milk',2,'Cold'),
    ('Affogato','egg, caffeine',3,'Cold'),
    ('Cheesecake','milk',4,'Cake'),
    ('Cannoli','milk,nuts',5,'Small Sweets'),
    ('ChocoFudge Cake','milk',6,'Cake'),
    ('Apple_Meringue Pie','egg',7,'Cake'),
    ('Panna Cotta','milk',8,'Small Sweets'),
    ('Creme Brulee','egg',9,'Small Sweets'),
    ('Brownie','wheat, nuts',10,'Small Sweets')    ]

#(Name,Veg,Warmth,Allergy,Popularity,ProteinName)
wscontent = [
    ('Bruschetta',1,'Cold',None,1,None),
    ('Minestrone Soup',1,'Warm',None,2,None),
    ('Haggis Neeps_Tatties:',0,'Warm','Lamb',3,'lamb'),
    ('Arancini',0,'Warm',None,4,'Meat'),
    ('Mozzarella_Burrata',0,'Cold','milk',5,None),
    ('Calamari Fritti',0,'Warm','seafood',6,'Seafood'),
    ('Focaccia',1,'Cold','wheat',7,None),
    ('Sourdough Bread',1,'Warm','wheat',8,None),
    ('Smoked Salmon',0,'Cold','Fish',9,'salmon'),
    ('Steamed Mussels',0,'Warm','shellfish',10,'mussels')]

#(Name,Veg,MeatSeafood,Pasta,Allergy,Popularity,ProteinName)
wmcontent = [
    ('Beef Wellington',0,'Meat',0,'egg,wheat,Beef',17,'Beef'),
    ('Ribeye Steak (Cote de boeuf)',0,'Meat',0,'Beef',8,'Beef'),
    ('Carbonara Pasta',0,'Meat',1,'egg,wheat,Pork',10,'Pork'),
    ('Bolognese Pasta',0,'Meat',1,'wheat,Beef',13,'Beef'),
    ('Venison Steak',0,'Meat',0,'Venison',19,'Venison'),
    ('Lamb Steak (Rump, Rack)',0,'Meat',0,'Lamb',14,'Lamb'),
    ('Beef Sirloin Steak (Tomahawk)',0,'Meat',0,'Beef',4,'Beef'),
    ('Fish Steak (Salmon, Seabass, Cod, Haddock)',0,'Seafood',0,'Fish',7,'Fish'),
    ('Pomodoro Pasta',1,None,1,'wheat',16,'For VEG'),
    ('Pesto Pasta',1,None,1,'nuts,wheat',6,'For VEG'),
    ('Arrabbiata Pasta',1,None,1,'wheat',11,'For VEG'),
    ('Lasagne Pasta',0,'Meat',1,'wheat',3,'For VEG'),
    ('Chicken Breast',0,'Meat',0,'Chicken',18,'Chicken'),
    ('Beef Fillet Steak(Chateaubriand)',0,'Meat',0,'Beef',1,'Beef'),
    ('Pork Chop(Belly)',0,'Meat',0,'Pork',12,'Pork'),
    ('Funghi (Mushroom) Pasta',1,None,1,'mushroom,cheese,wheat',5,'For VEG'),
    ('Spinach_Ricotta Pasta',1,None,1,'cheese,wheat',15,'For VEG'),
    ('Scoglio Pasta(Frutti di Mare)',0,'Seafood',1,'shellfish,wheat,seafood',2,'Seafood'),
    ('Ragu Pasta',0,'Meat',1,'wheat,Beef',9,'Beef')
]
#19 Western MAIN,
#(Name,Soup,Veg,Spicy,RiceNoodle,MeatSeafood,Allergy,Popularity)
kjmcontent = [
    ('Tonkotsu Ramen',1,0,0,'Noodle','Pork','Pork',2),
    ('JJamBBong',1,0,1,'Noodle','Pork,Seafood','seafood',9),
    ('Sundubu JJigae',1,1,1,'Rice','Seafood','seafood',8),
    ('Kimchi JJigae',1,1,1,'Rice','Pork','Pork',10),
    ('DakGalbi',0,0,1,'Rice','Chicken','Chicken',4),
    ('GimBap',0,0,0,'Rice','Pork','Pork',11),
    ('Chicken Katsu (Curry)',0,0,0,'Rice','Chicken','Chicken',6),
    ('Teriyaki Don',0,0,0,'Rice','Chicken','wheat,Chicken',5),
    ('Yaki Soba',0,0,0,'Noodle','Pork','Pork',11),
    ('BibimBap',0,1,1,'Rice','Beef','Beef',1),
    ('Japchae',0,1,0,'Noodle','Beef','Beef',3),
    ('Kimchi Fried Rice',0,1,1,'Rice','Pork','Pork',7)
    ]
#kjside(Name,Veg,Warmth,Spicy,Raw,Allergy,Popularity)
kjscontent = [
    ('KaRaaGe',0,'Warm',0,0,None,4),
    ('Korean Fried Chicken',0,'Warm',1,0,'wheat,Chicken',3),
    ('Mandu(Gyoza)',0,'Warm',0,0,None,5),
    ('Nigiri(Roll)_Vegetarian',1,'Cold',0,1,'egg',8),
    ('Nigiri(Roll)_Seafood',0,'Cold',0,1,'seafood',1),
    ('Sashimi',0,'Cold',0,1,'seafood',6),
    ('Miso Soup',1,'Warm',0,0,None,9),
    ('TTeokBBokki',1,'Warm',1,0,'seafood',2),
    ('Kimchi Pancake',1,'Warm',1,0,'wheat',7)
]
# kjdessert (Name,Warmth,Allergy)
kjdcontent = [
    ('Hotteok','Warm','wheat',4),
    ('Korean CornDog','Warm','wheat',1),
    ('Takoyaki','Warm','wheat,egg,seafood',2),
    ('BingSu','Cold','milk,nuts',5),
    ('Mochi','Cold','wheat',3),
    ('Castella Cake','Warm','egg,wheat',6)
]

cursor.execute(west_dessert)
cursor.execute(west_main)
cursor.execute(west_starter)
cursor.execute(korjan_dessert)
cursor.execute(korjan_main)
cursor.execute(korjan_sidedish)

cursor.executemany(insert_wd,wdcontent)
cursor.executemany(insert_wm,wmcontent)
cursor.executemany(insert_ws,wscontent)
cursor.executemany(insert_kjm,kjmcontent)
cursor.executemany(insert_kjs,kjscontent)
cursor.executemany(insert_kjd,kjdcontent)

conn.commit()
cursor.close()
conn.close()