# PyPoo: Wastewater Treatment Modeling Framework

PyPoo is a modular, extensible framework for simulating wastewater treatment processes. The framework is designed to integrate various reaction models (e.g., ASM1, ADM1, ASM3, etc.) with unit operation modules that perform mass and energy balances. By using a modular repository structure and YAML-based configuration files, users can easily extend or modify the simulation components to suit their needs.

## Repository Structure

The project repository is organized as follows:

```text
Pypoo/
├── reaction_model/
│   ├── ASM1/
│   │   ├── __init__.py
│   │   └── ...         # ASM1 reaction model code, inflow/outflow calculations, etc.
│   ├── ADM1/
│   │   ├── __init__.py
│   │   └── ...         # ADM1 reaction model code, inflow/outflow calculations, etc.
│   └── (other reaction model modules)
├── unit_operation/
│   ├── activated_sludge/
│   │   ├── __init__.py
│   │   └── ...         # Unit operation models for activated sludge, energy and mass balance code, etc.
│   ├── aeration/
│   │   ├── __init__.py
│   │   └── ...         # Aeration model code and associated calculations
│   └── (other unit operation modules)
├── config/
│   ├── reaction_models/
│   │   └── ...         # YAML configuration files for reaction models
│   ├── unit_operations/
│   │   └── ...         # YAML configuration files for unit operations
│   ├── flowsheet/
│   │   └── ...         # YAML configuration files for the overall flowsheet
│   └── config_global.yml  # Global configuration settings
├── utils/
│   ├── __init__.py
│   └── ...             # Utility modules (e.g., numerical algorithms, helper functions, etc.)
├── environment.yml     # Conda environment file
├── main.py             # Entry point for running simulations
└── README.md           # This file
```

- **reaction_model/**: Contains modules for different reaction models. Each module includes the reaction kinetics and the associated inflow/outflow calculations for that model.
- **unit_operation/**: Contains modules for various unit operations (e.g., activated sludge, aeration tanks) that calculate material and energy balances based on the reaction model in use.
- **config/**: Holds configuration files in YAML format:
  - `reaction_models/`: Configuration files for the reaction models.
  - `unit_operations/`: Configuration files for the unit operation modules.
  - `flowsheet/`: Configuration for how unit operations are interconnected.
  - `config_global.yml`: Global configuration settings.
- **utils/**: Utility code for numerical methods and common helper functions.
- **environment.yml**: A Conda environment file that specifies all required dependencies.
- **main.py**: The main entry point to run a simulation.
- **README.md**: This file.

## Getting Started

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/) (Anaconda or Miniconda)

### Setup

1. **Clone the Repository**

   From your terminal:

   ```bash
   git clone <repository-url>
   cd Pypoo
   ```

2. **Create the Conda Environment**

   Use the provided YAML file to create the environment:

   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the Environment**

   ```bash
   conda activate pypoo-env
   ```

4. **Run Tests or Start a Simulation**

   To run tests:

   ```bash
   pytest
   ```

   Or run the main simulation:

   ```bash
   python main.py
   ```

## Usage (currently in development, could be modified in the future)

- **Configuration:**  
  Edit the YAML files under the `config/` directory to adjust model parameters, configure reaction models, unit operations, and define the overall flowsheet.

- **Extending the Framework:**  
  - To add a new reaction model, create a new module under `reaction_model/` following the provided template.  
  - To integrate a new unit operation, add its module under `unit_operation/` and update the corresponding YAML config file.

- **Utilities:**  
  Use the modules in `utils/` for numerical algorithms and helper functions required throughout the simulation.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository and create a new branch.
2. Make your changes and ensure all tests pass.
3. Submit a pull request with a description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [Younes AJEDDIG](mailto:younes.ajeddig@live.fr).

Happy modeling and simulation!
