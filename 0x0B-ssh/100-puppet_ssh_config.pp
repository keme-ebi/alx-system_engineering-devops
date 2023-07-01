# Set up client SSH configuration in order to connect without password

file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => '
      Host *
        PasswordAuthentication no

      Host 100.25.140.168
        IdentityFile ~/.ssh/school',
}
