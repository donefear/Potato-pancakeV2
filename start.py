from airtable import Airtable
from Lib import Base
base_key = 'applLavo9RpSwqvrS'
table_name = 'Social Content Calendar'

print("fuck this shit i'm out")
airtable = Airtable(base_key, table_name, api_key='key5sPiXSqrA7KE9r')
info = airtable.get_all()
DictInfo = info[0]
Fields = DictInfo.get('fields')

Base.main(info)
