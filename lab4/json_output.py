import json
file = open("lab4\JSON\sample-data.json ")
sample_data = json.load(file)

output = "Interface Status \n================================================================================\nDN                                                 Description           Speed    MTU\n-------------------------------------------------- --------------------  ------  ------\n"

for i in sample_data['imdata']:
    attributes = i['l1PhysIf']['attributes']
    dn = attributes['dn']
    descr = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')

    output += f"{dn:50} {descr:20} {speed:7} {mtu:6}\n"

print(output)

