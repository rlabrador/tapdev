# -*- coding: utf-8 -*-
{
    'name': "IKASTOLA - LAUETERDI",

    'summary': """
        module de gestion des TAP dans les Ikastolas d'Iparralde""",

    'description': """
        Updated : Ce module se veut d'aider les membres des associations d'Ikastolas afin de gérer les contrats TAP, les relations aux intervenants et les planning.
        Cherchons traducteur en euskara...""",

    'author': "RL",
    'website': "http://www.baionako_ikastola_polobeyris.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Ikastolak',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base','contacts','google_drive','google_calendar','google_spreadsheet'],
    'depends': ['base','contacts','google_drive'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
        #This will link to a file in the folder data. This file, defaultdata.xml will contain the data that is automatically installed when the module is installed.
	     'data/defaultdata.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml'
    ],
}