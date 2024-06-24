class FileSystem:
    def __init__(self):
        # Initialize the simulated file system with a nested dictionary structure
        self.file_system = {
            "home": {
                "user": {
                    "documents": {
                        "notes.txt": "These are your notes."
                    },
                    "downloads": {},
                }
            }
        }
        self.current_path = ["home", "user"]  # Set the initial current path

    def list_directory(self):
        """
        List the contents of the current directory.
        """
        dir_content = self.file_system
        for part in self.current_path:
            dir_content = dir_content.get(part, {})  # Traverse the current path
        return "\n".join(dir_content.keys())  # Return the keys (directory contents) as a newline-separated string

    def change_directory(self, directory):
        """
        Change the current directory.
        """
        if directory == "..":  # Handle going up one directory
            if len(self.current_path) > 1:
                self.current_path.pop()  # Remove the last directory in the path
            return "Changed to " + "/".join(self.current_path)
        else:
            dir_content = self.file_system
            for part in self.current_path:
                dir_content = dir_content.get(part, {})  # Traverse the current path
            if directory in dir_content:  # Check if the directory exists
                self.current_path.append(directory)  # Add the directory to the current path
                return "Changed to " + "/".join(self.current_path)
            else:
                return "Directory not found."

    def make_directory(self, directory):
        """
        Create a new directory in the current directory.
        """
        dir_content = self.file_system
        for part in self.current_path:
            dir_content = dir_content.get(part, {})  # Traverse the current path
        if directory not in dir_content:  # Check if the directory does not already exist
            dir_content[directory] = {}  # Create the new directory
            return f"Directory '{directory}' created."
        else:
            return "Directory already exists."

    def create_file(self, filename):
        """
        Create a new file in the current directory.
        """
        dir_content = self.file_system
        for part in self.current_path:
            dir_content = dir_content.get(part, {})  # Traverse the current path
        if filename not in dir_content:  # Check if the file does not already exist
            dir_content[filename] = ""  # Create the new file
            return f"File '{filename}' created."
        else:
            return "File already exists."

    def read_file(self, filename):
        """
        Read the contents of a file.
        """
        dir_content = self.file_system
        for part in self.current_path:
            dir_content = dir_content.get(part, {})  # Traverse the current path
        if filename in dir_content:  # Check if the file exists
            return dir_content[filename]  # Return the file contents
        else:
            return "File not found."

    def remove_file(self, filename):
        """
        Remove a file from the current directory.
        """
        dir_content = self.file_system
        for part in self.current_path:
            dir_content = dir_content.get(part, {})  # Traverse the current path
        if filename in dir_content:  # Check if the file exists
            del dir_content[filename]  # Delete the file
            return f"File '{filename}' removed."
        else:
            return "File not found."
