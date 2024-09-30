from odoo import http
from odoo.http import request

class PosController(http.Controller):

    @http.route('/pos/orders', type='http', auth='user')
    def get_orders(self):
        if not request.env.user.has_group('point_of_sale.group_pos_manager'):
            return request.not_found()  # Ou redirigez vers une page d'erreur
        # Logique pour récupérer et afficher les commandes
