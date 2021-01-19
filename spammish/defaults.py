# This file contains the default configuration values

TEMPLATES_AUTO_RELOAD = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

HEALTHZ = {
    "live": "spammish.utils.healthz.liveness",
    "ready": "spammish.utils.healthz.readiness",
}

IPA_SERVER = "ipa.spammish.test"
IPA_CA_CERT_PATH = "/etc/ipa/ca.crt"
