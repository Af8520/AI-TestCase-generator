# AI Test Case Generator

## Overview
AI Test Case Generator is an intelligent tool designed to automatically generate test cases for software applications. Using GPT-powered natural language processing, this tool takes in feature descriptions or user inputs and generates a variety of test cases, helping QA engineers automate and streamline their testing efforts. The generated test cases include various types such as functional, GUI, negative, and boundary tests.

## Features
- **Automated Test Case Generation**: Automatically generates test cases based on input functionality.
- **Predefined and Custom Scenarios**: Users can input specific functionalities, and the AI will generate test cases covering multiple scenarios.
- **Natural Language Processing (NLP)**: Leverages OpenAI’s GPT models to understand and interpret feature requirements written in natural language.
- **Exportable Test Cases**: Test cases are generated in a structured format, which can be exported for use in test automation suites.
- **Support for Multiple Test Types**: Functional, GUI, boundary, and negative test cases are supported.
  
## Pre-Conditions
1. **API Key for OpenAI**: 
   - To use the GPT-powered test case generation, you need an API key from OpenAI. You can obtain the API key from [OpenAI's API page](https://platform.openai.com/signup).
   - Once you have the API key, add it as an environment variable:
     
      API_KEY = "api-key by OpenAI"
     

## Technologies Involved
- **Python**: The core language used to build the AI Test Case Generator.
- **OpenAI GPT API**: Provides natural language processing capabilities to interpret and generate test cases based on user inputs.
- **Streamlit**: A framework used for building the web interface, allowing users to interact with the test case generator in a user-friendly manner.
- **Pandas**: Utilized for handling data structures and exporting test cases in various formats (CSV, Excel, etc.).
- **Git**: Version control for managing the project codebase.


## Example
If the input functionality is "Login to the app," the AI Test Case Generator will create test cases like:

| Test Case ID | Steps                                                         | Expected Results                             | Type of Test |
|--------------|---------------------------------------------------------------|----------------------------------------------|--------------|
| TC01         | Enter valid username and password and click 'Login'           | User is successfully logged in               | Functional   |
| TC02         | Enter invalid username and password and click 'Login'         | Error message is displayed                   | Negative     |
| TC03         | Leave username and password fields empty and click 'Login'    | Error message prompts user to enter credentials | GUI          |



