import shutil
from pathlib import Path
from parser import parse_arguments

def copy_files_by_extension(src_path: Path, dst_path: Path) -> None:
    if not src_path.exists():
        print(f"Source directory {src_path} does not exist.")
        return
    for item in src_path.iterdir():
        if item.is_dir():
            copy_files_by_extension(item, dst_path)
        else:
             # Create subdirectory for each file extension
            ext = item.suffix[1:]  # Get extension without the dot
            target_dir = dst_path / ext
            target_dir.mkdir(parents=True, exist_ok=True)

            # Copy the file to the corresponding subdirectory
            try:
                shutil.copy2(item, target_dir / item.name)
            except PermissionError as e:
                print(f"Permission error: {e}")
            except Exception as e:
                print(f"Error copying file {item}: {e}")


def main():
    # Get command line arguments
    args = parse_arguments()

    src_path = Path(args.source)
    dst_path = Path(args.destination)

    # Start copying files
    copy_files_by_extension(src_path, dst_path)

    # Display directory tree for source and destination directories
    print("Source directory structure:")
    display_tree(src_path)
    print("\nDestination directory structure:")
    display_tree(dst_path)

# ANSI escape codes for colored output
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"


def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        print(indent + prefix + COLOR_BLUE + path.name + COLOR_RESET)
        indent += "    " if prefix else ""
        # Get a sorted list of items, with directories first
        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
        for index, child in enumerate(children):
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + path.name)

if __name__ == "__main__":
    main()