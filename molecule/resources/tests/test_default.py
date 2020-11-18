import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("install_path", [
    "/home/testuser/.local/share/fonts/NerdFonts",
    "/usr/local/share/fonts/NerdFonts"
])
def test_nerdfonts_install(host, install_path):
    f = host.file(install_path)

    assert f.exists
    assert f.is_directory


@pytest.mark.parametrize(
    "prefix, fontname, user, home, expected",
    [
        ("/usr/", "AnonymousPro", "root", "/root", True),
        ("/usr/", "AnonymousProX", "root", "/root", False),
        ("/usr/", "SourceCodePro", "root", "/root", True),
        ("/usr/", "Mononoki", "root", "/root",  True),
        (
            "/home/testuser/.",
            "AnonymousPro",
            "testuser",
            "/home/testuser",
            True
        ),
        (
            "/home/testuser/.",
            "AnonymousProX",
            "testuser",
            "/home/testuser",
            False
        ),
        (
            "/home/testuser/.",
            "SourceCodePro",
            "testuser",
            "/home/testuser",
            True
        ),
        ("/home/testuser/.", "Mononoki", "testuser", "/home/testuser", True)
    ]
)
def test_nerdfont_exist(host, prefix, fontname, user, home, expected):
    font_path = f"{prefix}local/share/fonts/NerdFonts/{fontname}"
    with host.sudo(user):
        command = f"HOME={home} fc-list"
        fonts = host.check_output(command)
        assert (font_path in fonts) == expected
