# a puppet script that fixes bad `phpp` extensions to `php`
# in the WordPress file `wp-settings.php`.

exec { 'replace-line':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
