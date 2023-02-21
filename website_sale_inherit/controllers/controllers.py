from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class WebsiteSaleInherit(WebsiteSale):
#     @http.route('/website_sale_inherit/website_sale_inherit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_inherit/website_sale_inherit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_inherit.listing', {
#             'root': '/website_sale_inherit/website_sale_inherit',
#             'objects': http.request.env['website_sale_inherit.website_sale_inherit'].search([]),
#         })

#     @http.route('/website_sale_inherit/website_sale_inherit/objects/<model("website_sale_inherit.website_sale_inherit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_inherit.object', {
#             'object': obj
#         })

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True,)
    def shop(self, page=0, category=None, search='', ppg=False, **post, ):
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
        print("hasil inherit")
        return res

    # @http.route('/shop/crate_produk', type="http", auth='user', website="True")
    # def create_produk(self, **kw):
    #     product = request.env['product.template'].search([])
    #     return http.request.render('website_sale_inherit.create_produk',  {
    #          'produk' : product
    #     })

    @http.route('/shop/crate_produk', type="http", auth='user', website="True")
    def create_produk(self, **kw):
        user = request.env.user
        if user.has_group('base.group_portal'):
            return request.render('website_sale_inherit.access_denied')
        else:
            product = request.env['product.template'].search([])
            return http.request.render('website_sale_inherit.create_produk', {
                'produk': product
            })

    @http.route('/shop/webproduk', type="http", auth='user', website="True")
    def create_webproduk(self, **kw): 
        request.env['product.template'].sudo().create(kw)
        return http.request.render('website_sale_inherit.thanks',  {})
        
