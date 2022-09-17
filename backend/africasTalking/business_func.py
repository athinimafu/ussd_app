from . import at_client
from flask import blueprints

business_blueprint = blueprints.Blueprint(__name__, 'business')


@business_blueprint.route('/deposit', 'GET')
def deposit_view():
    return "Deposit View: Some form will go here"


@business_blueprint.route('/deposit', 'POST')
def deposit():
    return "Depositing to users"
