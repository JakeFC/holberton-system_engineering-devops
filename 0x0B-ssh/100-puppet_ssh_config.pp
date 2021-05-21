# Changes client SSH config file to be able to connect w/o a password
service { 'ssh':
	ensure => running
}

augeas { 'ssh config':
       context => '/etc/ssh/ssh_config',
       changes => [
       	       'set PasswordAuthentication no',
	       'set HostName 54.221.48.50',
	       'set User ubuntu',
	       'set IdentityFile -/.ssh/holberton'
	       ]
}