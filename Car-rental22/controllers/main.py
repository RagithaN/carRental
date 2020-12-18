# -*- coding: utf-8 -*-

import random
import werkzeug

from odoo.http import Controller, request, route


class TripController(Controller):

    # Generic display pages
    # --------------------------------------------------

    @route('/hello', type='http', auth="public", website=True)
    def carrental_hello(self, **post):
        return request.render("carrental.carrental_hello", {'name': 'World'})

    @route('/hello2', type='http', auth="public", website=True)
    def carrental_hello2(self, **post):
        return request.render("carrental.carrental_hello2", {'name': 'World'})

   
   
