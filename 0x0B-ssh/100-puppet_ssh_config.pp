# Set up client SSH configuration in order to connect without password

file { '~/.ssh/config':
    ensure  => 'present'
    content => '
      # SSH client configuration
      Host 34.207.189.167
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    ',
}
