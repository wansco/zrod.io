# zrod.io

If you want to learn more about this project, please contact me.

Flexible rod design.


## Overview
zrod.io provides a simple API to process rod design input data using the industry standard wave equation method. This repository contains example implementations for the front end UI only (not the backend calculations). The core (backend) calculations have not been thoroughly vetted. Please provide feedback on issues with the resulting calculations.


#### Architecture
In an effort to avoid the complicated licensing models and dongles required by other rod design software solutions, we have placed all the mathematical models on a hosted server and provide access through a simple API. This allows us to open source the front-end code. You are free to modify the source code in accordance with the GPL. If you wish to modify the code and distribute a commercial (closed-source) version, please contact me.


### API Key
zrod.io requires an API Key and an account to access the service. Please contact me to obtain an API Key for testing. Please note that the API authentication process is likely to change. Please do not hard-code your API key as that is subject to revocation.

The example jupyter notebook has a default key that is limited to 1 request per minute. In other words, you should contact me to get a key if you actually plan on using this for anything. Also, that default example key may be revoked at anytime.


#### Project State
I am still developing the documentation and front end source code. Please check back as I plan on updating this repository in the near future.

This project has evolved over time. The API needs to be restructured, so please be aware that anything built on top of this project may see breaking changes. If you want to avoid that, make sure you contact me.

