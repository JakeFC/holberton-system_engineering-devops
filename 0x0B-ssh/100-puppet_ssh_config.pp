service { 'ssh':
	ensure => running
}

augeas { 'ssh web01':
       context => '~/.ssh/config',
       changes => [
       	       'set PasswordAuthentication no',
	       'set HostName 54.221.48.50',
	       'set User ubuntu',
	       'set StrictHostKeyChecking no',
	       'set IdentifyFile -/.ssh/holberton'
	       ]
}