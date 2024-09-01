import os
import glob

# Define the directory containing wallpapers and the index file
WALLPAPER_DIR = os.path.expanduser('~/Pictures/Wallpapers')
INDEX_FILE = os.path.expanduser('~/.current_wallpaper_index')

def get_next_index(wallpapers):
    # Read the current index from the file or default to 0 if the file doesn't exist
    if os.path.isfile(INDEX_FILE):
        with open(INDEX_FILE, 'r') as file:
            try:
                current_index = int(file.read().strip())
            except ValueError:
                current_index = 0
    else:
        current_index = 0
    
    # Get the count of wallpapers
    wallpaper_count = len(wallpapers)

    # Increment the index and wrap around if necessary
    next_index = (current_index + 1) % wallpaper_count

    # Save the new index to the file
    with open(INDEX_FILE, 'w') as file:
        file.write(str(next_index))
    
    return next_index

def set_wallpaper(index, wallpapers):
    # Get the path to the selected wallpaper
    wallpaper_path = wallpapers[index]

    # Set the wallpaper using swww
    os.system(f'swww img "{wallpaper_path}"')

    print(f"Wallpaper changed to {wallpaper_path}")

def main():
    # Get a list of all wallpaper files in the directory
    wallpapers = glob.glob(os.path.join(WALLPAPER_DIR, '*'))

    # Ensure there are wallpapers available
    if not wallpapers:
        print("No wallpapers found in the directory.")
        return

    # Get the next index and set the wallpaper
    index = get_next_index(wallpapers)
    set_wallpaper(index, wallpapers)

if __name__ == "__main__":
    main()

