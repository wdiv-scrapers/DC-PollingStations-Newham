from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "https://mapping.newham.gov.uk/ArcGIS/rest/services/Polling_Station_Finder14/MapServer/1/query?text=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=&outFields=OBJECTID%2CPLACE_REFE%2CPLACE_PNAM%2CPLACE_ADD1%2CPLACE_ADD2%2CPLACE_ADD3%2CPLACE_PCOD&f=kmz"
districts_url = "https://mapping.newham.gov.uk/ArcGIS/rest/services/Polling_Station_Finder14/MapServer/1/query?text=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=OBJECTID+LIKE+%27%25%27&time=&returnCountOnly=false&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=&outFields=OBJECTID%2CPLACE_REFE%2CPLACE_PNAM%2CPLACE_ADD1%2CPLACE_ADD2%2CPLACE_ADD3%2CPLACE_PCOD&f=kmz"
council_id = 'E09000025'


stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations', 'kmz')
stations_scraper.scrape()
districts_scraper = HashOnlyScraper(districts_url, council_id, 'districts', 'kmz')
districts_scraper.scrape()
