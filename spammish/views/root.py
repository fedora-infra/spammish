from flask import g, render_template

from ..utils.ipa import get_ipa_client
from ..utils.models import StageUser
from . import blueprint as bp


# Possible statuses:
# - spamcheck_awaiting: basset has not checked it yet
# - active: not spam
# - spamcheck_denied: spam
# - spamcheck_manual: basset does not know, manual check needed


@bp.route("/")
def root():
    ipa = get_ipa_client()
    stage_users = ipa.stageuser_find()["result"]
    return render_template(
        "index.html", stage_users=[StageUser(su) for su in stage_users]
    )
