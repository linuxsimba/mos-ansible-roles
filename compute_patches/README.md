# compute_patches

Patches to apply to the MOS setup that are not included in the Maintenance Update. For now only supports MOS8 patches.



## Requirements:
* Ansible 2+
* MOS 8.0 

## Role Variables
None

## Example
```
---
- hosts: compute
  roles:
     - { role: compute_patches }
     
```
## Dependencies

It does not depend on any other ansible role


## License

MIT

## Author Information
Stanley Karunditu
