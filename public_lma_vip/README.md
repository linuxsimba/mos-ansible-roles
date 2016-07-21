# Public Stacklight VIP

This role configures a external facing VIP connection for Stacklight.

> Note: This is only to be used in a testing environment. In a production
environment is it recommended to put a management station on the Mgmt network.

## Requirements

* Ansible 2.x
* Stacklight 0.9+
* MOS8+

## Role Variables

These variables are defined in defaults/main.yml (provide link)

## Dependencies

* lma_vip_local: Gets the VIP IP address
