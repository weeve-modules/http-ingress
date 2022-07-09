# HTTP Ingress


|              |                                                                                 |
| ------------ | ------------------------------------------------------------------------------- |
| name         | HTTP Ingress                                                                    |
| version      | v0.0.1                                                                          |
| docker image | [weevenetwork/http-ingress](https://hub.docker.com/r/weevenetwork/http-ingress) |
| authors      | Jakub Grzelak                                                                   |

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

| Name      | Environment Variables | type   | Description                                 |
| --------- | --------------------- | ------ | ------------------------------------------- |
| Host Name | HOST_NAME             | string | Host name/address where the server will run |
| Port      | HOST_PORT             | string | Port on which the server will run           |

***

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
| --------------------- | ------ | -------------------------------------- |
| MODULE_NAME           | string | Name of the module                     |
| MODULE_TYPE           | string | Type of the module (ingress, processing, egress)                     |
| EGRESS_SCHEME         | string | URL Scheme    |
| EGRESS_HOST           | string | URL target host |
| EGRESS_PORT           | string | URL target port |
| EGRESS_PATH           | string | URL target path |
| EGRESS_URL            | string | HTTP ReST endpoint for the next module |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

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

Modules return a 200 response for success, and 500 for error. No other return message is supported.

## docker-compose example

```yml
version: "3"
services:
  boilerplate:
    image: weevenetwork/http-ingress
    environment:
      MODULE_NAME: http-ingress
      EGRESS_URL: https://testmp.free.beeceptor.com
      HOST_PORT: 80
      HOST_NAME: 255.456.789.255
    ports:
      - 5000:80
```
