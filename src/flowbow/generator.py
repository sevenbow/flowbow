"""Generator module"""

from pathlib import Path

from jinja2 import Template


def generate_class_code(template_name: str, output_dir: str):
    """Generate Python class code from template."""
    template_dir = Path(__file__).parent / "templates" / template_name

    for filepath in template_dir.rglob("*"):
        if filepath.is_file():
            # Read template
            with open(filepath, "r") as template_file:
                template = Template(template_file.read())

            # Generate the final code by substituting placeholders
            rendered_template = template.render()

            # Write rendered template to a file
            output_path = Path(output_dir) / filepath.relative_to(template_dir)
            output_path.parent.mkdir(exist_ok=True, parents=True)
            with open(output_path, "w") as code_file:
                code_file.write(rendered_template)
            print(f"Code generated in {output_path}")
