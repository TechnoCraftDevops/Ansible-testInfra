# Run ansible CLI

## ping all hosts
ansible all -m ping

## check one playbook for one hosts
ansible-playbook [playbook_file].yml --check --limit [host-name/host-groupe]

## run one playbook for all hosts
ansible-playbook [playbook_file].yml

## run one playbook for one hosts
ansible-playbook docker_install.yml --check --limit [host-name/host-groupe]  

# Install testinfra
## require
-- pip install pytest-testinfra

-- ansible [core 2.12.7]

-- Python 3.10.4

-- pytest-7.1.2

# Run ansible tests
## run specific test
py.test --hosts=docker-host --connection=ansible --ansible-inventory=test_inventories/ --force-ansible tests/[file].py
## run all tests
py.test --hosts=docker-host --connection=ansible --ansible-inventory=test_inventories/ --force-ansible tests/*