return{
  "christoomey/vim-tmux-navigator",
  vim.keymap.set('n', 'C-h', ":TmuxNaviagteLeft<CR>"),
  vim.keymap.set('n', 'C-j', ":TmuxNaviagteDown<CR>"),
  vim.keymap.set('n', 'C-k', ":TmuxNaviagteUp<CR>"),
  vim.keymap.set('n', 'C-l', ":TmuxNaviagteRight<CR>")
}
