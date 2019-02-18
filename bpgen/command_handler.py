from bpgen.commands.create_module import handle as handle_create_module
from bpgen.commands.create_template import handle as handle_create_template
from bpgen.commands.generate_module import handle as handle_generate_module
from bpgen.utils import print_and_exit


def handle(arguments):
    commands_methods = {
        'create-module': handle_create_module,
        'create-template': handle_create_template,
        'generate-module': handle_generate_module,
    }
    command_method = commands_methods.get(arguments.command)

    if not command_method:
    	print_and_exit("No command was provided")

    command_method(arguments)
