"""
Demonstrates how to copy a folder within a site
"""
from office365.sharepoint.client_context import ClientContext
from tests import test_team_site_url, test_user_credentials

ctx = ClientContext(test_team_site_url).with_credentials(test_user_credentials)

# uploads a temporary folder first in a Documents library
path = "../../data/report.csv"
file_from = (
    ctx.web.default_document_library().root_folder.files.upload(path).execute_query()
)

# copies the file with a new name into folder
destination_url = "Shared Documents/archive/2002/01"
file_to = file_from.copyto_using_path(destination_url, True).execute_query()
print("Folder has been copied into '{0}'".format(file_to.server_relative_path))

# clean up
file_from.delete_object().execute_query()
file_to.delete_object().execute_query()
