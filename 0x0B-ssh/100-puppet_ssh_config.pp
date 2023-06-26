# Set up client SSH configuration in order to connect without password

file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => '
      Host *
        PasswordAuthentication no

      Host 34.207.189.167
        IdentityFile ~/.ssh/school',
}
