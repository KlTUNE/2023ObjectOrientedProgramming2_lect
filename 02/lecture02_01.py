#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

def lecture02_01_printHeroStatus() -> None:
    hero_header = []
    hero_data = []
    with open('lecture02_Hero.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(hero_header) == 0:
                hero_header = row
            else :
                hero_data.append(row)

    for row in hero_data:
        if row[0] == '1':
            print(f"Name:{row[1]} HP:{row[2]} MP:{row[3]} Atk:{row[4]} Def:{row[5]} Age:{row[6]}")

def lecture02_01_printWeaponStatus() -> None:
    weapon_header = []
    weapon_data = []
    with open('lecture02_Weapon.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(weapon_header) == 0:
                weapon_header = row
            else :
                weapon_data.append(row)

    for row in weapon_data:
        if row[0] == '1':
            print(f"Name:{row[1]} HP:{row[2]} MP:{row[3]} Atk:{row[4]} Def:{row[5]} Age:{row[6]}")

def lecture02_01_printHeroStatusWithWeapon() -> None:
    hero_header = []
    hero_data = []
    with open('lecture02_Hero.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(hero_header) == 0:
                hero_header = row
            else :
                hero_data.append(row)

    for row in hero_data:
        if row[0] == '1':
            hero_name = row[1]
            hero_hp = int(row[2])
            hero_mp = int(row[3])
            hero_atk = int(row[4])
            hero_def = int(row[5])
            hero_age = int(row[6])
            hero_weapon = int(row[7])

    weapon_header = []
    weapon_data = []
    with open('lecture02_Weapon.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(weapon_header) == 0:
                weapon_header = row
            else :
                weapon_data.append(row)

    for row in weapon_data:
        if hero_weapon == int(row[0]):
            weapon_name = row[1]
            weapon_hp = int(row[2])
            weapon_mp = int(row[3])
            weapon_atk = int(row[4])
            weapon_def = int(row[5])
            weapon_age = int(row[6])
        else :
            weapon_name = "なし"
            weapon_hp = 0
            weapon_mp = 0
            weapon_atk = 0
            weapon_def = 0
            weapon_age = 0

    print(f"{weapon_name}を装備した{hero_name}のステータスは" +
        f"HP:{hero_hp+weapon_hp}," +
        f"MP:{hero_mp+weapon_mp}," +
        f"Atk:{hero_atk+weapon_atk}," +
        f"Def:{hero_def+weapon_def}," +
        f"Age:{hero_age+weapon_age}")

if __name__ == '__main__':
    lecture02_01_printHeroStatus()
    lecture02_01_printWeaponStatus()
    lecture02_01_printHeroStatusWithWeapon()