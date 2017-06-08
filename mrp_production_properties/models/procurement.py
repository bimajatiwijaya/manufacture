# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    property_ids = fields.Many2many('mrp.property',
                                    'procurement_property_rel',
                                    'procurement_id', 'property_id',
                                    string='Properties')

    # check_bom_exists XXX
    def _prepare_mo_vals(self, bom):
        res = super(ProcurementOrder, self)._prepare_mo_vals(bom)
        return res

    @api.multi
    def make_mo(self):
        res = super(ProcurementOrder, self).make_mo()
        production_obj = self.env['mrp.production']
        for procurement_id, produce_id in res.iteritems():
            procurement = self.browse(procurement_id)
            production = production_obj.browse(produce_id)
            vals = {
                'property_ids': [
                    (6, 0, [x.id for x in procurement.property_ids])
                ]
            }
            production.write(vals)
        return res
