{
    'name': "futbol",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modulo de Partidos
    """,

    'author': "Francisco",
    'website': "http://www.Partidosfrancisco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/posiciones.xml',
        'wizards/wizard_posiciones.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
