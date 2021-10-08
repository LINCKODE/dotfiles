import os

os.system("echo Starting to move zsh dotfiles...")

os.system("cp -r .oh-my-zsh ~/")
os.system("echo Oh my zsh done.")

os.system("cp -r .zshrc ~/")
os.system("echo zshrc done.")

os.system("cp -r .zshfiles ~/")
os.system("echo zshfiles done.")

os.system("echo Done! You can start zsh now.")
