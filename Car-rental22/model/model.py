from odoo import api, fields, models, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.exceptions import UserError

class cars(models.Model):
    _name ='carrental.cars'
    _description = 'carrental cars'
    cid=fields.Integer("car Number",required=True)
    owner_name = fields.Char("name", required=True, )
    make=fields.Char("make", required=True, )
    year_of_manufacture=fields.Integer("year",required=True)
    bookings_count=fields.Integer(compute='_compute_bookings_count', store=True,string="total bookings")
    def open_bookings_ofthe_car(self):
      return {
      	carrental.bookings;
      
      }
    
     
