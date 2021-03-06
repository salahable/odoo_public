# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import pooler, SUPERUSER_ID
from openupgrade import openupgrade
from openupgrade.openupgrade_70 import set_partner_id_from_partner_address_id as fix_partner

drop_cols = [('mrp_bom', 'product_tmpl_id')]


@openupgrade.migrate()
def migrate(cr, version):
    """
    * Create mail aliases for crm case section,
    * Load xml data (Mail alias and updates to CRM stages)
    * Change categ_id to many to many
    """
    openupgrade.drop_columns(cr, drop_cols)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
