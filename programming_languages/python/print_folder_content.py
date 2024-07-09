import os
import argparse

def should_exclude(folder_path, exclude_folders):
    for exclude_folder in exclude_folders:
        if exclude_folder in folder_path.split(os.path.sep):
            return True
    return False

def print_file_contents(folder_path, file_extensions=None, exclude_folders=None):
    if exclude_folders is None:
        # Default folders to exclude
        exclude_folders = [
            '.git',
            'node_modules',
            '__pycache__',
            'venv',
            'env',
            '.venv',
            '.env',
            'dist',
            'build',
            'logs',
            '.pytest_cache',
            '.mypy_cache',
            '.tox',
            '.eggs',
            '*.egg-info',
            '.virtualenvs',
            '.idea',
            '.vscode',
        ]

    if file_extensions is None:
        file_extensions = []  # If no extensions are specified, all files will be processed

    # Walk through the directory tree
    for root, dirs, files in os.walk(folder_path):
        # Modify dirs in-place to exclude specified folders and their nested folders
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d), exclude_folders)]

        for file_name in files:
            # Check if the file has one of the specified extensions (if any)
            if not file_extensions or any(file_name.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file_name)
                
                # Check if the current item is a file
                if os.path.isfile(file_path):
                    try:
                        # Open the file in read mode with utf-8 encoding
                        with open(file_path, 'r', encoding='utf-8') as file:
                            # Read the file content
                            content = file.read()
                            
                            # Print the file path and content
                            print(f"File: {file_path}")
                            print(content + "\n")
                    except UnicodeDecodeError:
                        try:
                            # Retry with a different encoding (e.g., 'latin-1')
                            with open(file_path, 'r', encoding='latin-1') as file:
                                # Read the file content
                                content = file.read()
                                
                                # Print the file path and content
                                print(f"File: {file_path}")
                                print(content + "\n")
                        except IOError as e:
                            print(f"Error reading file: {file_path}")
                            print(f"Error details: {str(e)}\n")
                    except IOError as e:
                        print(f"Error reading file: {file_path}")
                        print(f"Error details: {str(e)}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print contents of files in a folder.")
    parser.add_argument("folder_path", nargs="?", help="Path to the folder to process")
    parser.add_argument("-f", "--filter", nargs="*", help="File extensions to include (e.g., .py .txt)")
    parser.add_argument("-e", "--exclude", nargs="*", default=[], help="Folders to exclude")
    
    args = parser.parse_args()

    folder_path = args.folder_path or input("Enter the folder path: ")
    
    file_extensions = args.filter
    if file_extensions:
        file_extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in file_extensions]
    
    # Combine default exclude folders with user provided ones
    exclude_folders = set([
        '.git',
        'node_modules',
        '__pycache__',
        'venv',
        'env',
        '.venv',
        '.env',
        'dist',
        'build',
        'logs',
        '.pytest_cache',
        '.mypy_cache',
        '.tox',
        '.eggs',
        '*.egg-info',
        '.virtualenvs',
        '.idea',
        '.vscode',
    ])
    exclude_folders.update(args.exclude)
    
    print_file_contents(folder_path, file_extensions=file_extensions, exclude_folders=list(exclude_folders))
