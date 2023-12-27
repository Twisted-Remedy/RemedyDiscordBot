def getRoute(route):
    all_route_id = {
        'br': 'americas',
        'eune': 'europe',
        'euw': 'europe',
        'jp': 'asia',
        'kr': 'asia',
        'lan': 'americas',
        'las': 'americas',
        'na': 'americas',
        'oce': 'americas',
        'tr': 'europe',
        'ru': 'europe'
    }
    return all_route_id.get(route)

def getRegion(region):
    all_region_id = {
        'br': 'br1',
        'eune': 'eun1',
        'euw': 'euw1',
        'jp': 'jp1',
        'kr': 'kr',
        'lan': 'la1',
        'las': 'la2',
        'na': 'na1',
        'oce': 'oc1',
        'tr': 'tr1',
        'ru': 'ru'
    }
    return all_region_id.get(region)