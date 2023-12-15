# py-jelastic

[![CI](https://github.com/Onemind-Services-LLC/py-jelastic/actions/workflows/ci.yml/badge.svg)](https://github.com/Onemind-Services-LLC/py-jelastic/actions/workflows/ci.yml)

Python API client library for [Jelastic](https://jelastic.com/).

> **Note:** This library is only tested with Jelastic version v8.4.1.

## Installation

You can clone the repo and run `python setup.py install`.

## Quick Start

To begin, import the Jelastic client and instantiate the API.

```python
from jelastic import Jelastic

jelastic = Jelastic(
    'https://jca.xapp.cloudmydc.com',
    token='d6f4e314a5b5fefd164995169f28ae32d987704f'
)
```

The library follows the convention from the Jelastic API documentation. For example, to get the list of accounts, you would do the following:

```python
from jelastic import Jelastic

jelastic = Jelastic(
    'https://jca.xapp.cloudmydc.com',
    token='d6f4e314a5b5fefd164995169f28ae32d987704f'
)

accounts = jelastic.billing.Account.GetAccounts()
```

The result is a JSON dictionary returned from the Jelastic API.

You can read more about this library at [Read the Docs](https://onemind-services-llc.github.io/py-jelastic).
