# lbaas_v2

This role configures LBAAS v2 in a MOS environment. In Mirantis Openstack 8.0
it appears that neutron server is not under the control of pacemaker.
This role creates a lbaas v2 agent on each controller. It was originally
created for integration with AVI networks Load balancer.

## Requirements

* Ansible 2.x
* MOS8+

## Role Variables

These variables are defined in
[defaults/main.yml](https://github.com/linuxsimba/mos-ansible-roles/blob/master/lbaas_v2/defaults/main.yml)

Requires `service_plugins` /etc/neutron/neutron.conf variable to be configured.
See examples in the role's `defaults/main.yml` for more details.

## Inventory Variables

Requires a groups['controller'] host group. This is currently created
statically. Dynamic creation using the fuel2 node list -f json output is coming
soon.

## TODO
* Add Horizon Lbaas v2 dashboard support

## Example

```
ansible -i ansible.hosts -m lbaas_v2 controller
```
