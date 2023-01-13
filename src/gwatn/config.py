"""Settings for an AtomicTNode, readable from environment and/or from env files."""

import pendulum
from gridworks.gw_config import AlgoApiSecrets
from gridworks.gw_config import GNodeSettings
from gridworks.gw_config import Public
from pydantic import BaseSettings
from pydantic import SecretStr


class Settings(GNodeSettings):
    g_node_alias: str = "d1.isone.ver.keene.holly"
    g_node_role_value: str = "AtomicTNode"
    my_super_alias: str = "d1.isone.ver.keene.super1"

    # Next 4 settings are consistent with dev env settings in gridworks-marketmaker repo
    market_maker_alias = "d1.isone.ver.keene"
    market_maker_algo_address = (
        "CYWMWYHJ7ON4IR5XQDJBBPDU472QU4KJQ6XQVZBIIRTCHT6SHTFNHEAVC4"
    )
    mm_api_root = "http://localhost:7997"
    initial_time_unix_s = pendulum.datetime(
        year=2020, month=1, day=1, hour=4, minute=20
    ).int_timestamp

    class Config:
        env_prefix = "ATN_"
        env_nested_delimiter = "__"


class SupervisorSettings(GNodeSettings):
    g_node_alias: str = "d1.isone.ver.keene.super1"
    g_node_role_value: str = "Supervisor"

    class Config:
        env_prefix = "SUPER_"
        env_nested_delimiter = "__"


class ValidatorSettings(BaseSettings):
    algo_api_secrets: AlgoApiSecrets = AlgoApiSecrets()
    public: Public = Public()
    sk: SecretStr = SecretStr(
        "FCLmrvflibLD6Deu3NNiUQCC9LOWpXLsbMR/cP2oJzH8IT4Zu8vBAhRNsXoWF+2i6q2KyBZrPhmbDCKJD7rBBg=="
    )
    cert_name: str = "Molly Metermaid"
    name: str = "Molly Inc Telemetry Surveyors and Purveyors"
    api_root: str = "http://localhost:8001"

    class Config:
        env_prefix = "VLDTR_"
        env_nested_delimiter = "__"


class TaOwnerSettings(BaseSettings):
    algo_api_secrets: AlgoApiSecrets = AlgoApiSecrets()
    public: Public = Public()
    sk: SecretStr = SecretStr(
        "sp4SDWmH8Rin0IhPJQq1UMsSR5C0j1IGqzLdcwCMySBVzT8lEUwjwwpS9z6l6dKSg52WWEjRdJDAL+eVt4kvBg=="
    )

    ta_daemon_addr: str = "NZXUSTZACPVJBHRSSJ5KE3JUPCITK5P2O4FE67NYPXRDVCJA6ZX4AL62EA"
    ta_validator_addr: str = (
        "7QQT4GN3ZPAQEFCNWF5BMF7NULVK3CWICZVT4GM3BQRISD52YEDLWJ4MII"
    )
    ta_validator_api_root: str = "http://localhost:8001"
    ta_daemon_api_fqdn: str = "http://localhost"
    ta_daemon_api_port: str = "8002"
    initial_ta_alias: str = "d1.isone.ver.keene.holly.ta"
    micro_lat: int = 45511230
    micro_lon: int = -68354650

    class Config:
        env_prefix = "HH_"
        env_nested_delimiter = "__"


class TaDaemonSettings(BaseSettings):
    algo_api_secrets: AlgoApiSecrets = AlgoApiSecrets()
    public: Public = Public()
    sk: SecretStr = SecretStr(
        "tQ8ABbLLR96cnRE3Y2tlrj2d/rNPRFkf8FosJ46tVIlub0lPIBPqkJ4yknqibTR4kTV1+ncKT324feI6iSD2bw=="
    )
    ta_owner_addr: str = "KXGT6JIRJQR4GCSS647KL2OSSKBZ3FSYJDIXJEGAF7TZLN4JF4DGDDX4BI"
    validator_addr: str = "7QQT4GN3ZPAQEFCNWF5BMF7NULVK3CWICZVT4GM3BQRISD52YEDLWJ4MII"

    class Config:
        env_prefix = "TAD_"
        env_nested_delimiter = "__"


class DiscovererSettings(BaseSettings):
    algo_api_secrets: AlgoApiSecrets = AlgoApiSecrets()
    public: Public = Public()
    sk: SecretStr = SecretStr(
        "X20eXB/VZilEmzaPCDSn9WsuGZ5/f0+IxuEhfYfVtmZR9q5bcbjpBodPpiUCCkr0Xv11sKYxf08PnAKQFNtW3Q=="
    )
    discovered_ctn_alias = "d1.isone.ver.keene.pwrs"
    original_child_alias_list = ["d1.isone.ver.keene.holly"]
    micro_lat = 44838681
    micro_lon = -68705311
