from office365.sharepoint.client_context import ClientContext
from tests import test_team_site_url, test_user_credentials

ctx = ClientContext(test_team_site_url).with_credentials(test_user_credentials)

file_url = "Shared Documents/SharePoint User Guide.docx"
file = ctx.web.get_file_by_server_relative_url(file_url)
file.delete_object().execute_query()
