# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NaveEspacial(models.Model):
    
    _name = 'mision_espacial.nave_espacial'
    _description = 'Nave espacial info'
    
    name = fields.Char(string='Nombre del cohete', required=True)
    
    combustible = fields.Selection(string='Combustible',
                             selection=[('hidracina','Hidracina'),
                                        ('tetróxido de nitrógeno','Tetróxido de nitrógeno')],
                            copy=False)
    
    tipo_barco = fields.Selection(string='Tipo barco',
                             selection=[('vehículos lanzadera','Vehículos lanzadera'),
                                        ('naves no tripuladas o robóticas','naves no tripuladas o robóticas'),
                                       ('naves espaciales tripuladas','Naves espaciales tripuladas')],
                            copy=False)
    
    n_pasajeros = fields.Integer(string='Numero pasajeros')
    active = fields.Boolean(string='Activo', default=True)