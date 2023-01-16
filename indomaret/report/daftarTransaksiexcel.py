from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.indomaret.report_transaksi_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()
  
    
    def generate_xlsx_report(self, workbook, data, transaksi):
        sheet = workbook.add_worksheet('Daftar Supplier')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama Kasir', bold)
        sheet.write(1, 1, 'Tanggal Penjualan', bold)
        sheet.write(1, 2, 'Status', bold)
        row = 2
      
        for obj in transaksi:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, str(obj.date_time))
            sheet.write(row, col+2, str(obj.state))
            row += 1
            # for ob in obj.transaksi_ids:  
            #     a = self.env['indomaret.detailtransaksi'].search([("id", '=', ob.product_id.id)])
            #     sheet.write(row, col+3, a.name)   