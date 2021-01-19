from flask import abort, current_app, g
from python_freeipa import ClientMeta


def get_ipa_client():
    if g.gss_creds is None:
        abort(401)
    client = ClientMeta(
        current_app.config["IPA_SERVER"],
        verify_ssl=current_app.config["IPA_CA_CERT_PATH"],
    )
    client.login_kerberos()
    return client
