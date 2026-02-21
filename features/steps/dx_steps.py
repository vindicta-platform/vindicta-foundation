from pathlib import Path
from behave import given, when, then


@given("the project dependencies are locked")
def step_dependencies_locked(context):
    # Basic pre-condition asserting we are in the right repo
    assert Path("pyproject.toml").exists(), "Must be run from the repository root"


@when("I inspect the pyproject.toml configuration")
def step_inspect_pyproject(context):
    with open("pyproject.toml", "r") as f:
        context.pyproject_content = f.read()


@then('the "dev" dependencies should include "{package}"')
def step_check_dev_dependency(context, package):
    # Simple un-parsed text check since it's sufficient for verifying it's in the list
    assert (
        f'"{package}"' in context.pyproject_content
        or f'"{package}>=' in context.pyproject_content
    ), f"Expected to find {package} in pyproject.toml"


@given("the Justfile exists")
def step_justfile_exists(context):
    assert Path("Justfile").exists(), "Justfile not found"


@when("I locate the test execution command")
def step_locate_test_cmd(context):
    with open("Justfile", "r") as f:
        context.justfile = f.read()


@then('it should be configured to run pytest with "{flag}"')
def step_pytest_flag(context, flag):
    test_lines = [line for line in context.justfile.splitlines() if "pytest" in line]
    assert test_lines, "Could not find a pytest command in the Justfile"
    assert any(flag in line for line in test_lines), (
        f"Expected pytest to run with {flag}, found commands: {test_lines}"
    )
