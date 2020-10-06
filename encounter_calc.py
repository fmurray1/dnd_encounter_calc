from typing import Dict
import click
from .encounter import Encounter, Enemy

encounter_list: Dict[str, Encounter] = {}
active_encounter: Encounter = None

@click.command()
def calc(en:Encounter):
    modifier = 1
    total_xp = 0
    if en.total_enemies == 2:
        modifier = 1.5
    elif en.total_enemies >= 3 and en.total_enemies <= 6:
        modifier = 2
    elif en.total_enemies >= 7 and en.total_enemies <= 10:
        modifier = 2.5
    elif en.total_enemies >= 11 and en.total_enemies <= 14:
        modifier = 3
    else:
        modifier = 4

    for enemy in en.enemies():
        total_xp += enemy.xp()
    return total_xp*modifier


@click.command()
@click.option('--name', '-n', type=str)
def create_encounter(name):
    encounter_list[name] = Encounter()


@click.command()
@click.option('--count', '-c', type=int, default=1)
def add_enemy():
    pass

if __name__ == "__main__":
    pass