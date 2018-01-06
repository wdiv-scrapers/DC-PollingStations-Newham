from dc_base_scrapers.common import get_data_from_url
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "https://mapping.newham.gov.uk/ArcGIS/rest/services/Polling_Station_Finder14/MapServer/1/query?text=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=&outFields=OBJECTID%2CPLACE_REFE%2CPLACE_PNAM%2CPLACE_ADD1%2CPLACE_ADD2%2CPLACE_ADD3%2CPLACE_PCOD&f=kmz"
districts_url = "https://mapping.newham.gov.uk/ArcGIS/rest/services/Polling_Station_Finder14/MapServer/1/query?text=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=&outFields=OBJECTID%2CPLACE_REFE%2CPLACE_PNAM%2CPLACE_ADD1%2CPLACE_ADD2%2CPLACE_ADD3%2CPLACE_PCOD&f=kmz"
council_id = 'E09000025'


class NewhamHashOnlyScraper(HashOnlyScraper):

    def get_data(self):
        data = get_data_from_url(self.url)
        """
        Newham's API occasionally serves up an error response
        with a 200 OK status code. Handle this error instead of doing this
        https://github.com/wdiv-scrapers/data/blob/3ae9425ba145239b9a9fad4df4ef0c21dddf5044/E09000025/stations.kmz
        """
        if b'does not exist or is inaccessible' in data and b'Invalid URL' in data:
            raise Exception('Bad response')
        return data

stations_scraper = NewhamHashOnlyScraper(stations_url, council_id, 'stations', 'kmz')
stations_scraper.scrape()
districts_scraper = NewhamHashOnlyScraper(districts_url, council_id, 'districts', 'kmz')
districts_scraper.scrape()
