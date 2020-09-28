broker_url='amqp://clips:clips@127.0.0.1:5672/clips'
result_backend='arangodb://clips:clips@127.0.0.1:8529/clips/results'
imports=(
    'corec.endpoints',
)
