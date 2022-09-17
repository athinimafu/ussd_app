import os
import africastalking as at_client

AT_SANDBOX = os.environ.get("AT_SANDBOX")
AT_KEY = os.environ.get("AT_KEY")
at_client.initialize(AT_SANDBOX, AT_KEY)
