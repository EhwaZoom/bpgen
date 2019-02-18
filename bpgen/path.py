import os


def get_path_to_module(path_to_modules, module_name):
    return os.path.join(
        path_to_modules,
        module_name
    )


def get_path_to_templates(path_to_module):
    return os.path.join(
        path_to_module,
        'templates'
    )


def get_path_to_template(path_to_module, template_name):
    return os.path.join(
        path_to_module,
        'templates',
        template_name
    )


def get_path_to_template_config(path_to_template):
    return os.path.join(
        path_to_template,
        'config.json'
    )


def get_path_to_template_file(path_to_template):
    return os.path.join(
        path_to_template,
        'template.bpt'
    )
