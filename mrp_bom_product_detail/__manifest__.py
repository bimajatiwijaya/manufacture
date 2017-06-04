# -*- coding: utf-8 -*-

##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Solutions Libergia inc. (<http://www.libergia.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Bom product details',
    'version': '10.0.1.0.0',
    'author': "Solutions Libergia inc.,Odoo Community Association (OCA)",
    'license': 'GPL-3 or any later version',
    'category': 'Manufacturing',
    'depends': [
        "mrp",
    ],
    'data': [
        'views/mrp_bom_product_details.xml',
    ],
    'auto_install': False,
    'installable': True,
}
