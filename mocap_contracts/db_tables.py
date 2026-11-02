"""The DAO and migration of every table message.

Written by tools/harpia_gen.py (`make gen`); do not edit. Use
mocap_contracts.db."""

from harpia_generated.db.Proposal_cb110dd8cf55c19c22ff64a9cdf4d22e_dao import Proposal_dao
from harpia_generated.migrate.Proposal_cb110dd8cf55c19c22ff64a9cdf4d22e_migrate import migrate_Proposal
from harpia_generated.db.Request_cb110dd8cf55c19c22ff64a9cdf4d22e_dao import Request_dao
from harpia_generated.migrate.Request_cb110dd8cf55c19c22ff64a9cdf4d22e_migrate import migrate_Request
from harpia_generated.db.Review_cb110dd8cf55c19c22ff64a9cdf4d22e_dao import Review_dao
from harpia_generated.migrate.Review_cb110dd8cf55c19c22ff64a9cdf4d22e_migrate import migrate_Review

TABLES = {
    "Proposal": (Proposal_dao, migrate_Proposal),
    "Request": (Request_dao, migrate_Request),
    "Review": (Review_dao, migrate_Review),
}
