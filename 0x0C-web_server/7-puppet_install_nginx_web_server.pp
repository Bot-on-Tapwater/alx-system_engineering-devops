# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Define the Nginx server block for the root
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html;
        
        location / {
            return 200 'Hello World!';
        }
        
        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
    }
  ",
}

# Create a symlink to enable the configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Remove the default Nginx configuration symlink
file { '/etc/nginx/sites-enabled/000-default':
  ensure => 'absent',
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
}
