import os
from typing import List

from bpgen.path import (
    get_path_to_module,
    get_path_to_templates,
    get_path_to_template,
    get_path_to_template_config,
    get_path_to_template_file
)
from bpgen.argparser import (
    Parameter as ArgParameter,
    parse_parameter as parse_arg_parameter,
    parse_parameters as parse_arg_parameters
)
from bpgen.parameter_parser import Parameter, parse_parameters
from bpgen.config import Config, load_template_config
from bpgen.utils import print_and_exit


def generate_template(
    source: str,
    parameters: List[Parameter],
    config: Config
):
    """Generate a single template from the module."""
    path_to_generated_file = config.path_to_generated_file
    for parameter in parameters:
        source = source.replace(parameter.formatted_name, parameter.value)
        path_to_generated_file = path_to_generated_file.replace(
            parameter.formatted_name,
            parameter.value
        )

    try:
        os.makedirs(os.path.dirname(path_to_generated_file), exist_ok=True)
    except FileNotFoundError:
        print_and_exit("Incorrect path to generated file was specified")

    with open(path_to_generated_file, 'w') as f:
        f.write(source)


def concat_parameters(
    arg_parameters: List[ArgParameter],
    parameters: List[Parameter]
) -> List[Parameter]:
    """Transfer argument parameters values to parameter objects."""
    parameter_values = {}

    for arg_parameter in arg_parameters:
        parameter_values[arg_parameter.name] = arg_parameter.value

    for parameter in parameters:
        parameter.value = parameter_values[parameter.name]

    return parameters


def load_template_file(path_to_template: str) -> str:
    path_to_template_file = get_path_to_template_file(path_to_template)
    with open(path_to_template_file, 'r') as f:
        filedata = f.read()
    return filedata


def check_parameters_usage(
    paths_to_templates: List[str],
    parameters: List[ArgParameter]
) -> set:
    """
    Check if all parameters in templates are provided.
    Returns set of missing parameters.
    """
    missing_parameters = set()
    parameter_names = set([p.name for p in parameters])

    for path in paths_to_templates:
        config = load_template_config(path)
        filedata = load_template_file(path)
        parsed_template_parameters = parse_parameters(filedata, config)
        parsed_path_parameters = parse_parameters(
            config.path_to_generated_file,
            config
        )
        template_parameters_names = set(
            [p.name for p in parsed_template_parameters]
        )
        path_parameters_names = set(
            [p.name for p in parsed_path_parameters]
        )
        parsed_parameters_names = \
            template_parameters_names | path_parameters_names

        difference = parsed_parameters_names - parameter_names
        missing_parameters = missing_parameters | difference

    return missing_parameters


def handle(arguments):
    path_to_module = get_path_to_module(
        arguments.path_to_modules,
        arguments.module_name
    )
    path_to_templates = get_path_to_templates(path_to_module)

    if not os.path.exists(path_to_module):
        print_and_exit("No module was found")
    if not os.path.exists(path_to_templates):
        print_and_exit("No templates in the module were found")

    template_names = next(os.walk(path_to_templates))[1]
    paths_to_templates = []
    for template_name in template_names:
        paths_to_templates.append(
            get_path_to_template(path_to_module, template_name)
        )
    try:
        # Requires for desired behavior when no parameters provided
        arg_parameters_for_parse = \
            arguments.parameters if arguments.parameters else []
        arg_parameters = parse_arg_parameters(arg_parameters_for_parse)
    except ValueError:
        print_and_exit(
            "Incorrect syntax. Parameters should follow this syntax pattern: "
            "PARAMETER_NAME=PARAMETER_VALUE"
        )

    missing_parameters = check_parameters_usage(
        paths_to_templates,
        arg_parameters
    )
    if missing_parameters:
        print_and_exit(
            "You are not provided parameters which templates use: {}".format(
                ', '.join(missing_parameters)
            )
        )

    for path in paths_to_templates:
        config = load_template_config(path)
        filedata = load_template_file(path)
        parsed_parameters = parse_parameters(filedata, config)
        parameters = concat_parameters(arg_parameters, parsed_parameters)
        generate_template(filedata, parameters, config)

    print("Module was successfully generated", end='')
