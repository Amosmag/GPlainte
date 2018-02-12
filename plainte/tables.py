from .models import Plainte
from table import Table
from table.columns import Column


class PlainteTable(Table):
    nom = Column(field='nom')
    prenoms = Column(field='prenoms')
    email = Column(field='email')

    class Meta:
        model = Plainte
        ajax = True
        #ajax_source = reverse_lazy('table_data')
