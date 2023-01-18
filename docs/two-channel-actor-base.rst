TwoChannelActorBase
=====================

This is similar to the `ActorBase <https://gridworks.readthedocs.io/en/latest/actor-base.html>`_ available
in the gridworks package (included as a sub-package here).

The difference is that ActorBase publishes and consumes from the same channel, while the TwoChannelActorBase
publishes and consumes on different channels - which is the method that RabbitMq recommends. Having two
channels helps prevent slow-downs and gridlock, which is especially important for AtomicTNodes as they
send and receive a lot of messages.

At some point both will be combined. However, there is an intermittent bug in the TwoChannelActorBase, which
is that if the publishing channel stops working correctly it does not get restarted. The currently implemented
workaround for this is to have Supervisor GNodes use their consuming channel for both publishing and consuming.
That channel is correctly restarted when it stops working. In addition, the Supervisor will detect if any
of its Subordinates (e.g. an AtomicTNode) have a faulty publishing channel and will kill and restart them.

.. automodule:: gwatn.two-channel-actor-base


This class should **not** be initialized directly.

.. autoclass:: AtnActorBase
    :members:
