# Assistente de Delivery com AWS Step Functions e Amazon Bedrock

## Visão Geral

O projeto "Assistente de Delivery" é uma solução que utiliza **AWS Step Functions** para orquestrar o fluxo de trabalho de gerenciamento de pedidos de entrega e **Amazon Bedrock** para processar e interpretar interações baseadas em linguagem natural. Este assistente visa automatizar e otimizar o processo de criação, monitoramento e gerenciamento de pedidos de entrega, melhorando a eficiência e a experiência do cliente.

## Arquitetura do Projeto

O assistente de delivery é composto pelos seguintes componentes principais:

1. **AWS Step Functions**: Orquestra o fluxo de trabalho de entrega, coordenando diferentes tarefas envolvidas no processamento de pedidos.
2. **Amazon Bedrock**: Processa consultas e interações dos clientes com base em modelos avançados de linguagem natural.
3. **AWS Lambda**: Executa funções específicas, como integração com sistemas de rastreamento, atualização de status e notificações.
4. **Amazon SNS (Simple Notification Service)**: Envia notificações sobre o status das entregas.
5. **Amazon DynamoDB**: Armazena dados de pedidos e status.

## Componentes e Funções

### 1. **AWS Step Functions**

Configurações de workflow usando Amazon States Language (ASL):

```json
{
  "Comment": "Assistente de Delivery",
  "StartAt": "ReceberPedido",
  "States": {
    "ReceberPedido": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:ReceberPedidoFunction",
      "Next": "ValidarPedido"
    },
    "ValidarPedido": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:ValidarPedidoFunction",
      "Next": "AtualizarStatus"
    },
    "AtualizarStatus": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:AtualizarStatusFunction",
      "Next": "NotificarCliente"
    },
    "NotificarCliente": {
      "Type": "Task",
      "Resource": "arn:aws:sns:REGION:ACCOUNT_ID:DeliveryNotification",
      "End": true
    }
  }
}
