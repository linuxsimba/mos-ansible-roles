# lma_slack

Update Stacklight configuration on all LMA nodes to support
sending of key Stacklight metrics to Slack.

By default it sends the cluster status changes for each of the key service


## Requirements:
* Ansible 2+
* MOS 8.0 or 9.0
* Stacklight 0.9+

## Role Variables

See defaults/main.yml

## Example:

```
- hosts: controller
  roles:
    - { role: lma_stack,
          slack_token: "13123123",
          slack_api_url: "linuxsimba.slack.com",
          slack_channel_name: "mos-alert" }
```

## Dependencies

It does not depend on any other ansible role


## License

MIT

## Author Information
Stanley Karunditu
