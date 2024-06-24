from file_system import FileSystem

class GameLogic:
    def __init__(self):
        self.fs = FileSystem()  # Initialize the file system
        self.command_keywords = ['ls', 'cd', 'mkdir', 'touch', 'cat', 'rm', 'help']  # List of valid commands

    def handle_command(self, command):
        """
        Handle the user command and execute the appropriate file system operation.
        """
        parts = command.split()  # Split the command into parts
        
        if not parts:
            return "No command entered."  # Return error message if no command entered
        
        cmd = parts[0]  # Get the command keyword
        if cmd == 'help':
            return "Available commands: ls, cd, mkdir, touch, cat, rm, etc."  # Return help message
        elif cmd == 'ls':
            return self.fs.list_directory()  # List directory contents
        elif cmd == 'cd':
            if len(parts) > 1:
                return self.fs.change_directory(parts[1])  # Change directory
            else:
                return "Usage: cd <directory>"  # Return usage message if no directory specified
        elif cmd == 'mkdir':
            if len(parts) > 1:
                return self.fs.make_directory(parts[1])  # Make new directory
            else:
                return "Usage: mkdir <directory>"  # Return usage message if no directory name specified
        elif cmd == 'touch':
            if len(parts) > 1:
                return self.fs.create_file(parts[1])  # Create new file
            else:
                return "Usage: touch <filename>"  # Return usage message if no filename specified
        elif cmd == 'cat':
            if len(parts) > 1:
                return self.fs.read_file(parts[1])  # Read file contents
            else:
                return "Usage: cat <filename>"  # Return usage message if no filename specified
        elif cmd == 'rm':
            if len(parts) > 1:
                return self.fs.remove_file(parts[1])  # Remove file
            else:
                return "Usage: rm <filename>"  # Return usage message if no filename specified
        else:
            return "Command not recognized."  # Return error message if command is not recognized
