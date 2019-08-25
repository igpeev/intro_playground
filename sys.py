# To know what’s in your current PMSP (Python Module Search Path)
import sys
for path in sys.path:
    print(path)

# Add another search location (used for imports)
sys.path.append('some_new_folder')

