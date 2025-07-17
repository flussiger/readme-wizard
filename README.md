This README was generated using README Wizard 1.0.

# README Wizard ![Version 1.0](https://img.shields.io/badge/Version-1.0-brightgreen)

## Project Description
README Wizard is a web-based tool that automatically generates professional README.md files for software projects. Users can input their project details through an intuitive web interface, and the application uses AI to create comprehensive, well-structured README files with proper formatting, sections, and best practices. The tool streamlines the documentation process for developers and saves time while ensuring consistent, high-quality project documentation.

## Technology Stack
- Python
- FastAPI
- HTML
- CSS
- JavaScript
- OpenAI API
- Pydantic

## Target Audience
The target audience includes software developers, open-source contributors, students, and anyone who needs to create professional documentation for their coding projects.

## Usage Steps
1. Clone the repository to your local machine
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your OpenAI API key in a `.env` file
4a. Run the FastAPI server: `uvicorn backend.main:app --reload`.
5. Open your browser and navigate to the local server (127.0.0.1:8000)
6. Fill out the form with your project details
7. Click "Generate README" to create your professional documentation
8. Copy the generated README content to your project

4b.  Alternatively you can run it trough CLI using the wizard.py file. 
    Example Usage: "cd cli; python wizard.py -d "A cool web app" -s "Python, Flask" -a "Developers" -n "MyApp" -v "1.0.0" -u "pip install && python app.py" -r "John Doe" -t "https://youtube.com/watch?v=demo""
    You would now get a finished readme in the readme.md file.

## Author
- Author: flussiger

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your/repository.git
    cd README-Wizard
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Features
- Automatically generates professional README.md files
- Intuitive web interface for inputting project details
- Utilizes AI for creating well-structured documentation
- Saves time and ensures consistent, high-quality project documentation

## Troubleshooting
If you encounter any issues or have questions, please reach out to the author, flussiger.

---
