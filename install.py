import os


def cleanup():
    print("Performing cleanup...")
    os.system("rm -rfvd ohmzsh/ && rm -rfvd zsh-syntax-hightlighting/ && rm -rfvd Vundle.vim")


os.system("echo Setting up dotfiles...")

cleanup()

os.system("echo Cloning Oh my zsh...")
os.system("git clone https://github.com/ohmyzsh/ohmyzsh.git")
os.system("mv ohmyzsh .oh-my-zsh")
os.system("mv .oh-my-zsh ~/")
os.system("echo Oh my zsh done.")

os.system("cp -r .zshrc ~/")
os.system("echo zshrc done.")

os.system("echo Cloning Zsh syntax highlighting...")
os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git")
os.system("mv zsh-syntax-highlighting .zshfiles")
os.system("echo Zsh syntax highlighting done.")

os.system("cp -r .zshfiles ~/")
os.system("echo zshfiles done.")

os.system("mkdir .vim")
os.system("echo Cloning Vundle...")
os.system("git clone https://github.com/VundleVim/Vundle.vim.git")
os.system("mv Vundle.vim .vim/bundle/Vundle.vim")
os.system("cp -r .vim ~/")
os.system("cp -r .vimrc ~/")
os.system("echo Vim done.")

cleanup()

os.system("echo Done! You can start zsh now.")
