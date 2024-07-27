import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Copy and sort files by extension from source to destination directory.")

    # Argument for the source directory path
    parser.add_argument('source', type=str, help='Path to the source directory')
    
    # Argument for the destination directory path (optional, default is 'dist')
    parser.add_argument('destination', type=str, nargs='?', default='dist', help='Path to the destination directory (default: dist)')
    
    return parser.parse_args()