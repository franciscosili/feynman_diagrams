#! /usr/bin/python3

import latexutils
import argparse
import os

def replace_template(template, replacements):
    for key, value in replacements.items():
        template = template.replace(f'{key}', str(value))
    return template


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tag', help='Diagram tag')
args = parser.parse_args()

output_dir = f'./{args.tag}'

if not os.path.exists(output_dir): os.makedirs(output_dir)



with open(f'templates/feynman_diagram_TEMPLATE.tex', 'r') as f:
    template_lines = f.read()

diagram_filename = 'feynman_diagram'

with open(f'{output_dir}/{diagram_filename}.tex', 'w') as f:
    replaced_text = replace_template(template_lines, {'TEMPLATE': '', 'NAME': args.tag})
    f.write(replaced_text)

latexutils.create_latex_doc(f'{output_dir}/{diagram_filename}.tex', f'{output_dir}/{args.tag}.tex')
os.system(f'rm {output_dir}/{diagram_filename}.txt')