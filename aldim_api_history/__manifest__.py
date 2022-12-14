{
    'name' : 'AldiM API History Receiver',
    'version': '0.1',
    'category': 'API/API',
    'summary': 'Modul to document every API History',
    'depends': ['base','sale'],
    'description': """
Modul Custom AldiM.
===============================================

Modul to document every API History, so tracking problem will be easier
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/aldim_api_history_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}