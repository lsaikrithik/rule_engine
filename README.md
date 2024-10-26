# Rule Engine Application

## Overview

This is a 3-tier rule engine application developed using Flask, which allows users to create, combine, and evaluate conditional rules based on attributes such as age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent these rules dynamically.

## Design Choices

### Architecture

**3-Tier Architecture**: The application is structured into three distinct layers:

- **Presentation Layer**: The frontend uses HTML, CSS, and JavaScript (jQuery) for a simple user interface that interacts with the backend via API calls.
- **API Layer**: The Flask framework serves as the backend API, exposing endpoints for rule creation, combination, and evaluation. It handles user requests, processes data, and communicates with the database.
- **Data Layer**: MongoDB is used as the database to store rules, enabling persistence and retrieval. The choice of MongoDB allows flexibility in storing unstructured data.

### Rule Representation

- **Abstract Syntax Tree (AST)**: The rules are represented as AST nodes, which can be created, combined, and evaluated dynamically. This allows for complex logical expressions to be constructed and manipulated programmatically.
- **Node Class**: Each node in the AST is represented by an instance of the Node class, which contains attributes for type, left and right child nodes, and value.

### Rule Evaluation

- **Evaluation Logic**: The application evaluates rules based on the data provided by users. The evaluation logic handles simple comparisons (>, <, =) and logical operators (AND, OR) to determine eligibility based on the given criteria.

### User Interface

- **Dynamic Interaction**: The frontend provides a user-friendly interface for creating and evaluating rules, with JSON input fields for easy manipulation of data. Results are displayed dynamically on the page without refreshing.

## Dependencies

To run this application, you will need the following:

- **Docker**: Ensure Docker is installed and running on your machine.
- **Flask**: A lightweight WSGI web application framework.
- **Flask-PyMongo**: A Flask extension for working with MongoDB.
- **python-dotenv**: For loading environment variables from a .env file.
- **jQuery**: For handling AJAX requests in the frontend.

## Getting Started

### Prerequisites

1. Install Docker.

### Running the Application

#### Clone the Repository

```bash
git clone https://github.com/yourusername/rule_engine.git
cd rule_engine
```

### Build and Run with Docker
To build and run the application, execute the following command:

```bash
docker-compose build
docker-compose up
```

### Access the Application
Open your web browser and go to http://localhost:5000 to access the Rule Engine application.

### API Endpoints
POST /create_rule: Create a new rule using a JSON payload with {"rule_string": "your_rule"}.

POST /combine_rules: Combine multiple rules using a JSON payload with {"rules": ["rule1", "rule2"]}.

POST /evaluate_rule: Evaluate a rule against given data using a JSON payload with {"data": {"key": value}, "ast": {"type": "operator", "left": {...}, "right": {...}, "value": "AND"}}.

### Conclusion
This rule engine application demonstrates how to dynamically create and evaluate complex eligibility rules using a structured approach. The use of Docker allows for easy deployment and management of the application.
