# Future Imports for py2/3 backwards compat.
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import range
import nexpose as nexpose
from nexpose import NexposeSession, as_string
from future import standard_library
import http.client
standard_library.install_aliases()

nexpose.SKIP_SSL_VERIFY = True
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

host = "localhost"
port = 3780
username = "nxadmin"
password = "nxadmin"

session = nexpose.NexposeSession.CreateAndOpen(host, port, username, password)

for asset in session.GetAssetSummaries():
    asset_details = session.GetAssetDetails(asset.id)
    print("Host: {} | Names: {} | Site: {} | Risk: {} | Vulns: {}".format(
            asset.host,
            asset_details.host_names,
            asset.site_id,
            asset.risk_factor,
            asset_details.vulnerability_instances
        )
    )
