# -*- coding: utf-8 -*-
# Copyright 2014 <alex.comba@agilebg.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    property_ids = fields.Many2many('mrp.property',
                                    'mrp_production_property_rel',
                                    'production_id', 'property_id',
                                    string='Properties')


class ProcurementOrder(models.Model):
    _inherit = "procurement.order"

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
