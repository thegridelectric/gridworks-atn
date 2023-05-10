Forward Looking Optimizer (FLO)
================================


![alt_text](images/flo-pic.png)



Atn Params
^^^^^^^^^^^^

Each ATN Strategy has a set of parameters that are tuned over time to optimize its performance
on the basis of historical data. These parameters can also be used to initialize and
run a GNodeInstance managing that strategy.  Many of these parameters will be shared in
common with the parameters used for the FLO, but some will be used to _derive_ specific
FLO params (for example, an AtomicTNode will have a parameter that it uses to get price
forecasts, typically in the form of a subscription to a price service, while the FLO will
include a sequence of price forecasts over the next 48 hours.

As an example, consider the atn  parameters for the
`brick storage heater <https://gridworks-atn.readthedocs.io/en/latest/types/atn-params-brickstoraheheater.html>`_

Flo Params
^^^^^^^^^^^^
Each FLO has a set of input parameters used to generate its output.

As an example, consider the flo parameters for the
`brick storage heater <https://gridworks-atn.readthedocs.io/en/latest/types/flo-params-brickstoraheheater.html>`_
