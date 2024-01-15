import sys
import os

if __name__ == "__main__":
    name = ''
    with open('bin/config') as config_file:
        name = config_file.read().strip()

    if name: 
        os.chdir('code-challenge')
        os.system("git add .")
        os.system("git commit --allow-empty -m \"Final commit\"")
        os.system(f"git bundle create ../{name}.bundle HEAD {name}")
