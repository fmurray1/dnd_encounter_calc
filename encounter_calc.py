from typing import Dict
import json
import click
from click_repl import register_repl
from encounter import Encounter, Enemy


enemy_list: Dict[str, Enemy] = {}
active_encounter: Encounter = Encounter('default')
encounter_list: Dict[str, Encounter] = {'default': active_encounter}

@click.group()
def cli():
    pass

@cli.command('calc')
@click.option('--encounter', '-e', default=active_encounter.name)
def click_calc(encounter):
    global encounter_list
    encounter_to_calc = encounter_list.get(encounter.lower())
    if encounter_to_calc is not None:
        encounter_to_calc.xp_calc()
        click.echo(encounter_to_calc.__repl__())
    else:
        click.echo("No encounter named {} found".format(encounter))

@cli.command()
@click.option('--name', '-n', type=str)
def create_encounter(name):
    global encounter_list
    name= name.lower()
    encounter_list[name] = Encounter(name)
    click.echo('Successfully created encounter {}'.format(name))


@cli.command()
@click.option('--name', '-n', required=True, type=str)
@click.option('--cr', required=True, type=int)
def create_enemy(name, cr):
    name= name.lower()
    click.echo(type(name))
    enemy_list[name] = Enemy(name, str(cr))

@cli.command()
@click.option('--name', '-n', required=True, type=str)
@click.option('--count', '-c', type=int, default=1)
def add_enemy(name, count):
    name= name.lower()
    active_encounter.add_enemies(count, enemy_list.get(name))


@cli.command()
@click.option('--name', '-n', type=str, required=True)
def select_encounter(name):
    name= name.lower()
    global active_encounter
    global encounter_list
    tmp_encounter = encounter_list.get(name)
    if tmp_encounter is not None:
        active_encounter =  tmp_encounter
        click.echo("Active encounter set to {}".format(name))
    else:
        click.echo("Encounter named {} not found".format(name))

@cli.command()
def calc_all():
    global encounter_list
    encounter_string = 'All current encounters:\n'
    for _, en in encounter_list.items():
        en.xp_calc()
        encounter_string += str(en)
    click.echo(encounter_string)


@cli.command()
@click.argument('enemy_json', type=click.File('r'))
def load_enemies(enemy_json):
    global enemy_list
    enemy_list = json.loads(enemy_json.read())

@cli.command()
@click.argument('path', type=click.File('w'))
def save_enemies(path):
    global enemy_list
    path.write(json.dumps(enemy_list))


register_repl(cli)

if __name__ == "__main__":
    cli()