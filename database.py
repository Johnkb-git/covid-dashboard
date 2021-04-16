import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')


def get_medicine(table_name, user_id):
    table = dynamodb.Table(table_name)
    response = table.scan(
        FilterExpression=Attr('use_id').eq(user_id)
    )
    return response
    # print(table.creation_date_time)


def verify_user(user_id, password):
    table = dynamodb.Table("user")
    response = table.get_item(
        Key={
            'user_id': user_id
        }
    )
    if "Item" not in response:
        return False
    item = response['Item']
    if password != item["password"]:
        return False
    return True
