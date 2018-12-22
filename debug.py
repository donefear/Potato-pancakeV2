from airtable import Airtable
base_key = 'applLavo9RpSwqvrS'
table_name = 'Social Content Calendar'

print("fuck this shit i'm out")
airtable = Airtable(base_key, table_name, api_key='key5sPiXSqrA7KE9r')
info = airtable.get_all(sort='Go Live Date/Time', max_records=5)
DictInfo = info[0]
print("-----------info------------")
print(info)
print("---------KeyNames-----------")
PostTime = DictInfo.get('Go Live Date/Time')
for x in DictInfo:
    print(x)
Fields = DictInfo.get('fields')
for x in Fields:
    print(x)
print("--------Field go live--------")
for event in info:
    Fieldz = event.get('fields')
    GEvent = Fieldz["Go Live Date/Time"]
    print(GEvent)



# print (info)
# print("--------------------------")
# print (PostTime)
