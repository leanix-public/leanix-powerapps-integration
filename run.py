import click
import json


@click.group()
def cli():
    """Command Line Program for developing CNS (e.g. processors)"""
    pass


@cli.command('get-ldif', help="")
def cli_get_ldif():

    f = open('sample.json',)
  
    data = json.load(f)

   
    content = []
    for d in data["value"]:
        print (json.dumps(d, indent=3))
        content.append({"id": d["id"], "type": "Application", "data": {
            "name": d["properties"]["displayName"],
            "region": d["properties"]["azureRegion"],
            "deployedAt": d["properties"]["lastModifiedTime"],
            "addons":  d["properties"]["addons"],
            "clientUris":  d["properties"]["clientUris"],
            "retentionPeriod": d["properties"]["retentionPeriod"],
            "protectionStatus": d["properties"]["protectionStatus"],
            
            
        }})


   

    print(json.dumps({
        "connectorType": "leanix",
        "connectorId": "leanix-powerapps-connector",
        "connectorVersion": "1.0.0",
        "lxVersion": "1.0.0",
        "processingDirection": "inbound",
        "processingMode": "full",
        "customFields": {},
        "content": content
    }, indent=2))



def main():
    cli()


if __name__ == '__main__':
    cli()
