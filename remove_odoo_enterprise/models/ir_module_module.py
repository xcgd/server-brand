# Copyright 2019-2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class IrModuleModule(models.Model):
    _inherit = "ir.module.module"

    @api.model
    def search_fetch(self, domain, field_names, offset=0, limit=None, order=None):
        domain += [("to_buy", "=", False)]
        return super().search_fetch(domain, field_names, offset, limit, order)
