import os

print("WARNING: This will remove all the zsh files, oh my zsh and the vimrc!")

consent = input("If you really wish to do this type >consent< : ")

if consent is "constent":
    print("Removing files...")
    os.system("rm -rdfv .zshfiles .zsh_history .zshrc .vimrc .oh-my-zsh/")
    print("Done.")
    exit()
else:
    print("Exiting...")
