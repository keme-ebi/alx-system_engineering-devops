# Using puppet to install and configure an nginx server instead of bash

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm;

        server_name _;
        location /redirect_me {
            return 301 https://youtube.com/;
        }
    }",
  notify => Service['nginx'],
}
