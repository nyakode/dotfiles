""" Configuracion de VIM Editor
""" Author: Fernando Castillo
""" User: <ferncastillov@outlook.com>

set number              " show line numbers
set wrap                " wrap lines
set encoding=utf-8      " set encoding to UTF-8 (default was "latin1")
set mouse=a             " enable mouse support (might not work well on Mac OS X)
set wildmenu            " visual autocomplete for command menu
set lazyredraw          " redraw screen only when we need to
set showmatch           " highlight matching parentheses / brackets [{()}]
set laststatus=2        " always show statusline (even with only single window)
set ruler               " show line and column number of the cursor on right side of statusline
set visualbell          " blink cursor on error, instead of beeping
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd	
set cursorline
set showmatch
set tabstop=3
set expandtab
set shiftwidth=3
set softtabstop=3
set relativenumber
set noshowmode
set autoindent
set undofile
set undodir=~/.vim/undodir


call plug#begin('~/.vim/plugged')

""" THEMES
Plug 'morhetz/gruvbox' " Tema de Gruvbox
Plug 'rafi/awesome-vim-colorschemes'
Plug 'severin-lemaignan/vim-minimap'
Plug 'lilydjwg/colorizer'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'ryanoasis/vim-devicons'

""" IDE
Plug 'easymotion/vim-easymotion'
Plug 'preservim/nerdtree'
Plug 'ervandew/supertab'
Plug 'christoomey/vim-tmux-navigator'
Plug 'valloric/youcompleteme'
Plug 'vim-python/python-syntax'
Plug 'honza/vim-snippets'
Plug 'tomtom/tcomment_vim'
Plug 'tpope/vim-markdown'
Plug 'kablamo/vim-git-log'
Plug 'gregsexton/gitv'


call plug#end()

"" Configuracion de apariencia
set t_Co=256
set background=dark
colorscheme minimalist
let base16colorspace=256
let g:gruvbox_contrast_dark="hard"

let g:spacegray_underline_search = 1
let g:spacegray_italicize_comments = 1

" Vim-Airline Configuration
let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
let g:airline_theme='minimalist'
let g:hybrid_custom_term_colors = 1
let g:hybrid_reduced_contrast = 1

"" Creacion de accesos directos
let mapleader = ' ' " configuramos un espacio como tecla de inicio para accesos directos
nmap <Leader>s <Plug>(easymotion-s2)
nmap <leader>nt :NERDTreeFind<CR>

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>

