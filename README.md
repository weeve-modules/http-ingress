# HTTP Ingress


|              |                                                             |
| ------------ | ----------------------------------------------------------- |
| name         | HTTP Ingress                                                |
| version      | v0.0.1                                                      |
| docker image | [weevenetwork/weeve-http-ingress](https://linktodockerhub/) |
| tags         | Python, Flask, Docker, Weeve                                |
| authors      | Jakub Grzelak                                               |

***
## Table of Content
- [HTTP Ingress](#http-ingress)
  - [Description](#description)
  - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)




## Description 

This module takes and processes ingress from HTTP POST requests.

### Features
1. Flask ReST client
2. Receives HTTP POST request
3. Request - sends HTTP Request to the next module

## Environment Variables

### Module Specific
The following module configurations can be provided in a data service designer section on weeve platform:

| Name          | Environment Variables  | type   | Description                                                     |
| ------------- | ---------------------- | ------ | --------------------------------------------------------------- |
| Handler Host  | HANDLER_HOST           | string | Handler host address to which HTTP POST request should be sent. |
| Handler Port  | HANDLER_PORT           | string | Handler port address to which HTTP POST request should be sent. |

***

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
| --------------------- | ------ | -------------------------------------- |
| EGRESS_API_HOST       | string | HTTP ReST endpoint for the next module |
| MODULE_NAME           | string | Name of the module                     |



## Dependencies

```txt
Flask==1.1.1
requests
python-dotenv
```

## Output
Output of this module is JSON body the same as the JSON body received from HTTP POST request.
