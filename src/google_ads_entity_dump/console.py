import os
from typing import NamedTuple, Mapping

from google_ads_entity_dump import exceptions


class GAQLContext(NamedTuple):
    client_customer_id: str
    client_id: str
    client_secret: str
    developer_token: str
    login_customer_id: str
    refresh_token: str


def ensure_full_context(candidate: Mapping, source: str) -> GAQLContext:
    required = set(GAQLContext._fields)
    available = set(candidate.keys())
    missing = required.difference(available)
    if missing:
        missing_str = ", ".join(missing)
        raise exceptions.ContextException(f"Following context values were missing in {source}: {missing_str}")
    return GAQLContext(**{k: str(candidate[k]) for k in required})


def from_envvars() -> GAQLContext:
    prefix = "GAED_"
    raw_context = {k[len(prefix) :].lower(): os.environ[k] for k in os.environ if k.startswith(prefix)}
    return ensure_full_context(raw_context, "envvars")


def main():
    ctx = from_envvars()
    raise NotImplementedError(ctx)
