# -*- coding: utf-8 -*-
from odoo import models, api, exceptions

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def search(self, args, offset=0, limit=None, order=None):
        # Vérifie si l'utilisateur a les droits d'administrateur
        if not self.env.user.has_group('point_of_sale.group_pos_manager'):
            raise exceptions.AccessError("Accès refusé : vous n'avez pas les droits nécessaires pour consulter les commandes.")
        return super(PosOrder, self).search(args, offset=offset, limit=limit, order=order)
