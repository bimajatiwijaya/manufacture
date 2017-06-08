# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models
#_bom_explode XXX


class StockMove(models.Model):
    _inherit = 'stock.move'

    # v10
    # def _prepare_procurement_from_move(self, move):
    def _prepare_procurement_from_move(self):
        res = super(StockMove, self)._prepare_procurement_from_move()
        if res and self.procurement_id and self.procurement_id.property_ids:
            res['property_ids'] = [(6, 0,
                                    self.procurement_id.property_ids.ids)]
        return res

    # v10
    # @api.model
    # def _action_explode(self, move):

    def action_explode(self):
        """ Explodes pickings.
        @param move: Stock moves
        @return: True
        """
        property_ids = self.procurement_id.sale_line_id.property_ids.ids
        return super(StockMove, self.with_context(
            property_ids=property_ids)).action_explode()