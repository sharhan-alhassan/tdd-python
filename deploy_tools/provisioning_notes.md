Provisioning a new site
=======================
## Required packages:
* nginx
* python3
* virtualenv + pip
* Git

eg, on Ubuntu:
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get install nginx git python3 python3-venv

## Nginx Virtual Host config
* see nginx.template.conf
* replace SITENAME with, e.g., tdd-staging

## Systemd service
* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., tdd-staging

## Folder structure:
Assume we have a user account at /home/username
```python
/home/username
└── sites
    └── SITENAME
        ├── database
        ├── tdd-python
        ├── static  **
        └── virtualenv
```