import os
from notion_client import Client
from constants import NOTION_API_TOKEN
from constants import NOTION_DATABASE_ID
from pprint import pprint

notion = Client(auth=NOTION_API_TOKEN)

my_page = notion.databases.query(
    **{
        "database_id": NOTION_DATABASE_ID,
    }
)

for result in my_page["results"]:
    pprint(result.keys())

def create_notion_page(page_name):
    response = notion.pages.create( 
        **{
            "cover": {
        "type": "external",
        "external": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
        }
    },
    "icon": {
        "type": "emoji",
        "emoji": "🥬"
    },
    "parent": {
        "type": "database_id",
        "database_id": NOTION_DATABASE_ID
    },
    "properties": {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": page_name
                    }
                }
            ]
        },
    },
    "children": [
        {
            "object": "block",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Lacinato kale"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "paragraph": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                            "link": {
                                "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                            }
                        },
                        "href": "https://en.wikipedia.org/wiki/Lacinato_kale"
                    }
                ],
                "color": "default"
            }
        }]}
    )
    pprint(response)

create_notion_page("Test")