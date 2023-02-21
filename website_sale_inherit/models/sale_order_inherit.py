from odoo import _, api, fields, models


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'


    promo = fields.Selection(string='Promo', selection=[('10', '10%'), ('15', '15%'), ('25', '25%'),])
    after_disc = fields.Float(string='After Diskon')

    @api.onchange('promo','list_price')
    def after_disc_onchange(self):
        for rec in self:
            disc = rec.list_price * int(rec.promo)/100
            rec.after_disc = rec.list_price - disc

    # @api.onchange('total_harga', 'qty', 'harga_satuan')
    # # total auto fill apabila sudah memasukan harga satuan 
    # def compute_totalharga(self):
    #     for rec in self:
    #         rec.total_harga = rec.qty * rec.harga_satuan
    
    
    

    
    
