# Architecture

## 1. Core

- **Role:**  
  - Provides the simulation engine and central management of configurations, data structures, and numerical solvers.
  - Orchestrates the simulation loop, managing the execution of reaction models and unit operations.
- **Interactions:**  
  - Loads settings from YAML configuration files (global settings, reaction models, unit operations, and flowsheet definitions).
  - Instantiates and coordinates the execution of the reaction models, unit operations, and flowsheet configuration.
  - Routes data between modules (e.g., state variables, parameters, and simulation outputs).

---

## 2. Reaction Models

- **Role:**  
  - Encapsulate the reaction kinetics and stoichiometry (e.g., ASM1, ADM1, ASM3, etc.).
  - Compute reaction rates and conversion terms based on current concentrations and process conditions.
  - Manage specific input/output calculations (for influent and effluent flows) associated with each reaction scheme.
- **Interactions:**  
  - Receive model-specific configurations and parameters from YAML files (stored in *config/reaction_models*).
  - Provide reaction rate outputs to unit operations for mass and energy balance calculations.
  - Are invoked by unit operations during each simulation step to update chemical transformations.

---

## 3. Unit Operations

- **Role:**  
  - Represent individual process units (e.g., aeration tanks, clarifiers, digesters) that perform mass and energy balances.
  - Integrate the reaction model calculations into overall process unit balances.
- **Interactions:**  
  - Use reaction model outputs to update state variables (material, energy, and flow balances) in each unit.
  - Obtain their configuration details from YAML files in *config/unit_operations*.
  - Feed their computed effluent conditions to the flowsheet configuration.

---

## 4. Flowsheet Configuration

- **Role:**  
  - Defines the overall process network by specifying how unit operations are interconnected.
  - Establishes the material and energy flow paths between different process units.
  - Acts as a blueprint for the simulation by linking the outputs of one unit as inputs for the next.
- **Interactions:**  
  - Loads its own configuration from YAML files (found in *config/flowsheet*).
  - Directs the core module on how to assemble the simulation by wiring unit operations together.
  - Enables data exchange between units, ensuring a coherent simulation of the entire treatment process.

---

## 5. Reporting

- **Role:**  
  - Collects simulation outputs such as time-series data, concentration profiles, flow rates, and energy consumption.
  - Provides visualization tools (graphs, tables, dashboards) and export functionalities (CSV, JSON, HTML).
  - Assists in calibration, debugging, and performance analysis.
- **Interactions:**  
  - Receives processed data from unit operations and the core simulation loop.
  - Uses utility functions (from the *utils* module) for post-processing and visualization.
  - May integrate with external tools or dashboards to present the simulation results.

---

### How They Work Together

1. **Initialization & Configuration:**  
   - The **Core** module reads YAML configurations for global settings, reaction models, unit operations, and the flowsheet.
   - It creates instances of reaction models and unit operations, then assembles them according to the **Flowsheet Configuration**.

2. **Simulation Execution:**  
   - **Unit Operations** call their associated **Reaction Models** to compute kinetic data.
   - The **Core** orchestrates the simulation loop, updating state variables and solving the overall mass and energy balances.
   - The **Flowsheet Configuration** ensures that the outputs (e.g., effluent conditions) from one unit are correctly passed as inputs to the next.

3. **Reporting & Analysis:**  
   - Simulation outputs are collected by the **Reporting** module, which utilizes shared utility functions for data processing.
   - Results are then visualized and exported for analysis, feedback, and potential calibration of the model.

---

This modular architecture—comprising the core engine, reaction models, unit operations, flowsheet configuration, and reporting—allows PyPoo to be highly flexible and extensible, enabling users to easily add, modify, or replace individual components while ensuring that they integrate seamlessly within the overall simulation environment.
