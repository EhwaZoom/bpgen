import os
import json

from bpgen.path import (
    get_path_to_module,
    get_path_to_template,
    get_path_to_template_config,
    get_path_to_template_file
)
from bpgen.utils import print_and_exit


def handle(arguments):
    default_template_config = {
        'parameter_pattern': {
            'parameter_name': 'VAR',
            'pattern': '${VAR}'
        },
        'path_to_generated_file': ''
    }

    path_to_module = get_path_to_module(
        arguments.path_to_modules,
        arguments.module_name
    )
    path_to_template = get_path_to_template(
        path_to_module,
        arguments.template_name
    )
    path_to_template_config = get_path_to_template_config(path_to_template)
    path_to_template_file = get_path_to_template_file(path_to_template)

    if not os.path.exists(path_to_module):
        print_and_exit("Module is not found")

    os.makedirs(path_to_template, exist_ok=True)
    # Create an empty template file
    open(path_to_template_file, 'a').close()
    with open(path_to_template_config, 'w') as outfile:
        json.dump(
            default_template_config,
            outfile,
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
        )
    print("Template was successfully created", end='')
