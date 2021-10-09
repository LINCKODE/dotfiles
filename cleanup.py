import os

print("WARNING: This will remove all the zsh files, oh my zsh and the vimrc!")

consent = input("If you really wish to do this type >consent<: ")

if consent == "consent":
    print("Removing files...")
    os.system("cd .. && rm -rdfv .zshfiles .zsh_history .zshrc .vimrc .oh-my-zsh/ && cd -")
    print("Done.")

    install = input("Do you wish to install the dotfiles? >yes<? ")
    if install == "yes":
        os.system("python3 install.py")

    exit()
else:
    print("Exiting...")
