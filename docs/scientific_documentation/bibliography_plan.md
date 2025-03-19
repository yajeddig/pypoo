# Bibliography plan

## 1. Reaction Models in Wastewater Treatment

### a. Core Models and Their Variants

- **Activated Sludge Models (ASM):**
  - **ASM1:**  
    - Fundamentals, kinetics, and stoichiometry  
    - Limitations and assumptions
  - **ASM2 and ASM2d:**  
    - Differences between ASM2 and ASM2d (with dynamic mixing, for example)  
    - Enhanced representations of particulate and soluble matter  
  - **ASM3:**  
    - Improvements in biochemical kinetics and parameter sensitivity  
    - Application scenarios and calibration methods
- **Anaerobic Digestion Models:**
  - **ADM1 (Anaerobic Digestion Model No. 1):**  
    - Reaction kinetics and mass balances  
    - Gas-liquid transfer processes  
    - pH and ion chemistry in ADM1
- **Other Advanced Reaction Models:**  
  - Emerging or hybrid models (e.g., incorporating biofilm processes, extended nutrient cycles, etc.)  
  - Models for specialized substrates or treatment processes

### b. Model Calibration and Parameter Estimation

- Techniques for calibrating biochemical reaction models
- Sensitivity analysis and uncertainty quantification methods

### c. Literature & Standards

- Key textbooks, research articles, and technical reports (e.g., Henze et al.’s work on ASM, IWA guidelines)
- Review articles on the evolution of activated sludge and anaerobic digestion models

---

## 2. Unit Operations in Wastewater Treatment

### a. Types of Unit Operations

- **Biological Reactors:**
  - Aeration tanks (e.g., fixed-volume, variable-volume, biofilm reactors)
  - Activated sludge units (ASU) and associated models
  - Anaerobic digesters
- **Physical Operations:**
  - Clarifiers (primary, secondary)
  - Filters and sedimentation basins
  - Membrane bioreactors
- **Chemical/Physical-chemical Processes:**
  - Precipitation and dissolution processes (e.g., phosphorus removal)
  - Disinfection units

### b. Material and Energy Balances

- Methods for performing mass and energy balance calculations in each unit
- Integration of reaction model outputs with unit operation models

### c. Configuration and Control Strategies

- Control algorithms applied in unit operations (e.g., aeration control)
- Operational flexibility and dynamic behavior

### d. Literature & Standards

- Case studies on wastewater treatment plant (WWTP) design and operation  
- Research articles on the simulation of specific unit operations

---

## 3. Flowsheet Simulation and Solution Algorithms

### a. Flowsheet Configuration & Superstructure

- Approaches for representing complex process networks (e.g., flowsheet graphs, connectivity matrices)
- How to integrate unit operations to form a coherent system simulation

### b. Numerical Methods & Solvers

- **DAE (Differential-Algebraic Equation) Solvers:**  
  - Overview of common solvers and libraries (e.g., CVODE, Sundials, or Python-based solvers)  
  - Handling stiff systems and coupled mass balances
- **Modular & Sequential Simulation Techniques:**
  - Sequential modular approach vs. fully coupled solution strategies
  - Iterative schemes for converging unit interconnections
- **Optimization & Calibration Algorithms:**
  - Methods for process optimization (e.g., dynamic optimization, model predictive control)
  - Parameter estimation and calibration techniques

### c. Software Architecture Considerations

- Integration of YAML-based configuration for flowsheet, unit operations, and reaction models
- Data management and reporting pipelines for simulation outputs

### d. Literature & Standards

- Texts and articles on process systems engineering and flowsheet simulation (e.g., Aspen Plus, gPROMS)
- Recent research on numerical methods in environmental process simulation

---

## 4. Supporting Topics and Utilities

### a. Utilities and Helper Functions

- Data structures for time-series, state variables, and parameters
- Visualization and reporting tools (e.g., integration with pandas, matplotlib, etc.)
- Numerical utilities for pre-processing and post-processing simulation data

### b. Software Engineering and Best Practices

- Modular programming and repository structuring for scientific computing projects
- Configuration management and reproducibility in simulation studies

### c. Integration with External Tools

- Connection with external calibration tools, statistical packages, or machine learning frameworks
- Interfacing with standard formats for data exchange (e.g., JSON, YAML, CSV)

---

## Next Steps

1. **Literature Search:**  
   - Gather and review key papers and books on ASM models, ADM1, and other reaction models.
   - Search for state-of-the-art flowsheet simulation methodologies and numerical solvers used in process systems engineering.
2. **Bibliography Organization:**  
   - Create a reference manager library (using tools like Zotero or Mendeley) to keep track of sources.
   - Organize references by category: Reaction Models, Unit Operations, Flowsheet Algorithms, and Utilities.
3. **Gap Analysis:**  
   - Identify areas where literature is lacking or where models need further development.
   - Outline any potential modifications or extensions needed for your specific PyPoo framework.
4. **Document Findings:**  
   - Summarize the research in a living document or report that can be updated as new literature is found.
