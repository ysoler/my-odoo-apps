# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (C) 2004-2012 OpenERP S.A. (<http://openerp.com>).
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

from openerp import models,fields

class ZopimConfiguration(models.TransientModel):
    _name = 'zopim.config.settings'
    _inherit = 'res.config.settings'

    key = fields.Char('Zopim Live Chat Key', required=True)
    color_primary = fields.Char('Primary Color', required=False)
    color_badge = fields.Char('Badge Color', required=False)
    
    def get_default_key(self, cr, uid, ids, context=None):
        key = self.pool.get("ir.config_parameter").get_param(cr, uid, "zopim_live_chat.key", default=None, context=context)
        return {'key': key or False}
        
    def set_key(self, cr, uid, ids, context=None):
        config_parameters = self.pool.get("ir.config_parameter")
        for record in self.browse(cr, uid, ids, context=context):
            config_parameters.set_param(cr, uid, "zopim_live_chat.key", record.key or False, context=context)

    def get_default_color_primary(self, cr, uid, ids, context=None):
        color_primary = self.pool.get("ir.config_parameter").get_param(cr, uid, "zopim_live_chat.color_primary", default=None, context=context)
        return {'color_primary': color_primary or False}
        
    def set_color_primary(self, cr, uid, ids, context=None):
        config_parameters = self.pool.get("ir.config_parameter")
        for record in self.browse(cr, uid, ids, context=context):
            config_parameters.set_param(cr, uid, "zopim_live_chat.color_primary", record.color_primary or False, context=context)

    def get_default_color_badge(self, cr, uid, ids, context=None):
        color_badge = self.pool.get("ir.config_parameter").get_param(cr, uid, "zopim_live_chat.color_badge", default=None, context=context)
        return {'color_badge': color_badge or False}
        
    def set_color_badge(self, cr, uid, ids, context=None):
        config_parameters = self.pool.get("ir.config_parameter")
        for record in self.browse(cr, uid, ids, context=context):
            config_parameters.set_param(cr, uid, "zopim_live_chat.color_badge", record.color_badge or False, context=context)

