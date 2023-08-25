exec { 'killmenow':
  command  => 'pkill killmenow',
  onlyif   => 'pgrep killmenow',
  provider => shell,
}
