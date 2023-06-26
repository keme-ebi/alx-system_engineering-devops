# Set up client SSH configuration in order to connect without password

file { "/usr/bin":
    ensure  => present,
    content => "
      Host 34.207.189.167
        IdentityFile ~/.ssh/school
        PasswordAuthentication no",
}
