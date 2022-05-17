# -*- coding: utf-8 -*-

{
    'name': 'Odoo biblioteca',
    
    'sumary': """App para administrar libros y clientes""",
    
    'description':"""
        Biblioteca el modulo:
        -Libros
        -Clientes
    """,
    
    'author': 'Luciano guerrero',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',    
    'version': '0.1',
    
    'depends':['base'],
    
    'data': [
        'security/biblioteca_security.xml',
        'security/ir.model.access.csv',
        
        'views/biblioteca_menuitems.xml',
        #'views/course_views.xml',
        #'views/session_views.xml',
        
    ],
    
    'demo': [
        'demo/libro_demo.xml',
    ],
    
}