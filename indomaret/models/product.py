
from odoo import api, fields, models

from odoo.exceptions import UserError
from odoo.exceptions import Warning
from odoo import _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORM
from datetime import timedelta



class indomaretproduct(models.Model):
    _name = 'indomaret.barang'
    _description = 'model.technical.name'

    name = fields.Char(string='Nama Produk')
    stock = fields.Integer(string='Stok Produk')
    price = fields.Float(string='Harga Produk')
    products_ids = fields.One2many(comodel_name='indomaret.detailtransaksi', inverse_name='product_id', string='Produk')
    target_date = fields.Datetime(string='Tanggal Masuk')

   
  
    


    # @api.onchange('target_date')
    # def onchange_test(self):
    #     datetime_obj = datetime.now()
    #     reduced_time = datetime_obj - timedelta(minutes=5)
    #     if self.target_date: 
    #         if self.target_date < reduced_time:
    #             raise UserError(_('Warning You Must Set date now'))
    
    # @api.onchange('target_date')
    # def onchange_test(self):
    #     if self.target_date:
    #         date = datetime.strptime(self.target_date, '%Y-%m-%d %H:%M:%S')
    #         target_date = date.date()
    #         today = fields.Date.today()
    #         if str(target_date) < today:
    #             raise UserError('Warning You Must Set date now')
        

    

    
    








    