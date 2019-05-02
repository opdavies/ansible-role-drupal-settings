import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_drupal_site_directory_exists(host):
    directory = host.file('/var/www/test/sites/default')

    assert directory.exists
    assert directory.is_directory
