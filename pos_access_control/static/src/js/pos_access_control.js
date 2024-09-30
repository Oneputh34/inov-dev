odoo.define('pos_access_control', function (require) {
    "use strict";

    var screens = require('point_of_sale.screens');
    var gui = require('point_of_sale.gui');

    // Intercepter l'accès à l'écran des commandes
    var OrdersScreenWidget = screens.OrdersScreenWidget.include({
        show: function () {
            // Vérifier si l'utilisateur a les droits d'accès
            if (!this.pos.user_has_group('point_of_sale.group_pos_manager')) {
                // Afficher un message d'erreur et revenir à l'écran principal
                this.gui.show_popup('confirm', {
                    title: 'Accès refusé',
                    body: 'Vous n\'avez pas l\'autorisation d\'accéder aux commandes.',
                });
                this.gui.back(); // Revenir à l'écran précédent
            } else {
                this._super();
            }
        },
    });
});
