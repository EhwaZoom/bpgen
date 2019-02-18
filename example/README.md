## BPGen example

Assume, you have entities, repositories and entities mappings to a database in your project.

Directory hierarchy like that:
```
├───Data
│   ├───Mappings
│   │       UserMapping.cs
│   │
│   └───Repositories
│       └───UserRepository
│               IUserRepository.cs
│               UserRepository.cs
│
└───Domain
    └───Entities
            User.cs
```

You want to add a new entity — `Organization`. There is some common part between `User` and `Organization` files. The difference is in detail implementation for each entity. So, you want to generalize it and create the necessary structure of any entity using one command. Follow the next steps to achieve this.

1. Create module using `bpgen create-module entity`
2. Create a template for each file in the module:
```console
bpgen create-template --module entity mapping 
bpgen create-template --module entity irepository
bpgen create-template --module entity repository
bpgen create-template --module entity entity
```

You will get this directory hierarchy after these steps:
```
├───bpgen_modules
│   └───entity
│       └───templates
│           ├───entity
│           │       config.json
│           │       template.bpt
│           │
│           ├───irepository
│           │       config.json
│           │       template.bpt
│           │
│           ├───mapping
│           │       config.json
│           │       template.bpt
│           │
│           └───repository
│                   config.json
│                   template.bpt
│
├───Data
│   ├───Mappings
│   │       UserMapping.cs
│   │
│   └───Repositories
│       └───UserRepository
│               IUserRepository.cs
│               UserRepository.cs
│
└───Domain
    └───Entities
            User.cs
```

3. Set up a configuration file and fill content to a template file for each template. You need to change `path_to_generated_file` setting in the configuration file at least.

Consider the `irepository` template. Set the `path_to_generated_file` setting in the `bpgen_modules/entity/templates/irepository/config.json` file equal to `Data/Repositories/${entity_name}Repository/I${entity_name}.cs`. Put an actual `IRepository.cs` content inside the `bpgen_modules/entity/templates/irepository/template.bpt` file with replaced concrete values by their parameter names. There is the only parameter in this case — `entity_name` for example:

```
using System;
using System.Threading.Tasks;
using foo.Domain.Entities;

namespace foo.Data.Repositories {
    public interface I${entity_name}Repository : INHibernateRepository<${entity_name}, Guid> { }
}
```


4. You are ready to use `generate-module`, which will generate desired files for a new entity: `bpgen generate-module entity -p entity_name=Organization -p table_name=organizations`.

Result:
```
├───bpgen_modules
│   └───entity
│       └───templates
│           ├───entity
│           │       config.json
│           │       template.bpt
│           │
│           ├───irepository
│           │       config.json
│           │       template.bpt
│           │
│           ├───mapping
│           │       config.json
│           │       template.bpt
│           │
│           └───repository
│                   config.json
│                   template.bpt
│
├───Data
│   ├───Mappings
│   │       OrganizationMapping.cs
│   │       UserMapping.cs
│   │
│   └───Repositories
│       ├───OrganizationRepository
│       │       IOrganizationRepository.cs
│       │       OrganizationRepository.cs
│       │
│       └───UserRepository
│               IUserRepository.cs
│               UserRepository.cs
│
└───Domain
    └───Entities
            Organization.cs
            User.cs
```