import os

def create_project_structure(base_path):
    structure = {
        "data": ["raw", "processed"],
        "notebooks": [],
        "src": ["__init__.py", "data_processing.py", "model_training.py", "batch_prediction.py"],
        "tests": ["unit", "integration"],
        "models": [],
        "monitoring": [],
        "docker": ["Dockerfile", "docker-compose.yaml"],
        "scripts": ["run_project.sh"],
    }

    # Create base directory
    os.makedirs(base_path, exist_ok=True)

    # Create structure
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        for file_or_subfolder in files:
            if "." in file_or_subfolder:  # If it contains a dot, it is a file
                open(os.path.join(folder_path, file_or_subfolder), 'a').close()
            else:  # Otherwise, it is a subfolder
                os.makedirs(os.path.join(folder_path, file_or_subfolder), exist_ok=True)

    # Create root-level files
    root_files = ["Makefile", "requirements.txt", "README.md", ".gitignore", "config.yaml"]
    for root_file in root_files:
        open(os.path.join(base_path, root_file), 'a').close()

# Define the project name
project_name = "ZOOCAMP_Mike_regration"

# Create the structure
create_project_structure(project_name)

print(f"Project structure for '{project_name}' has been created.")
