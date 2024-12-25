"""CLI Package.
"""

from enum import Enum

import typer
from typing_extensions import Annotated

from flowbow.generator import generate_class_code, write_code_to_file

cli = typer.Typer()

class CodeType(Enum):
    class_ = "class"
    flask_ = "flask"

@cli.command()
def main(
    class_name: str,
    type: Annotated[CodeType, typer.Argument(help="Type of code to generate")] = None,
    init_params: Annotated[str, typer.Argument(help="Constructor parameters (comma separated)")] = "",
    init_body: Annotated[str, typer.Argument(help="Constructor body (Python code)")] = "",
):
    """CLI Code Generator"""
    if type == "class":
        class_code = generate_class_code(class_name, init_params, init_body)
        file_name = f"{class_name}.py"
        write_code_to_file(file_name, class_code)

if __name__ == "__main__":
    cli()
