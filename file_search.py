import os

def search_files(dir_path, query):
    print(f"Searching for '{query}' in {dir_path}")
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if query in file:
                print(f"\033[92mFound {file} in {root}\033[0m")

dir_path = input("Enter path to directory: ")
query = input("Enter name of file you're looking for: ")
search_files(dir_path, query)
