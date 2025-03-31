import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print("Deleting public directory...")
    # Change to the doc directory
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.makedirs("docs", exist_ok=True)

    # Use your copy_files_recursive function to copy static files to public
    copy_files_recursive("static", "docs")

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public,basepath)

main()
