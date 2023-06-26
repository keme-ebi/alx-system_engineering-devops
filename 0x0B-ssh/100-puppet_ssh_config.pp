# Set up client SSH configuration in order to connect without password

class { 'sshkeys::client':
    ensure                  => 'present'
    identity_file           => '~/.ssh/school',
    password_authentication => 'no',
}
