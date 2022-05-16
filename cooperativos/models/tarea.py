# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tarea(models.Model):
    
    _name = 'cooperativos.tarea'
    _description = 'Tarea info'
    
    name = fields.Char(string='Tarea', required=True)
    description = fields.Text(string='Description')
    
    tipo_tarea = fields.Selection(string='Tipo tarea',
                             selection=[('estudiar','Estudiar'),
                                        ('tomar en préstamo libros o devolverlos','Tomar en préstamo libros o devolverlos')],
                            copy=False)
    hora_inicio = fields.Date(string='Fecha de inicio')
    hora_final = fields.Date(string='Fecha de final')
    