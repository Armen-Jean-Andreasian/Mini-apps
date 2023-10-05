class FileManager:
    """
    Creates a file based on given data, format and filename.
    """

    @staticmethod
    def make_file(format_: str, file_data: bytes, name: str):
        file_name = f"{name}.{format_}"

        with open(file_name, "wb") as file:
            file.write(file_data)