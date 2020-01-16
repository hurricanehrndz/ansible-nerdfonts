Ansible role: nerdfonts
=========

[![Build Status][travis-badge]][travis-link]
[![Galaxy Role][role-badge]][galaxy-link]
[![MIT licensed][mit-badge]][mit-link]

Ansible role for [NerdFonts][nerdfonts] ([on GitHub][nf-git]) installation.

Requirements
------------

One of the following OS (or deriviatives):

- Debian | Ubuntu

NOTE:

- Role requires Fact Gathering by ansible!

Role Variables
--------------

| Variable              | Description                             | Default                                      |
|-----------------------|-----------------------------------------|----------------------------------------------|
| **nerdfonts_fonts[]** | List of nerdfonts to be installed       | see [`defaults/main.yml`](defaults/main.yml) |
| **nerdfonts_mono**    | Install mono font variation             | `no`                                         |
| **nerdfonts_users[]** | List of users nerdfonts to be installed | see [`defaults/main.yml`](defaults/main.yml) |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    nerdfonts_users: [ testuser ]
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

Carlos Hernandez | [e-mail](mailto:hurricanehrndz@techbyte.ca)

[role-badge]: https://img.shields.io/ansible/role/d/45889?style=for-the-badge
[galaxy-link]: https://galaxy.ansible.com/hurricanehrndz/nerdfonts/
[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge
[mit-link]: https://raw.githubusercontent.com/hurricanehrndz/ansible-nerdfonts/master/LICENSE
[homebrew]: http://brew.sh/
[nerdfonts]: https://nerdfonts.com/
[nf-git]: https://github.com/ryanoasis/nerd-fonts
[travis-badge]: https://img.shields.io/travis/hurricanehrndz/ansible-nerdfonts/master.svg?style=for-the-badge&logo=travis
[travis-link]: https://travis-ci.org/hurricanehrndz/ansible-nerdfonts
