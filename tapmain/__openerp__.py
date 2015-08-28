# -*- coding: utf-8 -*-
{
    'name': "IKASTOLA - LAUETERDI",

    'summary': """
        module de gestion des TAP dans les Ikastolas d'Iparralde""",

    'description': """
        Updated : Ce module se veut d'aider les membres des associations d'Ikastolas afin de gérer les contrats TAP, les relations aux intervenants et les planning.
        Cherchons traducteur en euskara...""",

    'author': "RL",
    'website': "http://hiriondo.free.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Ikastolak',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base','contacts','google_drive','google_calendar','google_spreadsheet'],
    'depends': ['base','contacts','google_drive','website','school'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
        #This will link to a file in the folder data. This file, defaultdata.xml will contain the data that is automatically installed when the module is installed.
	     'data/defaultdata.xml',
        #raoute les entrees dans le menu principal
         'views/contractor_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml'
        #'demo.xml', 'school/demo/school_demo.xml'
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}