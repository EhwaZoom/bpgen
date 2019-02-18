import json

from bpgen.path import get_path_to_template_config


class ParameterPattern:
    def __init__(self, parameter_name: str, pattern: str):
        self.parameter_name = parameter_name
        self.pattern = pattern


class Config:
    def __init__(
        self,
        path_to_generated_file: str,
        parameter_pattern: ParameterPattern
    ):
        self.path_to_generated_file = path_to_generated_file
        self.parameter_pattern = parameter_pattern


def load_template_config(path_to_template: str) -> Config:
    path_to_template_config = get_path_to_template_config(path_to_template)
    with open(path_to_template_config, 'r') as f:
        config = json.load(f)

    parameter_pattern = config.get('parameter_pattern')
    return Config(
        path_to_generated_file=config.get('path_to_generated_file'),
        parameter_pattern=ParameterPattern(
            parameter_name=parameter_pattern.get('parameter_name'),
            pattern=parameter_pattern.get('pattern')
        )
    )
