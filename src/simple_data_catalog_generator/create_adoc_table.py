def create_adoc_table(entries: list, num_cols: int) -> str:
    """
    Creates an AsciiDoc table string from a list of entries.

    Args:
        entries (list): A list of data entries to include in the table. An entry
            may itself be a list/tuple (e.g. a (label, value) pair); such
            nested entries are flattened into individual cells.
        num_cols (int): The desired number of columns in the table.

    Returns:
        str: An AsciiDoc table string. If the number of cells is not a
        multiple of num_cols, the trailing incomplete row is dropped (rather
        than the table being left malformed).
    """
    # Flatten nested list/tuple entries into individual cells so that a
    # (label, value) pair occupies two columns rather than one.
    flat = []
    for entry in entries:
        if isinstance(entry, (list, tuple)):
            flat.extend(entry)
        else:
            flat.append(entry)

    # Drop any trailing cells that do not form a complete row.
    if num_cols:
        flat = flat[: (len(flat) // num_cols) * num_cols]

    table_str = ""
    col_specs = "[cols=" + '"' + ",".join(["1"] * num_cols) + '"]\n'
    header = "|=== \n"

    table_str += col_specs + header

    for entry in flat:
        table_str = table_str + "a| " + str(entry) + "\n"  # a is to support lists

    table_str = table_str + "|=== \n\n"
    return table_str
