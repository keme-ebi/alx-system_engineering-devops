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
            error_page 404 /404.html;
            return 200 'Hello World!';
        }
    }",
  notify  => Service['nginx'],
}

exec { 'add_header':
  provider => shell,
  command  => 'sudo sed -i "/http {/a \\\tadd_header X-Served-By \"$hostname\";" /etc/nginx/nginx.conf'
}

exec { 'restart':
  provider => shell,
  command  => 'sudo service restart',
  after    => Exec['add_header'],
}
