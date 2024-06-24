# Simulated file system
file_system = {
    "home": {
        "user": {
            "documents": {
                "notes.txt": "These are your notes."
            },
            "downloads": {},
        }
    }
}

current_path = ["home", "user"]

def handle_command(command):
    global current_path
    parts = command.split()
    
    if parts[0] == 'help':
        return "Available commands: ls, cd, mkdir, touch, cat, rm, etc."
    elif parts[0] == 'ls':
        return list_directory()
    elif parts[0] == 'cd':
        if len(parts) > 1:
            return change_directory(parts[1])
        else:
            return "Usage: cd <directory>"
    elif parts[0] == 'mkdir':
        if len(parts) > 1:
            return make_directory(parts[1])
        else:
            return "Usage: mkdir <directory>"
    elif parts[0] == 'touch':
        if len(parts) > 1:
            return create_file(parts[1])
        else:
            return "Usage: touch <filename>"
    elif parts[0] == 'cat':
        if len(parts) > 1:
            return read_file(parts[1])
        else:
            return "Usage: cat <filename>"
    elif parts[0] == 'rm':
        if len(parts) > 1:
            return remove_file(parts[1])
        else:
            return "Usage: rm <filename>"
    else:
        return "Command not recognized."

def list_directory():
    dir_content = file_system
    for part in current_path:
        dir_content = dir_content.get(part, {})
    return "\n".join(dir_content.keys())

def change_directory(directory):
    global current_path
    if directory == "..":
        if len(current_path) > 1:
            current_path.pop()
        return "Changed to " + "/".join(current_path)
    else:
        dir_content = file_system
        for part in current_path:
            dir_content = dir_content.get(part, {})
        if directory in dir_content:
            current_path.append(directory)
            return "Changed to " + "/".join(current_path)
        else:
            return "Directory not found."

def make_directory(directory):
    dir_content = file_system
    for part in current_path:
        dir_content = dir_content.get(part, {})
    if directory not in dir_content:
        dir_content[directory] = {}
        return f"Directory '{directory}' created."
    else:
        return "Directory already exists."

def create_file(filename):
    dir_content = file_system
    for part in current_path:
        dir_content = dir_content.get(part, {})
    if filename not in dir_content:
        dir_content[filename] = ""
        return f"File '{filename}' created."
    else:
        return "File already exists."

def read_file(filename):
    dir_content = file_system
    for part in current_path:
        dir_content = dir_content.get(part, {})
    if filename in dir_content:
        return dir_content[filename]
    else:
        return "File not found."

def remove_file(filename):
    dir_content = file_system
    for part in current_path:
        dir_content = dir_content.get(part, {})
    if filename in dir_content:
        del dir_content[filename]
        return f"File '{filename}' removed."
    else:
        return "File not found."
