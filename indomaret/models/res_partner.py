from odoo import api, fields, models


class karyawan(models.Model):
    _inherit = 'res.partner'

    poin = fields.Integer(string='Poin')




    
