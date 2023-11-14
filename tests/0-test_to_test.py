import testinfra

def test_os_release(host):
    assert host.file("/etc/os-release").contains("Ubuntu")

def test_sshd_inactive(host):
    assert host.service("sshd").is_running is False

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644