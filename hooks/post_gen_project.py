import shutil
import subprocess
from pathlib import Path

# Use the selected documentation package specified in the config,
# or none if none selected
docs_path = Path("docs")
# {% if cookiecutter.docs != "none" %}
docs_subpath = docs_path / "{{ cookiecutter.docs }}"
for obj in docs_subpath.iterdir():
    shutil.move(str(obj), str(docs_path))
# {% endif %}

# Remove all remaining docs templates
for docs_template in docs_path.iterdir():
    if docs_template.is_dir() and not docs_template.name == "docs":
        shutil.rmtree(docs_template)

# Remove LICENSE if "No license file"
if "{{ cookiecutter.open_source_license }}" == "No license file":
    Path("LICENSE").unlink()

# Make single quotes prettier
# Jinja tojson escapes single-quotes with \u0027 since it's meant for HTML/JS
pyproject_text = Path("pyproject.toml").read_text()
Path("pyproject.toml").write_text(pyproject_text.replace(r"\u0027", "'"))

# Run the command to install the dependencies using uv
subprocess.run(["cd", "{{ cookiecutter.repo_name }}"])
subprocess.run(["uv", "venv", "--python", "{{ cookiecutter.python_version }}"])
subprocess.run(["source .venv/bin/activate"], shell=True)
subprocess.run(["uv add numpy polars scikit-learn loguru typer ipykernel pre-commit"], shell=True)
subprocess.run(["pre-commit install"], shell=True)
