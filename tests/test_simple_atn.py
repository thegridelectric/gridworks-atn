import time
import uuid

import pendulum
import pika
from gridworks_test import TimeCoordinatorStubRecorder
from gridworks_test import load_rabbit_exchange_bindings
from gridworks_test import wait_for

from gwatn import atn_utils
from gwatn.config import AtnSettings
from gwatn.enums import MessageCategory
from gwatn.enums import UniverseType
from gwatn.simple_atn_actor import SimpleAtnActor as Atn
from gwatn.types import LatestPrice_Maker
from gwatn.types import SimTimestep_Maker


def test_atn():
    atn = Atn(AtnSettings())
    atn.start()
    wait_for(lambda: atn._consuming, 2, "actor is consuming")
    wait_for(lambda: atn._publish_channel, 2, "actor publish channel exists")
    wait_for(lambda: atn._publish_channel.is_open, 2, "actor publish channel exists")

    load_rabbit_exchange_bindings(atn._consume_channel)
    ##################
    # test receiving simulated timestep - add stub time coordinator
    ###################
    assert atn_utils.is_dummy_atn_params(atn.atn_params)
    assert atn.universe_type == UniverseType.Dev
    assert atn._time == atn.settings.initial_time_unix_s
    assert atn.time() == atn._time

    d = pendulum.datetime(year=2020, month=1, day=1, hour=5)
    t = d.int_timestamp
    payload = SimTimestep_Maker(
        from_g_node_alias="d1.time",
        from_g_node_instance_id=str(uuid.uuid4()),
        time_unix_s=t,
        timestep_created_ms=1000 * int(time.time()),
        message_id=str(uuid.uuid4()),
    ).tuple
    routing_key = "rjb.d1-time.timecoordinator.sim-timestep"
    properties = pika.BasicProperties(
        # reply_to=self.queue_name,
        # app_id=self.alias,
        type=MessageCategory.RabbitJsonBroadcast,
        correlation_id=str(uuid.uuid4()),
    )
    atn._publish_channel.basic_publish(
        exchange="timecoordinatormic_tx",
        routing_key=routing_key,
        body=payload.as_type(),
        properties=properties,
    )
    # Wait and Check that not atn_utils.is_dummy_atn_params(atn.atn_params)
    # Check that broadcast "atn.params.report.heatpumpwithbooststore" happened
    atn.stop()


#
# def test_price_received_before_timestep():
#     atn = Atn(Settings())
#     tc = TimeCoordinatorStubRecorder(Settings())
#     atn.start()
#     tc.start()
#
#     wait_for(lambda: atn._publish_channel, 2, "actor publish channel exists")
#
#     wait_for(lambda: atn._publish_channel.is_open, 2, "actor publish channel exists")
#
#     midnight = pendulum.datetime(year=2020, month=1, day=1, hour=5).int_timestamp
#     next_slot = atn.next_run.Slot
#     assert next_slot.StartUnixS == midnight
#     assert atn.time() < midnight
#     assert atn.time() > atn.active_run.Slot.StartUnixS
#     assert atn.next_run.Price is None
#
#     midnight_price = LatestPrice_Maker(
#         from_g_node_alias="d1.isone.ver.keene",
#         from_g_node_instance_id=str(uuid.uuid4()),
#         price_times1000=22600,
#         price_unit=MarketPriceUnit.USDPerMWh,
#         market_slot_name=atn_utils.name_from_market_slot(next_slot),
#         irl_time_utc=pendulum.from_timestamp(time.time()).to_iso8601_string(),
#         message_id=str(uuid.uuid4()),
#     ).tuple
#
#     midnight_timestep = SimTimestep_Maker(
#         from_g_node_alias="d1.time",
#         from_g_node_instance_id=str(uuid.uuid4()),
#         time_unix_s=midnight,
#         timestep_created_ms=int(time.time() * 1000),
#         message_id=str(uuid.uuid4()),
#     ).tuple
#
#     # Atn receives midnight price before midnight timestep
#     atn.latest_price_from_market_maker(midnight_price)
#     assert tc.atn_ready == False
#     assert atn.time() < midnight
#     assert atn.next_run.Price == 22.6
#     atn.timestep_from_timecoordinator(midnight_timestep)
#     wait_for(lambda: tc.atn_ready, 2, "timecoordinator got ready from atn")
#     assert tc.atn_ready == True
#     tc.stop()
#     atn.stop()
#
#
# def test_timestep_received_before_price():
#     atn = Atn(Settings())
#     tc = TimeCoordinatorStubRecorder(Settings())
#     atn.start()
#     tc.start()
#
#     wait_for(lambda: atn._publish_channel, 2, "actor publish channel exists")
#
#     wait_for(lambda: atn._publish_channel.is_open, 2, "actor publish channel exists")
#
#     midnight = pendulum.datetime(year=2020, month=1, day=1, hour=5).int_timestamp
#     next_slot = atn.next_run.Slot
#     assert next_slot.StartUnixS == midnight
#     assert atn.time() < midnight
#     assert atn.time() > atn.active_run.Slot.StartUnixS
#     assert atn.next_run.Price is None
#
#     midnight_price = LatestPrice_Maker(
#         from_g_node_alias="d1.isone.ver.keene",
#         from_g_node_instance_id=str(uuid.uuid4()),
#         price_times1000=22600,
#         price_unit=MarketPriceUnit.USDPerMWh,
#         market_slot_name=atn_utils.name_from_market_slot(next_slot),
#         irl_time_utc=pendulum.from_timestamp(time.time()).to_iso8601_string(),
#         message_id=str(uuid.uuid4()),
#     ).tuple
#
#     midnight_timestep = SimTimestep_Maker(
#         from_g_node_alias="d1.time",
#         from_g_node_instance_id=str(uuid.uuid4()),
#         time_unix_s=midnight,
#         timestep_created_ms=int(time.time() * 1000),
#         message_id=str(uuid.uuid4()),
#     ).tuple
#
#     atn.timestep_from_timecoordinator(midnight_timestep)
#     assert tc.atn_ready == False
#     assert int(atn.time()) == midnight
#     assert atn.active_run.Slot.StartUnixS == midnight
#     assert atn.active_run.Price is None
#
#     atn.latest_price_from_market_maker(midnight_price)
#
#     assert atn.active_run.Price == 22.6
#     wait_for(lambda: tc.atn_ready, 2, "timecoordinator got ready from atn")
#     assert tc.atn_ready == True
#     tc.stop()
#     atn.stop()
#
#
