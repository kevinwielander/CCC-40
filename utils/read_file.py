def read_file_lines(file_path):
    """
    Reads a text file and returns its lines as a list.

    :param file_path: Path to the text file.
    :return: A list of lines from the file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]