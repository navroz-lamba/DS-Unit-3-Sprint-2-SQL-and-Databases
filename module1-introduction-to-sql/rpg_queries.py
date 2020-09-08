import sqlite3
# connecting the file 
conn = sqlite3.connect('rpg_db.sqlite3')
# Making a cursor 
c = conn.cursor()

"""How many total Characters are there"""
def total_characters():
    c.execute("SELECT COUNT(*) FROM charactercreator_character;")
    print(c.fetchall())

"""How many of each specific subclass"""
def total_cleric():
    c.execute(" SELECT COUNT(*) FROM charactercreator_cleric")
    print(c.fetchall())


def total_fighter():
    c.execute(" SELECT COUNT(*) FROM charactercreator_fighter")
    print(c.fetchall())


def total_mage():
    c.execute(" SELECT COUNT(*) FROM charactercreator_mage")
    print(c.fetchall())


def total_necromancer():
    c.execute(" SELECT COUNT(*) FROM charactercreator_necromancer")
    print(c.fetchall())

"""How many total Characters are there"""
def total_items():
    c.execute(" SELECT COUNT(*) FROM armory_item")
    print(c.fetchall())

"""How many of the Items are weapons? How many are not?"""
def total_weapons():
    # merge armory_items and armory_weapons
    c.execute(" SELECT COUNT(*) FROM armory_weapon")
    print(c.fetchall())

"""How many Items does each character have? (Return first 20 rows)"""
def total_items_in_each_character():
    c.execute("""SELECT character_id, COUNT(DISTINCT item_id) FROM
            (SELECT cc.character_id, cc.name, ai.item_id, ai.name
            FROM charactercreator_character AS cc,
            armory_item AS ai,
            charactercreator_character_inventory as cci
            WHERE cc.character_id = cci.character_id
            AND cci.item_id = ai.item_id)
            GROUP BY 1
            ORDER BY 2 DESC
            LIMIT 20""") 
    print(c.fetchall())


"""How many Weapon does each character have? (Return first 20 rows)"""
def total_weapons_in_each_character():
    c.execute("""SELECT character_id, COUNT(DISTINCT item_ptr_id) FROM
            (SELECT cc.character_id, cc.name, aw.item_ptr_id
            FROM charactercreator_character AS cc,
            armory_weapon AS aw,
            charactercreator_character_inventory as cci
            WHERE cc.character_id = cci.character_id
            AND cci.item_id = aw.item_ptr_id)
            GROUP BY 1
            ORDER BY 2 DESC
            LIMIT 20""") 
    print(c.fetchall())


"""On average, how many Items does each character have?"""
def avg_number_of_items():
    c.execute(""" SELECT round(AVG(unique_item),3) AS avg_number_of_items FROM
            (SELECT cc.character_id, COUNT(DISTINCT ai.item_id) AS unique_item
            FROM charactercreator_character AS cc,
            armory_item AS ai,
            charactercreator_character_inventory as cci
            WHERE cc.character_id = cci.character_id
            AND cci.item_id = ai.item_id
            GROUP BY 1) """)
    print(c.fetchall())


"""On average, how many Weapons does each character have?"""
def avg_number_of_weapons():
    c.execute(""" SELECT round(AVG(unique_weapons),3) AS avg_number_of_weapons FROM
            (SELECT cc.character_id, COUNT(DISTINCT item_ptr_id) AS unique_weapons
            FROM charactercreator_character AS cc,
            armory_weapon AS aw,
            charactercreator_character_inventory as cci
            WHERE cc.character_id = cci.character_id
            AND cci.item_id = aw.item_ptr_id
            GROUP BY 1) """)
    print(c.fetchall())


avg_number_of_weapons()
