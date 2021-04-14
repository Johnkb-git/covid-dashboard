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
