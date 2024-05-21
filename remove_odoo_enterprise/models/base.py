# Copyright 2019-2020 Onestein (<https://www.onestein.eu>)
# Copyright 2023 Le Filament (https://le-filament.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class Base(models.AbstractModel):
    _inherit = "base"

    @api.model
    def search(self, domain, offset=0, limit=None, order=None):
        res = super().search(domain, offset, limit, order)
        if self._name == "payment.provider":
            res = res.filtered(lambda a: not a.module_to_buy)
        return res
