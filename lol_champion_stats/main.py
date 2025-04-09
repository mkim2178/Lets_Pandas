"""
Code adapted from python-lol-champ-stats by Kelvin Samuel
Source: https://github.com/kks110/python-lol-champ-stats
"""

import requests # use it to send requests to RIOT API
import csv # use it to create a csv file

# name of the columns
COLUMN_NAMES = ["name",
                "title",
                "hp",
                "hp_per_level",
                "mp",
                "mp_per_leve",
                "move_speed",
                "armor",
                "armor_per_level",
                "spell_block",
                "spell_block_per_level",
                "attack_range",
                "hp_regen",
                "hp_regen_per_level",
                "mp_regen",
                "mp_regen_per_level",
                "attack_damage",
                "attack_damage_per_level",
                "attack_speed",
                "attack_speed_per_level"
                ]


def latest_version():
    """
    data_dragon_url: An URL of Data Dragon versions (Provided by Riot). These versions are differed by the region (we will use NA region).
    convert_to_json: use get() function to send a GET request to the data_dragon_url and use json() to decode JSON response -> this returns a huge dictionary
    
    returns the version of "champion"
    """

    data_dragon_url = "https://ddragon.leagueoflegends.com/realms/na.json"
    convert_to_json = requests.get(data_dragon_url).json()
    return convert_to_json["n"]["champion"]


def champion_data_url():
    """
    returns the URL of the latest version of champion data
    """

    return "http://ddragon.leagueoflegends.com/cdn/" + latest_version() + "/data/en_US/champion.json"


def champion_name_and_stats():
    """
    data_url: the URL of the latest version of champion data
    convert_to_json: use requests.get() to send a GET request to a certain URL, convert, and decode the JSON response by using json() -> this returns a huge dictionary
    champion_names: convert_to_json["data"] is a dictionary -> key: champ name, value: champ's information.

    returns a dictionary of champion data and list of champion names
    """

    data_url = champion_data_url()
    convert_to_json = requests.get(data_url).json()
    champion_names = convert_to_json["data"].keys()
    
    return convert_to_json, champion_names


def generate_csv():
    """
    data: a dictionary of champion data
    csv_file_name: name of the csv file that we want to create -> ex) "ver_15.7.1_champion_stats.csv"

    write a csv file by using open(): 
    - file name will be the 'csv_file_name'
    - 'w': command to write a text into the file
    - newline = '': this helps me to avoid extra blank lines while writing a csv file (doesn't automatically convert newline characters: \r, \n, \r\n)
    - encoding = 'utf8': helps me to avoid encoding errors and handle text in english (also can handle other languages)

    writer: define a csv writer, parameters are file name of csv file that we want to write and the delimiter=',' (the delimiter will help to seperate words by a ',')
    
    writer.writerow(COLUMN_NAMES): the first row of the csv file should be the column names

    FOR LOOP:
    iterate the 'champions' list, state each champion's name, title, and every specific stat
    writer.writerow(list of elements): write each champion's information
    """

    data, champions = champion_name_and_stats()
    csv_file_name = "ver_" + latest_version() + "_champion_stats.csv"
    with open(csv_file_name, 'w', newline = '', encoding = 'utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter = ',')
        writer.writerow(COLUMN_NAMES)
        for champion in champions:
            name = data['data'][champion]['name']
            title = data['data'][champion]['title']
            hp = data['data'][champion]['stats']['hp']
            hp_per_level = data['data'][champion]['stats']['hpperlevel']
            mp = data['data'][champion]['stats']['mp']
            mp_per_level = data['data'][champion]['stats']['mpperlevel']
            move_speed = data['data'][champion]['stats']['movespeed']
            armor = data['data'][champion]['stats']['armor']
            armor_per_level = data['data'][champion]['stats']['armorperlevel']
            spell_block = data['data'][champion]['stats']['spellblock']
            spell_block_per_level = data['data'][champion]['stats']['spellblockperlevel']
            attack_range = data['data'][champion]['stats']['attackrange']
            hp_regen = data['data'][champion]['stats']['hpregen']
            hp_regen_per_level = data['data'][champion]['stats']['hpregenperlevel']
            mp_regen = data['data'][champion]['stats']['mpregen']
            mp_regen_per_level = data['data'][champion]['stats']['mpregenperlevel']
            attack_damage = data['data'][champion]['stats']['attackdamage']
            attack_damage_per_level = data['data'][champion]['stats']['attackdamageperlevel']
            attack_speed = data['data'][champion]['stats']['attackspeed']
            attack_speed_per_level = data['data'][champion]['stats']['attackspeedperlevel']
            writer.writerow([name, title, hp, hp_per_level, mp, mp_per_level, move_speed, armor, armor_per_level, spell_block, spell_block_per_level, attack_range, hp_regen, hp_regen_per_level, mp_regen, mp_regen_per_level, attack_damage, attack_damage_per_level, attack_speed, attack_speed_per_level])
            
def main():
    generate_csv()
    print("CSV FILE HAS BEEN SUCCESSFULLY CREATED")

if __name__ == "__main__":
    main()
