# -*- coding: utf-8 -*-

{
    'name': 'Odoo Cooperativos',
    
    'sumary': """App para organizar a voluntarios y tienda""",
    
    'description':"""
        Cooperativos el modulo:
        -Organiza voluntarios
        -Tiendas
    """,
    
    'author': 'Luciano guerrero',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',    
    'version': '0.1',
    
    'depends':['base'],
    
    'data': [
        'security/cooperativos_security.xml',
        'security/ir.model.access.csv',
        
        'views/cooperativos_menuitems.xml',
        'views/tarea_views.xml',
        #'views/session_views.xml',
        
    ],
    
    'demo': [
        'demo/cooperativo_demo.xml',
    ],
    
}