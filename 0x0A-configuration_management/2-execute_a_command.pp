# Creates a manifest that kills a process named killmenow

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => 'usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
}
