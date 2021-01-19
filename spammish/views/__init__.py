from flask import Blueprint

from spammish.utils import import_all


blueprint = Blueprint("root", __name__)
import_all("spammish.views")
