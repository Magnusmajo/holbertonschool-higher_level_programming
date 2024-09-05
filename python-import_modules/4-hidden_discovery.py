import os
import hidden_4

#!/usr/bin/python3

if __name__ == "__main__":

    alles = dir(hidden_4)
    for name in alles:
        if name[:2] != "__":
            print(name)

# Change the permissions of the script
os.chmod("/tmp/4-hidden_discovery.py", 0o755)
