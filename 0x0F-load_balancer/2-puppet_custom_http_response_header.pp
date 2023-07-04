# Using puppet to install and configure an nginx server

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

        location = / {
            return 200 'Hello World!';
        }
    }",
}

file { '/etc/nginx/nginx.conf':
  ensure      => present,
  environment => ["hostname=$(hostname)"],
  content     => "
    http {
        add_header X-Served-By '$hostname';
    }",
}

service { 'nginx':
  ensure    => 'running',
  enable    => 'true',
  hasstatus => 'true',
}
