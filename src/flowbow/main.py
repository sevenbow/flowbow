#!/usr/bin/env python3
"""Entrypoint.

Usage example:

```bash
# Use --help to see all options
python main.py --help
```
"""

import typer

cli = typer.Typer()

@cli.command()
def template():
    return "Hello World"

if __name__=="__main__":
    cli()
