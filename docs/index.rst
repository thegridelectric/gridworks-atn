GridWorks AtomicTNode SDK
=========

This is the `GridWorks <https://gridworks.readthedocs.io/>`_ Python SDK for building Atomic Transactive Nodes, or
`AtomicTNodes <https://gridworks.readthedocs.io/en/latest/atomic-t-node.html>`_. AtomicTNodes are the most fun and interesting GridWorks actors to design and build. They are what make electrical devices
*transactive*. More specifically, each AtomicTNode is dedicated to the job of operating its very own
`Transactive Device <https://gridworks.readthedocs.io/en/latest/transactive-device.html>`_. This is a
juggling act. The AtomicTNode bids into electricity markets 24-7 so that its Transactive Device
can thriftly taking advantage of the lowest prices. Simultaneously, the AtomicTNode has to respect the
primary use of the device.


The `GridWorks Millinocket demo  <https://gridworks.readthedocs.io/en/latest/story.html>`_ is a simulation of
hundreds of transactive thermal storage heating systems bidding into a local PNode market of
`ISO NE <https://www.iso-ne.com/>`_, the grid operator running wholesale electricity markets for
New England. (The simulated AtomicTNodes in this demo uses proprietary code built on top of this SDK).
The simulated results are impressive: significantly cutting the operating costs
of home heating while simultaneously reducing the curtailment (i.e. turning off and wasting) of local
wind farms.


Imagine I tell you that the transactive heating systems in the demo are real.

Do you believe me?

If you are the grid operator, are you prepared to settle financial transactions with
these heaters?  In order for an aggregation of AtomicTNode (aka, an
`AggregatedTNode  <https://gridworks.readthedocs.io/en/latest/aggregated-t-node.html>`_)
to participate in
electricity markets, the grid operator needs a reason to believe that the AtomicTNode is:
   - WHERE it claims to be on the electric grid;
   - consuming WHAT it claims to be consuming (in terms of kWh of electricity); and
   - that WHEN it claims to consume is accurate.

This calls a mechanism that enables distributed, decentralized, secure, and trustless transactions.

Enter the Algorand blockchain.

The first thing this SDK does is provide blockchain-related mechanisms for establishing these transactions.
Go through the `Validation <tadeed>`_ and `Atn Contract <dispatch-contract>`_ sequences in this documetation
in order to learn how this works.



To explore the rest of GridWorks, visit the `GridWorks docs <https://gridworks.readthedocs.io/en/latest/>`_.



Installation
^^^^^^^^^^^^

.. note::
    gridworks-atn requires python 3.10 or higher.


.. code-block:: console

    (venv)$ pip install gridworks-atn


.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Code Support

    Hello AtomicTNode <hello-atn>
    Brick Storage Heater model <brick-storage-heater>
    Forward Looking Optimization <flo>
    Simple Scada Simulation <simple-sim-scada>
    Lexicon <https://gridworks.readthedocs.io/en/latest/lexicon.html>


.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: API docs

    Type APIs <apis/types>

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: SDK docs

    TwoChannelActorBase <two-channel-actor-base>
    DataClasses <data-classes>
    Enums <enums>
    Types <sdk-types>

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Participate

    Contributing <contributing>
    Code of Conduct <codeofconduct>
    License <license>
