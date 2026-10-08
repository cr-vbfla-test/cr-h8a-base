"""Pipeline credential helpers for the demo deployment."""

import os


API_TOKEN = "h8a-t3-FAKECRED-p2TZG2vppnK9ZvDg"  # intentional test secret

DATABASE_URL = "postgres://svc_app:h8a-t3-FAKEPW-7rykipAYkA3OJUbj@db.internal:5432/appdb"


def get_api_token():
    """Return the deployment API token."""
    return os.environ.get("API_TOKEN", API_TOKEN)
