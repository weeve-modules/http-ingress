# HTTP Ingress


|              |                                                                                       |
| ------------ | ------------------------------------------------------------------------------------- |
| name         | HTTP Ingress                                                                          |
| version      | v0.0.1                                                                                |
| docker image | [weevenetwork/weeve-http-ingress](https://hub.docker.com/r/weevenetwork/http-ingress) |
| authors      | Jakub Grzelak                                                                         |

***
## Table of Content
- [HTTP Ingress](#http-ingress)
  - [Table of Content](#table-of-content)
  - [Description](#description)
    - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Examples](#examples)
    - [Input](#input)
    - [Output](#output)
  - [docker-compose example](#docker-compose-example)

## Description 

This module takes and processes ingress from HTTP POST requests.

### Features
1. Creates a HTTP ReST Server
2. Receives data in POST body

## Environment Variables

### Module Specific
The following module configurations can be provided in a data service designer section on weeve platform:

| Name         | Environment Variables | type   | Description                                                     |
| ------------ | --------------------- | ------ | --------------------------------------------------------------- |
| Handler Host | HANDLER_HOST          | string | Handler host address to which HTTP POST request should be sent. |
| Handler Port | HANDLER_PORT          | string | Handler port address to which HTTP POST request should be sent. |

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

## Examples

### Input
HTTP ReST POST request with request-body
### Output
Output of this module is JSON body the same as the JSON body received from HTTP POST request.

## docker-compose example

```yml
version: "3"
services:
  boilerplate:
    image: weevenetwork/http-ingress
    environment:
      MODULE_NAME: http-imgress
      EGRESS_API_HOST: https://hookb.in/r1YwjDyn7BHzWWJVK8Gq
      HANDLER_PORT: 80
      HANDLER_HOST: 255.456.789.255
    ports:
      - 5000:80
```