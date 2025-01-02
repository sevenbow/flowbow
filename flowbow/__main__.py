# Monkey-patch jinja to allow variables to not exist, which happens with sub-options
import jinja2

jinja2.StrictUndefined = jinja2.Undefined


# Monkey-patch cookiecutter to allow sub-items
from cookiecutter import prompt

from flowbow.monkey_patch import prompt_for_config

prompt.prompt_for_config = prompt_for_config


# monkey-patch context to point to flowbow.json
from cookiecutter import generate

from flowbow.monkey_patch import generate_context_wrapper

generate.generate_context = generate_context_wrapper

# for use in tests need monkey-patched api main
from cookiecutter import cli
from cookiecutter import main as api_main  # noqa: F401 referenced by tests


def default_flowbow_main(f):
    """Set the default for the cookiecutter template argument to the FlowBow template."""

    def _main(*args, **kwargs):
        f.params[1].default = (
            "https://github.com/sevenbow/flowbow"
        )
        return f(*args, **kwargs)

    return _main


main = default_flowbow_main(cli.main)


if __name__ == "__main__":
    main()
