# Changes client SSH config file to be able to connect w/o a password

file { "/etc/ssh/ssh_config":
    ensure  => 'present',
    content => 'PasswordAuthentication no\nIdentityFile -/.ssh/holberton'
}

#file_line { 'Remove pass auth':
#    ensure => 'present',
#    path   => '/etc/ssh/ssh_config',
#    line   => 'PasswordAuthentication no',
#}
#file_line { 'Set key file':
#    ensure => 'present',
#    path   => '/etc/ssh/ssh_config',
#    line   => 'IdentityFile -/.ssh/holberton',
#}