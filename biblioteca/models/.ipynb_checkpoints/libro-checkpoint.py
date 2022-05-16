# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Libro(models.Model):
    
    _name = 'biblioteca.libro'
    _description = 'Libro info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    autores = fields.Char(string='Autores')
    editores = fields.Char(string='Editores')
    ano_edicion = fields.Date(string='Año edición')
    isbn = fields.Integer(string='ISBN')
    
    genero = fields.Selection(string='Género',
                             selection=[('aventuras','Aventuras'),
                                        ('ciencia ficción','Ciencia ficción'),
                                       ('cuentos de hadas','Cuentos de hadas'),
                                       ('gótica','Gótica'),
                                       ('policíaca','Policíaca'),
                                       ('romance paranormal','Romance paranormal'),
                                       ('distópica','Distópica'),
                                       ('fantástica','Fantástica'),],
                            copy=False)
    