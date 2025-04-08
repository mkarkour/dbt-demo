# DBT-Core with DuckDB Demo Project

This repository contains a demonstration project showcasing how to use dbt-core with DuckDB for data transformation. The project is structured to help beginners understand dbt concepts and workflows while following industry best practices.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Project Setup](#project-setup)
  - [Processing Data with DuckDB](#processing-data-with-duckdb)
  - [Running Models](#running-models)
  - [Documentation](#documentation)
- [Project Context](#project-context)
- [Best Practices](#best-practices)
- [Resources](#resources)

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Installation

1. **Install dbt-core with DuckDB adapter**:

   ```bash
   pip install dbt-core dbt-duckdb
   ```

2. **Verify installation**:

   ```bash
   dbt --version
   ```

   The output should display the installed version of dbt-core and the dbt-duckdb adapter.

### Project Setup

1. **Clone this repository**:

   ```bash
   git clone https://github.com/MehdiKarkour/dbt-duckdb-demo.git
   cd dbt-duckdb-demo
   ```

2. **Configure your profiles.yml**:

   The project already contains a profiles.yml file configured for DuckDB:

   ```yaml
   demo:
     outputs:
       dev:
         type: duckdb
         path: dev.duckdb
         threads: 1
       prod:
         type: duckdb
         path: prod.duckdb
         threads: 4
     target: dev
   ```

   This configuration creates a DuckDB database file named `dev.duckdb` for your development environment.

3. **Test your connection**:

   ```bash
   dbt debug
   ```

   This command verifies that dbt can connect to DuckDB correctly.

### Processing Data with DuckDB

1. **Load sample data**:

   The project includes a Python script to load sample data:

   ```bash
   python scripts/fetch_data.py
   ```

   This script will create a DuckDB database and load the sample data from the CSV file.

2. **Explore the data**:

   You can connect to the DuckDB database using the DuckDB CLI or another SQL client:

   ```bash
   duckdb dev.duckdb
   ```

   Then run SQL queries:

   ```sql
   SELECT * FROM sales LIMIT 10;
   ```

### Running Models

1. **Execute a specific model**:

   ```bash
   dbt run --select model_name
   ```

   For example, to run the intermediate sales model:

   ```bash
   dbt run --select int_sales
   ```

2. **Execute all models**:

   ```bash
   dbt run
   ```

3. **Test models**:

   ```bash
   dbt test
   ```

4. **Build models (run + test)**:

   ```bash
   dbt build
   ```

5. **View model results** (requires dbt v1.7+):

   ```bash
   dbt show --select model_name
   ```

### Documentation

1. **Generate documentation**:

   ```bash
   dbt docs generate
   ```

2. **Serve documentation locally**:

   ```bash
   dbt docs serve
   ```

   This will open a web browser showing the documentation for your dbt project, including:
   - Model lineage graphs
   - Table and column descriptions
   - Source data definitions
   - Test coverage

## 🎯 Project Context

This demonstration project is designed to provide a comprehensive introduction to dbt (data build tool) with DuckDB as the processing engine. DuckDB is an in-process SQL OLAP database management system, making it ideal for local development and testing of dbt workflows.

The primary goals of this project are:

1. **Education**: To help data professionals understand the basic concepts and workflows of dbt without needing to set up complex data warehouse infrastructure.

2. **Demonstration**: To showcase how to structure a dbt project following industry best practices, including proper organization of models, tests, documentation, and source definitions.

3. **Quick Start**: To provide a ready-to-use environment where users can experiment with dbt features and capabilities immediately.

4. **Best Practices**: To demonstrate recommended patterns for data modeling, testing, and documentation within the dbt ecosystem.

This project includes example models that transform source data through staging, intermediate, and consumption layers, demonstrating a typical analytics engineering workflow. Users can extend these examples to understand how dbt can address specific data transformation needs.

## ✅ Best Practices

This project demonstrates several dbt best practices:

### Project Structure

- **Layered approach**: Models are organized in a multi-layered architecture:
  - `staging`: Contains models that clean and standardize source data
  - `intermediate`: Contains business logic transformations
  - `consumption`: Contains final models for business consumption

### Source Configuration

- **External sources**: Properly defined source tables using the sources.yml file
- **Documentation**: Source tables include descriptions for better understanding

### Model Organization

- **Materialization strategy**: Appropriate materialization strategies are set at the project level and can be overridden at the model level
- **Naming conventions**: Consistent naming conventions across the project (e.g., `int_` prefix for intermediate models)

### Testing

- **Data tests**: Implementation of uniqueness and not-null tests for key columns
- **Schema tests**: Validation of model schema integrity

### Version Control

- **Git integration**: Project structure designed for version control
- **.gitignore**: Properly configured to exclude build artifacts and local environment files

### Documentation

- **Model documentation**: Descriptive comments and documentation for models
- **Column descriptions**: Detailed column descriptions for improved understanding

## 📓 Resources

### Official Documentation

- [dbt Documentation](https://docs.getdbt.com/docs/introduction)
- [DuckDB Documentation](https://duckdb.org/docs/)
- [dbt-duckdb Adapter](https://github.com/jwills/dbt-duckdb)

### Learning Materials

- [dbt Learn](https://courses.getdbt.com/)
- [dbt Slack Community](https://community.getdbt.com/)
- [dbt Discourse Forum](https://discourse.getdbt.com/)
- [DuckDB Guides](https://duckdb.org/docs/guides/index)

### Blog Posts and Tutorials

- [Modern Data Stack with dbt and DuckDB](https://duckdb.org/2022/10/12/modern-data-stack-in-a-box.html)
- [Getting Started with dbt Core](https://docs.getdbt.com/docs/core/installation)
- [Analytics Engineering with dbt](https://blog.getdbt.com/what-is-analytics-engineering/)

### Books

- [The Analytics Engineer's Guide to dbt](https://www.getdbt.com/resources/analytics-engineering-guide/)

### Videos

- [dbt YouTube Channel](https://www.youtube.com/c/getdbt)
- [DuckDB Conference Presentations](https://duckdb.org/news/)

### Tools and Extensions

- [dbt Power User VSCode Extension](https://marketplace.visualstudio.com/items?itemName=innoverio.vscode-dbt-power-user)
- [dbt-utils Package](https://github.com/dbt-labs/dbt-utils)

For further assistance or questions about this demo project, please open an issue in the GitHub repository.