#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import yaml
import os
import glob

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_files():
    yaml_file = yaml.load(open('values.yaml'))
    cur_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)

    promenade_files = glob.glob("template/*")
    if not os.path.exists('output'):
        os.makedirs('output')

    for f in promenade_files:
        new_name = f.replace("template", "output")
        with open(new_name, 'w') as cur_file:
            cur_file.write(cur_env.get_template(f).render(
        types=yaml_file['types'], genesis=yaml_file['genesis'], script=yaml_file['script'], docker=yaml_file['docker'],
        node_keys=sorted(yaml_file['nodes'].keys()),nodes=sorted(yaml_file['nodes'].items())))


if __name__ == '__main__':
    generate_files()

