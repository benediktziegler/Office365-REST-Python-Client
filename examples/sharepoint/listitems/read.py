from office365.sharepoint.client_context import ClientContext
from tests import test_client_credentials, test_team_site_url

ctx = ClientContext(test_team_site_url).with_credentials(test_client_credentials)
tasks_list = ctx.web.lists.get_by_title("Company Tasks")
items = tasks_list.items.get().execute_query()
for item in items:
    print("{0}".format(item.properties.get("Title")))
