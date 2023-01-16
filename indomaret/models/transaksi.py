from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.exceptions import Warning
from odoo import _

class transaksi(models.Model): 
    _name = 'indomaret.transaksi'
    _description = 'New Description'


    name = fields.Selection(string='Nama Kasir', selection=[('rudi', 'Rudi'), ('junaedi', 'Junaedi'),('silvi', 'Silvia')], required=True)
    date_time = fields.Datetime(string='Waktu Penjualan',  default=fields.datetime.now())
    transaksi_ids = fields.One2many(comodel_name='indomaret.detailtransaksi', inverse_name='transaksi_id', string='Transaksi', required=True)
    total_pembayaran = fields.Float(compute='_compute_total_pembayaran', string='Total pembayaran')
    uang_masuk = fields.Float(string='Uang Masuk')
    uang_kembalian = fields.Float(compute='_compute_uang_masuk', string='Uang Kembalian')
    state = fields.Selection(string='status', selection=[('draft', 'Draft'), ('confirm', 'Confirm'), ('cancelled','Cancelled'), ('done','Done')], required=True, readonly=True, default='draft')

    def action_confirm(self):
        self.write({'state': 'confirm'}) 

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancelled(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})


    
    @api.depends('transaksi_ids')
    def _compute_total_pembayaran(self):
        #untuk menampilkan total yang harus di bayar dari semua pembelanjaan
        amount_total = 0
        for line in self.transaksi_ids:
            amount_total = amount_total + line.total_harga
        self.total_pembayaran = amount_total
          
    @api.depends('total_pembayaran', 'uang_masuk')
    #untuk menampilkan total uang kembalian
    def _compute_uang_masuk(self):
        self.uang_kembalian = self.uang_masuk - self.total_pembayaran

    @api.ondelete(at_uninstall =False)
    def _ondelete_penjualan(self):
    # stok bertambah apabila pembelian di batalkan
        if self.filtered(lambda line: line.state != 'draft'):
            raise UserError('Mohon maaf data yang anda tuju tidak dapat di hapus karena status sudah bukan DRAFT')
        else:
            if self.transaksi_ids:
                b = []
                for rec in self:
                    b = self.env['indomaret.detailtransaksi'].search([("transaksi_id", '=', rec.id)])
                    # b.product_id.stock = b.product_id.stock + b.qty
                    for ob in b:    
                        ob.product_id.stock = ob.product_id.stock + ob.qty

    def write(self,vals):
        # memperbaharui stok barang apabila ada yang di edit dan menambah barang baru
        for rec in self:
            a = self.env['indomaret.detailtransaksi'].search([("transaksi_id", '=', rec.id)]) 
            print(a)
            for data in a:
                print(str(f'{data.product_id.name} {data.qty}'))
                data.product_id.stock = data.product_id.stock + data.qty
        record = super(transaksi,self).write(vals)
        for rec in self:
            b = self.env['indomaret.detailtransaksi'].search([("transaksi_id", '=', rec.id)]) 
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(f'{databaru.product_id.name} {databaru.qty}'))
                    databaru.product_id.stock = databaru.product_id.stock - databaru.qty
                else:
                    pass
        return record

        
    @api.constrains('uang_masuk','uang_kembalian')
    # muncul peringatan apabila uang masuk kosong atau uang masuk masih kurang
    def _constrains_uangmasuk(self):
        if self.uang_kembalian < 0.00:
            raise UserError(_('Jumlah uang masuk kurang dari jumlah yang harus di bayar'))
        else:
            pass
            
                

    
class detailtransaksi(models.Model):
    _name = 'indomaret.detailtransaksi'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    transaksi_id = fields.Many2one(comodel_name='indomaret.transaksi', string='Transaksi')
    product_id = fields.Many2one(comodel_name='indomaret.barang', string='Produk')
    harga_satuan = fields.Float(compute="compute_hargasatuan", string='harga satuan')
    total_harga = fields.Float(compute="compute_totalharga", string='Total Harga')
    qty = fields.Integer(string='Quantity')


    # def _compute_coba1(self):
    #    for line in self.stock_pack_operation_ids:
    #     line.penaltii = self.penalty
    
    @api.onchange('total_harga', 'qty', 'harga_satuan')
    def compute_totalharga(self):
        for rec in self:
            rec.total_harga = rec.qty * rec.harga_satuan

    @api.depends('harga_satuan', 'product_id')
    # mencocokan harga
    def compute_hargasatuan(self):
         for rec in self:
            rec.harga_satuan = rec.product_id.price

    @api.model
    def create(self,vals):
    # stock berkurang apabila ada pembelian
        record =  super(detailtransaksi,self).create(vals)
        if record.qty:
            self.env['indomaret.barang'].search([("id", '=', record.product_id.id)]).write({'stock' : record.product_id.stock - record.qty})
        return record

    @api.constrains('qty')
    # membuat peringatan apabila pembelian melebihi stock
    def _constrains_warning(self):
        for rec in self:
            if rec.qty < 1:
                raise UserError(_(f'Masukan jumlah pembelian pada barang {rec.product_id.name}'))
            elif (rec.qty > rec.product_id.stock):
                    raise UserError(_(f'Pembelian {rec.product_id.name} Melebihi Stock Yang Ada'))

       
        

 

    # stok berkurang apabila ada pembelian (aman) -> masih ada yang harus di perbaiki pada saat batal pembelian di hapus semua barang. (aman)
    # membuat state (aman)
    # requird file (aman)
    # membuat peringatan apabila pembelian melebihi stock (aman)
    # apabila pembelian batal stok akan bertambah kembali (aman)
    # default qty
    # membuat laporan bentuk pdf



    
    



    

    
   
    
  # a = self.env['indomaret.detailtransaksi'].search([('transaksi_id', '=', rec.id)]).mapped('total_harga')
            # rec.total_pembayaran = a


   # @api.onchange('qty')
    # def _compute_stock(self):
        # if self.qty:
        #     self.product_id.stock = self.product_id.stock - self.qty (detail tarnsaksi)



 
    # @api.constrains('product_id','qty')
    # # membuat peringatan apabila pembelian melebihi stock
    # def _onchange_warning(self):
    #     if self.qty:
    #         if self.qty > self.product_id.stock:
    #             raise UserError(_('Pembelian Melebihi Stock Yang Ada'))
    #         elif (self.qty < 1):
    #             raise UserError(_('Psaadaadwad'))

    