# Ansible Role: Drupal settings

```yaml
drupal_settings:
  - drupal_root: /var/www/web
    sites:
      - name: default
        filename: settings.php # Optional, defaults to 'settings.php'
        settings:
          base_url: https://www.example.com # Optional, Drupal 7
          databases:
            default: # The database key
              default: # The database target
                driver: mysql # Optional, defaults to 'mysql'
                host: localhost # Optional, defaults to 'localhost'
                database: mydatabase
                username: user
                password: secret
          trusted_hosts: # Optional, Drupal 8
            - '^example\.com$'
            - '^.+\.example\.com$'
            - '^example\.org$'
            - '^.+\.example\.org$'
```
