nerdfonts
=========

[![MIT licensed][mit-badge]
[![Galaxy Role][role-badge]][galaxy-link]

Cross-platform ansible role for NerdFonts installation.

Requirements
------------

One of the following OS (or deriviatives):
 - Debian | Ubuntu
 - MacOS (with ![Homebrew][homebrew])

Role Variables
--------------

OS-Agnostic:

    - nerdfonts_fonts:                      # list of nerdfonts to be installed
       - fontname:                          # name of nerdfont
         caskname:                          # name of nerdfont in homebrew cask (for MacOS)
         caskname_mono:                     # name of mono nerdfont in homebrew cask (for MacOS)

Debian-Specific:

    - nerdfonts_env: system | user/users    # install fonts system- or user-wide
    - nerdfonts_deb_fonts_sys_dir:          # system-wide fonts directory
    - nerdfonts_deb_fonts_user_dir:         # user-specific fonts directory
    - nerdfonts_users:                      # list of users nerdfonts to be installed

MacOS-Specific:

    - nerdfonts_mono: yes | no              # install mono font from homebrew cask

Dependencies
------------

For MacOS if ![Homebrew][homebrew] is not installed, depends on:
 - drew-kun.homebrew

Install via galaxy:

    ansible-galaxy install drew-kun.homebrew

Example Playbook
----------------

    - hosts: deb_clients
      roles:
         - drew-kun.nerdfonts

License
-------

MIT

Author Information
------------------

![Andrew Shagayev](drewshg@gmail.com)

[galaxy-link]: https://galaxy.ansible.com/drew-kun/nerdfonts/
[homebrew]: http://brew.sh/
[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[mit-link]: https://raw.githubusercontent.com/geerlingguy/ansible-role-homebrew/master/LICENSE
