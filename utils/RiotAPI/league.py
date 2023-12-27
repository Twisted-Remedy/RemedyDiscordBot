from requests import session

# // #
from utils.RiotAPI.routing import getRegion

class League:
    def __init__(self, api_key: str = None):
        self._api_key = api_key
        self._session = session()

        ## All Champion Data
        self._champion_data = self._session.get("https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/champion.json").json()['data']

    # // # Data Dragon
    def IDToName(self, idx):
        name_id = {}
        for i in self._champion_data:
            name_id[i] = int(self._champion_data[i]['key'])
        return list(name_id.keys())[list(name_id.values()).index(idx)]

    def NameToID(self, name):
        name_id = {}
        for i in self._champion_data:
            name_id[i] = int(self._champion_data[i]['key'])
        return name_id[name]

    # // # Summoner-V4
    def SummonerInfoByName(self, region, name):
        region = getRegion(region)
        build_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
        return self._session.get(build_url, headers={"X-Riot-Token": self._api_key}).json()

    # // # Champion-Mastery-V4
    def MasteriesByName(self, region, name):
        encryptedPUUID = self.SummonerInfoByName(region, name)['puuid']
        region = getRegion(region)
        build_url = f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}"
        return self._session.get(build_url, headers={"X-Riot-Token": self._api_key}).json()

    def MasteriesByNameByChamp(self, region, name, champion):
        idx = self.NameToID(champion.title())
        encryptedPUUID = self.SummonerInfoByName(region, name)['puuid']
        region = getRegion(region)
        build_url = f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}/by-champion/{idx}"
        return self._session.get(build_url, headers={"X-Riot-Token": self._api_key}).json()