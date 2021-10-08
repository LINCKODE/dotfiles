# Path to your oh-my-zsh installation.
export ZSH="/home/linckode/.oh-my-zsh"

#ZSH_THEME="agnoster"
#ZSH_THEME="gnzh"
ZSH_THEME="strug"

plugins=(
	git
	adb
	archlinux
	catimg
	command-not-found
	dotenv
	fancy-ctrl-z
	git-prompt
	mvn
	nmap
	sudo
	systemd
	themes
	zsh_reload
)

source $ZSH/oh-my-zsh.sh


# Enable colors and change prompt:
autoload -U colors && colors
#PS1="%B%{$fg[red]%}[%{$fg[yellow]%}%n%{$fg[green]%}@%{$fg[blue]%}%M %{$fg[magenta]%}%~%{$fg[red]%}]%{$reset_color%}$%b "

if [[ 'false' == 'true' ]]; then
	
	session=$(python ~/.zshfiles/sessionSelector.py)

	if [[ $TERM_PROGRAM == 'tmux' ]]; then
		alias neo="neofetch | lolcat"
		alias quit="tmux detach"
		#alias exit="quit"
	else
		if [[ $( tmux list-sessions ) == '' ]]; then
			~/.zshfiles/tmux.sh
			tmux attach-session -t $session
			exit
		else
			tmux attach-session -t $session
			exit
		fi
	fi
fi

HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zshfiles/histfile

# Use lf to switch directories and bind it to ctrl-o
lfcd () {
    tmp="$(mktemp)"
    lf -last-dir-path="$tmp" "$@"
    if [ -f "$tmp" ]; then
        dir="$(cat "$tmp")"
        rm -f "$tmp"
        [ -d "$dir" ] && [ "$dir" != "$(pwd)" ] && cd "$dir"
    fi
}
bindkey -s '^o' 'lfcd\n'
source /home/linckode/.zshfiles/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

