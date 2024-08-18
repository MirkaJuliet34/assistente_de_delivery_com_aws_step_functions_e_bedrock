import boto3

bedrock_client = boto3.client('bedrock', region_name='REGION')

def processar_consulta_cliente(consulta):
    response = bedrock_client.invoke_model(
        ModelId='bedrock-model-id',
        Content=consulta
    )
    return response['Body'].read().decode('utf-8')
