FILEPATH = "todos.txt"


def get_todos(filepath: str = FILEPATH) -> list[str]:
    """Read a text file and returns the list of
    to-do items."""

    with open(filepath, "r") as file_local:
        todos_local: list[str] = file_local.readlines()

    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list on the text file."""

    with open(filepath, "w") as file:
        file.writelines(todos_arg)
