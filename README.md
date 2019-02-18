# BPGen

BPGen — **b**oiler**p**late **gen**erator. It helps to rid of writing routine code for each module.

## How it works
BPGen operates with modules and templates. Modules and templates are just simple directory hierarchy. Each module has one or more templates. Each template has a configuration file and a template file. One template — one generated file. You can not generate a template itself. You **should** use a module for that.

Once you call `generate-module`, BPGen checks if all used parameters in templates are provided, then create a new file based on a template configuration file, a template file and themselves provided parameters. BPGen is looking for parameter names in the template file and replaces them with provided values. BPGen also applies it on `path_to_generated_file` setting in the template configuration file.

Example is [here](https://github.com/EhwaZoom/bpgen).

## Installation
1. Clone this repository
2. Execute `pip install . --user` in the repository


## Requirements
Tested on Python 3.5+