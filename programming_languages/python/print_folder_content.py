#!/usr/bin/env python3
# File: print_folder_content.py

"""
Script to print the contents of files in a specified folder and optionally remove files by name.

Usage:
    python print_folder_content.py [folder_path] [options]

Arguments:
    folder_path             Path to the folder to process (optional)

Options:
    -h, --help              Show this help message and exit
    -f, --filter            File extensions to include (e.g., .py .txt)
    -x, --exclude-extensions  File extensions to exclude (e.g., .log .tmp)
    -e, --exclude           Folders to exclude
    -n, --remove            File names to remove

Examples:
    python print_folder_content.py /path/to/folder
    python print_folder_content.py /path/to/folder -f .py .txt
    python print_folder_content.py /path/to/folder -x .log .tmp
    python print_folder_content.py /path/to/folder -f .py -x .log -e __pycache__ .git
    python print_folder_content.py /path/to/folder -n file1.txt file2.log

If no folder path is provided, the script will prompt for it during execution.
"""
#!/usr/bin/env python3
# File: print_folder_content.py

import os
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def should_exclude(folder_path, exclude_folders):
    return any(exclude_folder in folder_path.split(os.path.sep) for exclude_folder in exclude_folders)

def print_file_contents(folder_path, file_extensions=None, exclude_extensions=None, exclude_folders=None, exclude_files=None):
    if exclude_folders is None:
        exclude_folders = [
            '.git', 'node_modules', '__pycache__', 'venv', 'env', '.venv', '.env',
            'dist', 'build', 'logs', '.pytest_cache', '.mypy_cache', '.tox',
            '.eggs', '*.egg-info', '.virtualenvs', '.idea', '.vscode',
        ]

    file_extensions = file_extensions or []
    exclude_extensions = exclude_extensions or []
    exclude_files = exclude_files or []

    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d), exclude_folders)]

        for file_name in files:
            if file_name in exclude_files:
                continue  # Skip files that are in the exclude list

            if (not file_extensions or any(file_name.endswith(ext) for ext in file_extensions)) and \
               not any(file_name.endswith(ext) for ext in exclude_extensions):
                file_path = os.path.join(root, file_name)
                
                if os.path.isfile(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                            print(f"File: {file_path}")
                            print(content + "\n")
                    except UnicodeDecodeError:
                        try:
                            with open(file_path, 'r', encoding='latin-1') as file:
                                content = file.read()
                                print(f"File: {file_path}")
                                print(content + "\n")
                        except IOError as e:
                            logging.error(f"Error reading file: {file_path}")
                            logging.error(f"Error details: {str(e)}\n")
                    except IOError as e:
                        logging.error(f"Error reading file: {file_path}")
                        logging.error(f"Error details: {str(e)}\n")

def main():
    parser = argparse.ArgumentParser(description="Print contents of files in a folder, excluding specified files.")
    parser.add_argument("folder_path", nargs="?", help="Path to the folder to process")
    parser.add_argument("-f", "--filter", nargs="*", help="File extensions to include (e.g., .py .txt)")
    parser.add_argument("-x", "--exclude-extensions", nargs="*", help="File extensions to exclude (e.g., .log .tmp)")
    parser.add_argument("-e", "--exclude", nargs="*", default=[], help="Folders to exclude")
    parser.add_argument("-n", "--exclude-files", nargs="*", help="File names to exclude from printing")
    
    args = parser.parse_args()

    folder_path = args.folder_path or input("Enter the folder path: ")
    
    file_extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in (args.filter or [])]
    exclude_extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in (args.exclude_extensions or [])]
    
    exclude_folders = set([
        '.git', 'node_modules', '__pycache__', 'venv', 'env', '.venv', '.env',
        'dist', 'build', 'logs', '.pytest_cache', '.mypy_cache', '.tox',
        '.eggs', '*.egg-info', '.virtualenvs', '.idea', '.vscode',
    ])
    exclude_folders.update(args.exclude)
    
    print_file_contents(folder_path, 
                        file_extensions=file_extensions, 
                        exclude_extensions=exclude_extensions, 
                        exclude_folders=list(exclude_folders),
                        exclude_files=args.exclude_files)

if __name__ == "__main__":
    main()