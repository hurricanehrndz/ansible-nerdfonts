Ansible role: nerdfonts
=========

[![Build Status][travis-badge]][travis-link]
[![Galaxy Role][role-badge]][galaxy-link]
[![MIT licensed][mit-badge]][mit-link]

Cross-platform ansible role for [NerdFonts][nerdfonts] ([on GitHub][nf-git]) installation.

Requirements
------------

One of the following OS (or deriviatives):

- Debian | Ubuntu
- MacOS (with [Homebrew][homebrew])

NOTE:

- Role requires Fact Gathering by ansible!
- On MacOS only user-specific installation from Homebrew is available

For MacOS:
if Homebrew is not installed on the managed host, install the following role via
galaxy:

```sh
ansible-galaxy install drew-kun.homebrew
```

And include it in the playbook:

```yaml
    roles:
        - drew-kun.homebrew
```

Role Variables
--------------

OS-Agnostic:

| Variable              | Description                       | Default                                      |
|-----------------------|-----------------------------------|----------------------------------------------|
| **nerdfonts_fonts[]** | List of nerdfonts to be installed | see [`defaults/main.yml`](defaults/main.yml) |
| **nerdfonts_mono**    | Install mono font variation       | `no`                                         |

Debian-Specific:

| Variable              | Description                             | Default                                      |
|-----------------------|-----------------------------------------|----------------------------------------------|
| **nerdfonts_users[]** | List of users nerdfonts to be installed | see [`defaults/main.yml`](defaults/main.yml) |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    nerdfonts_users: [ root, testuser ]
  tasks:
    - name: Add testuser
      user:
        name: testuser
        shell: /bin/bash

    - name: Install nerdfonts
      include_role:
        name: ansible-nerdfonts
```

License
-------

[MIT][mit-link]

Author Information
------------------

Andrew Shagayev | [e-mail](mailto:drewshg@gmail.com)

[role-badge]: https://img.shields.io/badge/role-drew--kun.nerdfonts-green.svg
[galaxy-link]: https://galaxy.ansible.com/hurricanehrndz/nerdfonts/
[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge
[mit-link]: https://raw.githubusercontent.com/hurricanehrndz/ansible-nerdfonts/master/LICENSE
[homebrew]: http://brew.sh/
[nerdfonts]: https://nerdfonts.com/
[nf-git]: https://github.com/ryanoasis/nerd-fonts
[travis-badge]: https://img.shields.io/travis/hurricanehrndz/ansible-nerdfonts/master.svg?style=for-the-badge&logo=travis
[travis-link]: https://travis-ci.org/hurricanehrndz/ansible-nerdfonts
