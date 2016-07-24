# external_lma_vip

This role configures a external facing VIP connection for Stacklight.

> Note: This is only to be used in a testing environment. In a production
environment is it recommended to put a management station on the Mgmt network.

## Requirements

* Ansible 2.x
* Stacklight 0.9+
* MOS8+

## Role Variables

These variables are defined in defaults/main.yml (provide link)

## Inventory Variables

* define an ``openstack_mgmt_ip`` variable on each Stacklight/LMA host. This is the Openstack mgmt IP of the controller.
This IP is where the various LMA servers bind to on the LMA server


* Ensure that all stacklight controllers are placed in a ``[lma]`` group.

* Ensure that each inventory hostvar variables has the `ansible_hostname` and `ansible_host`

> TODO: Use local ansible facts to automatically generate this data. For now user
has to manual collect this data.

Example:

```
[lma]

lma1 ansible_host='10.1.1.1' ansible_hostname='node-22' openstack_mgmt_ip='192.168.1.1'
```
