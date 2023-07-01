# Set up client SSH configuration in order to connect without password

file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => '
      Host *
        PasswordAuthentication no
        IdentityFile ~/.ssh/school',
}
