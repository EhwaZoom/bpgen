import os

from bpgen.path import get_path_to_templates, get_path_to_module
from bpgen.utils import print_and_exit


def handle(arguments):
    path_to_module = get_path_to_module(
        arguments.output,
        arguments.module_name
    )
    path_to_module_templates = get_path_to_templates(path_to_module)

    module_exists = os.path.exists(path_to_module)
    if module_exists:
        print_and_exit("Module already exists")

    os.makedirs(path_to_module_templates, exist_ok=True)
    print("Module was successfully created", end='')
