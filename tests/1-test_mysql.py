import testinfra

# def test_os_release(host):
#     assert host.file("/etc/os-release").contains("Ubuntu")

# def test_sshd_inactive(host):
#     assert host.service("sshd").is_running is False

def test_mysql_service_running(host):
    service = host.service('mysql')
    assert service.is_enabled
    assert service.is_running