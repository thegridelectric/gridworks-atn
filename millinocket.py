import subprocess
import time

import gridworks.algo_utils as algo_utils
import gridworks.gw_config as config
from rich.pretty import pprint

import gwatn.demo_methods as demo_methods
from gwatn import DispatchContract
from gwatn.scada_actor import ScadaActor
from gwatn.simple_atn_actor import SimpleAtnActor as Atn


sim_size = 1
ta_owners = []

try:
    scada = ScadaActor()
except:
    print("Setting up certs")
    ta_owners = demo_methods.cert_creation(sim_size=sim_size)
    scada = ScadaActor()

input("Hit return to see ScadaCertId")
pprint(scada.cert_id)

input("SCADA: Hit return to see scada account info")
pprint(scada.client.account_info(scada.acct.addr))

print("")

print(f"Note that the SCADA owns one asset, an NFT with id {scada.cert_id.Idx}")
print(f"The SCADA has created one app, with id {scada.dc_app_id}")
if not scada.in_dispatch_contract():
    print("SCADA  has not yet opted into that app")
print("")
print("")
input(f"Hit return to inspect the ASA {scada.cert_id.Idx}")
pprint(scada.client.asset_info(scada.cert_id.Idx))

input("SCADA: Hit return to see application state for the DispatchContract")
pprint(scada.dc_client.get_application_state())
print("")
print(
    "When the SCADA called the bootstrap1 method of the DispatchContract, it provided"
)
print(
    "its address (as governor), the ta_alias, and the scada_cert_idx. It also funded the contract "
)
print("")
input("SCADA: Hit return to call the hello method of the DispatchContract")

hello_method_result = scada.dc_client.call(
    DispatchContract.hello,
    name="DispatchContract",
).return_value

pprint(hello_method_result)

print("")
print("")
time.sleep(2)
print(
    "Starting SCADA actor. Check http://0.0.0.0:15672/#/queues for d1.isone.ver.keene.holly.scada.F-xxx"
)
scada.start()

print("")
print("")
input("Hit return to initialize AtomicTNode actor")
atn = Atn()

print("")
print("")
input("ATN: Hit return to see Atn's TradingRightsId")
pprint(atn.trading_rights_id)

input("ATN: Hit return to see atn's account info")
pprint(atn.client.account_info(atn.acct.addr))

print(f"Note that the Atn owns one asset, an NFT with id {atn.trading_rights_id.Idx}")
print("")
print("")
input(f"Hit return to inspect the ASA {atn.trading_rights_id.Idx}")
pprint(atn.client.asset_info(atn.trading_rights_id.Idx))


print("")
print("")
time.sleep(2)
print(
    "Starting SCADA actor. Check http://0.0.0.0:15672/#/queues for d1.isone.ver.keene.holly.F-xxx"
)
atn.start()

print("")
print("")
print(
    "The SCADA will now send the Atn a 'join.dispatch.contract' message over RabbitMq"
)
print("API for `join.dispatch.contract`:")
print(
    "https://gridworks-atn.readthedocs.io/en/latest/apis/types.html#joindispatchcontract"
)
print("SDK docs for `join.dispatch.contract`:")
print(
    "https://gridworks-atn.readthedocs.io/en/latest/types/join-dispatch-contract.html"
)
print("")
print("")
print(
    "When the AtomicTNode gets this message, it will finish bootstrapping the DispatchContract, "
)
print(
    "opt into the DispatchContract, and send a `dispatch.contract.confirmed.heatpumpwithbooststore`"
)
print("message over RabbitMq back to the Scada")
print(
    "https://gridworks-atn.readthedocs.io/en/latest/apis/types.html#dispatchcontractconfirmedheatpumpwithbooststore"
)
print("SDK docs for `join.dispatch.contract`:")
print(
    "https://gridworks-atn.readthedocs.io/en/latest/types/dispatch-contract-confirmed-heatpumpwithbooststore.html"
)
print("")
print("")
print("When the SCADA receives this message, it completes the contract initialization")
print("process by opting into the DispatchContract")
print("")
print("")
time.sleep(4)
print("At this point, the SCADA will accept dispatch commands from the AtomicTNode,")
print("the Atn and SCADA begin heartbeating, and they also begin sending their")
print("heart beats to the DispatchContract")
print("")
print("")
if not scada.in_dispatch_contract():
    input("Hit return to run scada.initialize_dispatch_contract()")
    scada.initialize_dispatch_contract()


input("SCADA: Hit return to see application state for the DispatchContract")
print("")
pprint(scada.dc_client.get_application_state())
print("")
print("The application state now includes the ta_trading_rights_idx")

input("SCADA: Hit return to see scada account info")
print("")
pprint(scada.client.account_info(scada.acct.addr))

print("")
print(
    f"The SCADA has opted into the Dispatch Contract (apps-local-state includes {scada.dc_app_id})"
)

input("ATN: Hit return to see atn's account info")
pprint(atn.client.account_info(atn.acct.addr))

print("")
print(f"The Atn has also opted into the Dispatch Contract")

print("")
print(f"scada.in_dispatch_contract(): {scada.in_dispatch_contract()} ")
print("")
print("The AtomicTNode sends a heartbeat once a minute, and the Scada responds ASAP")
print("We can run this manually before starting simulated time")
print("")
print("")
input("Hit return to run atn.hb_to_scada()")

atn.hb_to_scada()

print("")
print("")
print("")
print("After sending the heartbeat over rabbit, both the Atn and Scada")
print("called the heartbeat_algo_audit method of the DispatchContract")
print("with a report of the heartbeat they just sent")

# api_endpoint = f"http://0.0.0.0:8000/pause-time/"
# r = requests.post(url=api_endpoint)
#
#
# cmd = "docker compose -f docker-api.yml down"
# subprocess.run(cmd.split())

# print("")
# print("")
# print("The demo is now ready to start the simulated trading.")
# print("")
# time.sleep(2)
# print("The AtomicTNodes have access to simulated weather and price forecasts for 2020")
# print("")
# time.sleep(2)
# print("The MarketMaker has access to 2020 prices for Keene Rd")
# print("")
# time.sleep(2)
# print("Once the simulation starts, time moves forward in hourly timesteps")
# print("You can see time advancing in the marketmaker terminal window")
# print("Or at the marketmaker API: http://localhost:7997/get-time/")
# time.sleep(2)
# print("The rabbit queues will also start to get busy")
# print("http://d1-1.electricity.works:15672/#/queues")
# print("")
# time.sleep(2)

# input("HIT RETURN TO START SIMULATED TIME")

# print("")
# print("")
# print("")
# print("")

# api_endpoint = f"http://0.0.0.0:8000/resume-time/"
# r = requests.post(url=api_endpoint)


# time.sleep(2)
# print("")
# print("")
# print("In another window, try python pause_time.py (and `python resume_time.py`)")
# print("")
# print("")
# time.sleep(2)


input("HIT RETURN TO STOP SIMULATION")

cmd = "docker compose -f docker-api.yml down"
subprocess.run(cmd.split())

atn.stop()
scada.stop()

for ta_owner in ta_owners:
    ta_owner.stop()
