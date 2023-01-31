#jowad al fartousy
from fruitmand import fruitmand
from operator import itemgetter
kg = 'kg'
fruitmand.sort(key=itemgetter('weight'), reverse=True)

for x in fruitmand:
    print(x['name'])
    print(x['weight']/1000,kg)