# -*- coding: utf-8 -*-
# Copyright 2014 <alex.comba@agilebg.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models, fields


class MrpPropertyGroup(models.Model):
    """
    Group of mrp properties.
    """
    _name = 'mrp.property.group'
    _description = 'Property Group'

    name = fields.Char('Property Group', required=True)
    description = fields.Text('Description')


class MrpProperty(models.Model):
    """
    Properties of mrp.
    """
    _name = 'mrp.property'
    _description = 'Property'

    name = fields.Char('Name', required=True)
    composition = fields.Selection([('min', 'min'), ('max', 'max'),
                                    ('plus', 'plus')],
                                   'Properties composition', required=True,
                                   help="Not used in computations, "
                                        "for information purpose only.",
                                   default='min')
    group_id = fields.Many2one('mrp.property.group', 'Property Group',
                               required=True)
    description = fields.Text('Description')


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    property_ids = fields.Many2many('mrp.property',
                                    'mrp_bom_property_rel',
                                    'bom_id', 'property_id',
                                    string='Properties')

    @api.model
    def _bom_find(self, product_tmpl=None, product=None, picking_type=None,
                  company_id=False):
        res = super(MrpBom, self)._bom_find(product_tmpl, product,
                                            picking_type, company_id)
        return res
    # _bom_explode XXX
    def explode(self, product, quantity, picking_type=False):
        boms_done, lines_done = super(MrpBom, self).explode(product, quantity, picking_type)
        return boms_done, lines_done


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    property_ids = fields.Many2many('mrp.property',
                                    'mrp_production_property_rel',
                                    'production_id', 'property_id',
                                    string='Properties')
