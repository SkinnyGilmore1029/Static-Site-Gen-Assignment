import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    # Clean public directory
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.makedirs("public", exist_ok=True)

    # Use your copy_files_recursive function to copy static files to public
    copy_files_recursive("static", "public")

    # Generate the index page
    generate_page(
        "content/index.md",
        "template.html",
        "public/index.html"
    )

main()
