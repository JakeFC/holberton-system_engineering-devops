# Changes client SSH config file to be able to connect w/o a password
file { '/etc/ssh/ssh_config':
       ensure => 'present',
       content => 'PasswordAuthentication no,
       	       	  IdentityFile -/.ssh/holberton'
}