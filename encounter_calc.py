from typing import Dict
import json
import click
from encounter import Encounter, Enemy


enemy_list = Dict[str, Enemy] = {}
encounter_list: Dict[str, Encounter] = {}
active_encounter: Encounter = None


@click.command('calc')
@click.option('--encounter', '-e', default=active_encounter.name())
def click_calc(encounter):
    encounter_to_calc = encounter_list.get(encounter)
    if encounter_to_calc is not None:
        encounter_to_calc.xp_calc()
        print(encounter_to_calc)
    else:
        print("No encounter named {} found".format(encounter))

@click.command()
@click.option('--name', '-n', type=str)
def create_encounter(name):
    encounter_list[name] = Encounter(name)
    print('Successfully created encounter {}'.format(name))


@click.command()
def create_enemy()

@click.command()
@click.option('--count', '-c', type=int, default=1)
def add_enemy():
    pass


@click.command()
@click.option('--name', '-n', type=str, required=True)
def select_encounter(name):
    global active_encounter
    global encounter_list
    tmp_encounter = encounter_list.get(name)
    if tmp_encounter is not None:
        active_encounter =  tmp_encounter
        print("Active encounter set to {}".format(name))
    else:
        print("")

@click.command()
def calc_all():
    global encounter_list
    encounter_string = 'All current encounters:\n'
    for _, en in encounter_list.items():
        en.xp_calc()
        encounter_string += en 
    print(encounter_string)


@click.command()
@click.argument('enemy_json', type=clikc.File('r'))
def load_enemies(enemy_json):
    global enemy_list
    enemy_list = json.loads(enemy_json.read())

if __name__ == "__main__":
    pass