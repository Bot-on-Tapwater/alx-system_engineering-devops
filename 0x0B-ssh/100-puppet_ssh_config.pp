# Ensure SSH client configuration file exists
file { '/home/botontapwater-System-Product-Name/.ssh/config':
  ensure => 'present',
  owner  => 'botontapwater-System-Product-Name',
  group  => 'botontapwater-System-Product-Name',
  mode   => '0600',
  content => "Host *\n    IdentityFile ~/.ssh/school\n    PreferredAuthentications publickey\n    PasswordAuthentication no\n",
}
