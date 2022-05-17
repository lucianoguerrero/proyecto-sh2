# -*- coding: utf-8 -*-

{
    'name': 'Odoo Misión espacial',
    
    'sumary': """App para llegar a la luna""",
    
    'description':"""
        Misión espacial el modulo:
        -Nave espacial
        -Tripulación
    """,
    
    'author': 'Luciano guerrero',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',    
    'version': '0.1',
    
    'depends':['base'],
    
    'data': [
        'security/mision_espacial_security.xml',
        'security/ir.model.access.csv',
        
        'views/mision_espacial_menuitems.xml',
        'views/nave_espacial_views.xml',
        #'views/session_views.xml',
        
    ],
    
    'demo': [
        'demo/nave_espacial_demo.xml',
    ],
    
    'license':'OPL-1',
}