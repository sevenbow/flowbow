"""CLI Package."""

from enum import Enum

import typer
from typing_extensions import Annotated

from flowbow.generator import generate_class_code

cli = typer.Typer()


class CodeType(Enum):
    class_ = "class"
    flask_ = "flask"


@cli.command()
def main(
    template_name: str = "no-artifact-no-flows",
    output_dir: str = "./",
    type: Annotated[
        CodeType, typer.Argument(help="Type of code to generate")
    ] = None,
    init_params: Annotated[
        str, typer.Argument(help="Constructor parameters (comma separated)")
    ] = "",
    init_body: Annotated[
        str, typer.Argument(help="Constructor body (Python code)")
    ] = "",
):
    """CLI Code Generator"""

    generate_class_code(template_name=template_name, output_dir=output_dir)


if __name__ == "__main__":
    cli()
