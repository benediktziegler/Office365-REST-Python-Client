"""
Creates a lookup column in a list

https://learn.microsoft.com/en-us/graph/api/list-post-columns?view=graph-rest-1.0
"""

from office365.graph_client import GraphClient
from tests import create_unique_name
from tests.graph_case import acquire_token_by_username_password


def clean_up(columns):
    """
    :type columns: list[office365.onedrive.columns.definition.ColumnDefinition]
    """
    [column.delete_object().execute_query() for column in columns]


client = GraphClient(acquire_token_by_username_password)
lib = client.sites.root.lists["Docs"]

column_name = create_unique_name("LookupColumn")
lookup_column = lib.columns.add_lookup(column_name, lib).execute_query()
print(lookup_column.display_name)

clean_up([lookup_column])
