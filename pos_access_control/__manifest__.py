# -*- coding: utf-8 -*
{
    'name': 'POS Access Control',
    'version': '1.0',
    'depends': ['point_of_sale'],
    'data': [
        'views/views.xml',
        'static/src/js/pos_access_control.js',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        #'static/src/xml/pos_access_control.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_access_control/static/src/js/pos_access_control.js',
        ],
    },

    'installable': True,
    'application': True,
}

