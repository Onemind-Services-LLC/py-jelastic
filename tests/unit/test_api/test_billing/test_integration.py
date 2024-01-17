from . import *


def test_get_invoice_url(client):
    client._get.return_value = success_response
    response = client.Integration.GetInvoiceUrl(1)
    client._get.assert_called_with("GetInvoiceUrl", params={"invoiceId": 1})
    assert response == success_response


def test_get_sso_url(client):
    client._get.return_value = success_response
    response = client.Integration.GetSSOUrl("path")
    client._get.assert_called_with(
        "GetSSOUrl",
        params={"path": "path"},
    )
    assert response == success_response
