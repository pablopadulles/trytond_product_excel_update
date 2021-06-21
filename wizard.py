from trytond.model import (
    ModelView, ModelSQL, MatchMixin, DeactivableMixin, fields,
    sequence_ordered, Exclude)
from trytond.wizard import Wizard, StateTransition, StateView, StateAction, \
    StateReport, Button
from trytond.pool import Pool
import xlrd
from trytond.transaction import Transaction
from trytond.pyson import Eval, If, Bool, Not
from decimal import Decimal



class ActualizarProductosView(ModelView):
    'Actualizar Precios'
    __name__ = 'product.excel.update.view'

    excel = fields.Binary('Excel', states={'required': True})


class ActualizarProductosWizard(Wizard):
    'Actualizar Productos Wizard'
    __name__ = 'product.excel.update.wizard'

    start = StateView('product.excel.update.view',
        'product_excel_update.product_excel_update_view', [
            Button('Cancel', 'end', ''),
            Button('OK', 'actualizar', '', default=True),
            ])

    actualizar = StateTransition()

    def transition_actualizar(self):
        Product = Pool().get('product.product')
        ProductTemplate = Pool().get('product.template')
        book = xlrd.open_workbook(file_contents=self.start.excel)
        if len(book.sheets()) >= 1:
            hoja1 = book.sheet_by_name('Productos')
            for i in range(2, hoja1.nrows):
                linea = hoja1.row_values(i)
                if linea[3] == 'SI':
                    productos = Product.search([
                            ('id', '=', linea[4]),
                    ])
                    if linea[1]:
                        if linea[1].is_integer():
                            precio = Decimal(linea[1])
                        else:
                            precio = Decimal(str(linea[1])).quantize(Decimal('.01'))
                    else:
                        precio = Decimal(0).quantize(Decimal('.01'))
                    if productos:
                        Product.write(productos, {
                            'precio_lista': precio,
                        })
                else:
                    productos = ProductTemplate.search([
                            ('id', '=', linea[4]),
                    ])
                    if linea[1]:
                        if linea[1].is_integer():
                            precio = Decimal(linea[1])
                        else:
                            precio = Decimal(str(linea[1])).quantize(Decimal('.01'))
                    else:
                        precio = Decimal(0).quantize(Decimal('.01'))
                    if productos:
                        ProductTemplate.write(productos, {
                            'list_price': precio,
                        })

        return 'end'