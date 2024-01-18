import os
import pytest
from datetime import datetime
from jelastic import Jelastic

JELASTIC_URL = os.environ.get("JELASTIC_URL", "https://jca.xapp.cloudmydc.com/")
JELASTIC_TOKEN = os.environ.get("JELASTIC_TOKEN")

if not JELASTIC_TOKEN:
    raise Exception("JELASTIC_TOKEN must be set as environment variables")

CURRENT_DATETIME = datetime.now()


@pytest.fixture
def client():
    client = Jelastic(base_url=JELASTIC_URL, token=JELASTIC_TOKEN)
    return client.billing


def test_get_account(client):
    response = client.Account.GetAccount()
    assert isinstance(response, dict)


def test_get_account_billing_by_engine_type_and_period(client):
    response = client.Account.GetAccountBillingByEngineTypeAndPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME
    )
    assert isinstance(response, dict)


def test_get_account_billing_history_by_period(client):
    response = client.Account.GetAccountBillingHistoryByPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME
    )
    assert isinstance(response, dict)


def test_accounts(client):
    response = client.Account.GetAccounts()
    assert isinstance(response, dict)


def test_get_accounts_by_limits(client):
    response = client.Account.GetAccountsByLimits(
        [
            "1234:100",
        ]
    )
    assert isinstance(response, dict)


def test_get_accounts_by_personal_threshold(client):
    response = client.Account.GetAccountsByPersonalThreshold()
    assert isinstance(response, dict)


def test_get_accounts_by_uids(client):
    response = client.Account.GetAccountsByUids(["1234:100"])
    assert isinstance(response, dict)


def test_get_accounts_for_deactivation(client):
    response = client.Account.GetAccountsForDeactivation()
    assert isinstance(response, dict)


def test_get_accounts_for_destroying(client):
    response = client.Account.GetAccountsForDestroying()
    assert isinstance(response, dict)


def test_get_agg_cluster_billing_history(client):
    response = client.Account.GetAggClusterBillingHistory(
        CURRENT_DATETIME, CURRENT_DATETIME, 10, ["CPU"]
    )
    assert isinstance(response, dict)


def test_get_agg_extra_billing_history(client):
    response = client.Account.GetAggExtraBillingHistory(
        CURRENT_DATETIME, CURRENT_DATETIME, 10
    )
    assert isinstance(response, dict)


def test_get_collaboration_quotas(client):
    response = client.Account.GetCollaborationQuotas(owner_uid=77)
    assert isinstance(response, dict)


def test_get_countries(client):
    response = client.Account.GetCountries()
    assert isinstance(response, dict)


def test_get_country_states(client):
    response = client.Account.GetCountryStates(country_code="US")
    assert isinstance(response, dict)


def test_get_env_billing_history_by_period(client):
    response = client.Account.GetEnvBillingHistoryByPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME, "DAY"
    )
    assert isinstance(response, dict)


def test_get_extended_account_billing_history_by_period(client):
    response = client.Account.GetExtendedAccountBillingHistoryByPeriod(
        CURRENT_DATETIME, CURRENT_DATETIME

    )
    assert isinstance(response, dict)


def test_get_extern_billing_systems(client):
    response = client.Account.GetExternBillingSystems()
    assert isinstance(response, dict)


def test_get_fund_account_history(client):
    response = client.Account.GetFundAccountHistory(
        CURRENT_DATETIME, CURRENT_DATETIME, 33
    )
    assert isinstance(response, dict)


def test_get_quotas(client):
    response = client.Account.GetQuotas()
    assert isinstance(response, dict)


def test_get_sum(client):
    response = client.Account.GetSum(33, CURRENT_DATETIME, CURRENT_DATETIME)
    assert isinstance(response, dict)


def test_get_sum_account_billing_history(client):
    response = client.Account.GetSumAccountBillingHistory(
        33, CURRENT_DATETIME, CURRENT_DATETIME
    )
    assert isinstance(response, dict)


def test_get_suspended_accounts(client):
    response = client.Account.GetSuspendedAccounts()
    assert isinstance(response, dict)
