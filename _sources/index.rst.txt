.. py-jelastic documentation master file, created by
   sphinx-quickstart on Sat Dec 16 01:00:00 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. meta::
   :description: Index of user documentation for py-jelastic - Jelastic Python Client library
   :keywords: jelastic, vap, cloudmydc, cloud, application, hosting, client, api

.. title:: py-jelastic - Jelastic Python Client library

`py-jelastic` documentation
===========================

Getting Started
---------------

To begin, import the Jelastic client and instantiate the API.

.. code-block:: python

    from jelastic import Jelastic
    jelastic = Jelastic(
         'https://app.xapp.cloudmydc.com',
         token='d6f4e314a5b5fefd164995169f28ae32d987704f'
    )


The library follows the convention from the Jelastic API documentation. For example, to get the list of accounts, you would do the following:

.. code-block:: python

    from jelastic import Jelastic

    jelastic = Jelastic(
         'https://app.xapp.cloudmydc.com',
         token='d6f4e314a5b5fefd164995169f28ae32d987704f'
    )

    accounts = jelastic.billing.Account.GetAccounts()


The result is a JSON dictionary returned from the Jelastic API.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   install
   abstract
   administration
   automation
   billing
   data
   development
   environment
   exceptions
   iaas
   io
   management
   marketplace
   message
   migration
   platform
   pool
   pricing
   s3
   security
   thirdparty
   users
   utils

Project
-------

.. toctree::
   :maxdepth: 2

   support
   changes

Links
-----

.. toctree::
   :maxdepth: 2

   Website <https://cloudmydc.com>
   Application <https://app.xapp.cloudmydc.com>
   Github <https://github.com/Onemind-Services-LLC/py-jelastic>

.. Indices and tables
   ==================
   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
