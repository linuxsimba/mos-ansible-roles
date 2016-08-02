# external_lma_vip

This role configures a external facing VIP connection for Stacklight.

> Note: This is only to be used in a testing environment. In a production
environment is it recommended to put a management station on the Mgmt network.

## Requirements

* Ansible 2.x
* Stacklight 0.9+
* MOS8+

## Role Variables

These variables are defined in
[defaults/main.yml](https://github.com/linuxsimba/mos-ansible-roles/blob/master/external_lma_vip/defaults/main.yml)

## Inventory Variables

Define a host group called `lma`. This is used by the ansible delegation script
to obtain the VIP used by Nagios and the `br_mgmt` interface from each
Stacklight/LMA node.

Example Inventory File:

```
[controller]
control1 ansible_host=10.1.1.1
control2 ansible_host=10.1.1.2
control3 ansible_host=10.1.1.3

[lma]
lma1 ansible_host=10.1.1.4
lma2 ansible_host=10.1.1.5
lma3 ansible_host=10.1.1.6
```

## Example

```
ansible -i ansible.hosts -m external_lma_vip controller
```
