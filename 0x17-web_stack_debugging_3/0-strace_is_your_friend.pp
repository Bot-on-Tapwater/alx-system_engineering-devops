file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => file('/var/www/html/wp-settings.php'),
  replace => true,
}

exec { 'fix-wp-settings-php':
  command     => 'sed -i "s/\/class-wp.phpp/\/class-wp.php/g" /var/www/html/wp-settings.php',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
