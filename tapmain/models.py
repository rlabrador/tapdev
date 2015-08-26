# -*- coding: utf-8 -*-
from django.template.defaultfilters import default

from openerp import models, fields, api
from openerp.osv import osv
from openerp import tools
import os
from openerp.tools import image_resize_image

# # region Updater le logo de la société configurée
# class res_company(osv.osv):
#  _inherit="res.company"
#  _name="res.company"
#
#  def init(self, cr):
#    img=open(os.path.join(os.path.dirname(__file__), 'static', 'src', 'img','laguntzaileak.png'), 'rb') .read().encode('base64')
#    cr.execute('UPDATE res_partner SET image=%s WHERE is_company=TRUE', (img,))
#    size = (180, None)
# # endregion

class test(models.Model):
     """
     Cette classe créée est une table de test
     """
     _name = 'tapmain.test'
     name = fields.Char(string='First Name', required=False)
     last_name = fields.Char(string='Last Name', required=False)
     urgent_email = fields.Char(string='Urgent email', required=False)
     emergency_phone1 = fields.Char(string='Emergency Phone1', required=False)
     emergency_phone2 = fields.Char(string='Emergency Phone2', required=False)
     gender = fields.Selection([('m','Garçon'),('f','Fille')],string='Gender', required=False)
     is_active = fields.Boolean(string='IsActive', _defaults=False)
     birth_date = fields.Date(string='BirthDate', required=False)
     #Des dates par défaut sont créés grâce au model (create_uid, create_date,write_uid, write_date)
     #Ces champs sont des FK sur res_users
     #create_date = fields.Date(string='CreateDate')
     #write_date =  fields.Date(string='MyWriteDate')

