import os
def is_binary(file_path):
    """
    Checks if the given file is binary.
    """
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
    try:
        with open(file_path, 'rb') as file:
            return is_binary_string(file.read(1024))
    except Exception as e:
        print(f"Error checking if file is binary: {e}")
        return True  # Assuming binary if there's an error reading the file

def read_file_content(file_path):
    """
    Read the content of a file, handling binary files differently.
    """
    return os.path.basename(file_path)  # return filename for binary files