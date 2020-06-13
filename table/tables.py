import django_tables2 as tables
from table.models import TableData

class TableDataTable(tables.Table):
    class Meta:
        model = TableData
        fields = ('user_id','username','contact','primary_role','additional_role','school_id','school_name','block_name','district_name','dise_code')
        attrs = {'id':'emp_table'}