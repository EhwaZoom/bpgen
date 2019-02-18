import argparse
from typing import List


class Parameter:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value


def init_argparser():
    parser = argparse.ArgumentParser(description="Boilerplate code generator")
    subparsers = parser.add_subparsers(dest='command', help="Command help")
    init_create_module_subparser(subparsers)
    init_create_template_subparser(subparsers)
    init_generate_module_subparser(subparsers)
    return parser


def init_create_module_subparser(subparsers):
    create_module_parser = subparsers.add_parser(
        'create-module',
        help="Create module directory hierarchy"
    )
    create_module_parser.add_argument(
        'module_name',
        help="Module name"
    )
    create_module_parser.add_argument(
        '-o',
        '--output',
        default='bpgen_modules',
        help="Path to output directory"
    )


def init_create_template_subparser(subparsers):
    create_template_parser = subparsers.add_parser(
        'create-template',
        help="Create template files with default config"
    )
    create_template_parser.add_argument(
        'template_name',
        help="Template name"
    )
    create_template_parser.add_argument(
        '--module',
        dest='module_name',
        required=True,
        help="Module name"
    )
    create_template_parser.add_argument(
        '-m',
        '--modules',
        dest='path_to_modules',
        default='bpgen_modules',
        help="Path to directory with modules"
    )


def init_generate_module_subparser(subparsers):
    generate_module_parser = subparsers.add_parser(
        'generate-module',
        help="Generate module files based on their templates"
    )
    generate_module_parser.add_argument(
        'module_name',
        help="Module name"
    )
    generate_module_parser.add_argument(
        '-m',
        '--modules',
        dest='path_to_modules',
        default='bpgen_modules',
        help="Path to directory with modules"
    )
    generate_module_parser.add_argument(
        '-p',
        '--parameters',
        action='append',
        help="Set parameters for templates"
    )


def parse_parameter(parameter: str) -> Parameter:
    parameter_name, parameter_value = parameter.split('=')
    return Parameter(name=parameter_name, value=parameter_value)


def parse_parameters(parameters: List[str]) -> List[Parameter]:
    parsed_parameters = []
    for parameter in parameters:
        parsed_parameter = parse_parameter(parameter)
        parsed_parameters.append(parsed_parameter)
    return parsed_parameters
