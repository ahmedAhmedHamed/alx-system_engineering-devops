# Fixing a typo in file includes.
# utilises sed to do so.

exec {'fix-typo':
  command => "/bin/sed -i /var/www/html/wp-settings.php -e 's/class-wp-locale.phpp/class-wp-locale.php/'"
}
