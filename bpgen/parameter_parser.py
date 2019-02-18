import re
from typing import List

from bpgen.config import Config


class Parameter:
    def __init__(self, name: str, formatted_name: str, value: str = None):
        self.name = name
        self.formatted_name = formatted_name
        self.value = value


def parse_parameters(string: str, config: Config) -> List[Parameter]:
    """Find all used parameters in the string using regex."""
    pattern_begin, pattern_end = config.parameter_pattern.pattern.split(
        config.parameter_pattern.parameter_name
    )
    regex_pattern_begin = re.escape(pattern_begin)
    regex_pattern_end = re.escape(pattern_end)
    regex = '{}.+?{}'.format(regex_pattern_begin, regex_pattern_end)

    found_formatted_params = re.findall(regex, string)
    parameter_objs = []
    for formatted_parameter in found_formatted_params:
        # Getting a clear parameter name
        name = formatted_parameter.replace(pattern_begin, '')
        name = name.replace(pattern_end, '')

        parameter_obj = Parameter(
            name=name,
            formatted_name=formatted_parameter
        )
        parameter_objs.append(parameter_obj)

    return parameter_objs
