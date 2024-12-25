# code_generator/generator.py
from jinja2 import Template
import os

def generate_class_code(class_name, init_params, init_body):
    """Generate Python class code from template."""
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'python_class_template.py')
    
    with open(template_path, "r") as template_file:
        template = Template(template_file.read())
    
    # Generate the final code by substituting placeholders
    return template.render(class_name=class_name, init_params=init_params, init_body=init_body)

def write_code_to_file(file_name, code):
    """Write generated code to a file."""
    with open(file_name, "w") as code_file:
        code_file.write(code)
    print(f"Code generated in {file_name}")
