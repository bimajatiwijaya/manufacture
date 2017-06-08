# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models
from odoo.tools import float_compare


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    property_ids = fields.Many2many('mrp.property',
                                    'sale_order_line_property_rel', 'order_id',
                                    'property_id', 'Properties', readonly=True,
                                    states={'draft': [('readonly', False)]})

    @api.multi
    def _prepare_order_line_procurement(self, group_id=False):
        vals = super(SaleOrderLine, self)._prepare_order_line_procurement(
            group_id=group_id)
        vals['property_ids'] = [(6, 0, self.property_ids.ids)]
        return vals