# Ollama Python Library

The Ollama Python library provides the easiest way to integrate Python 3.8+ projects with [Ollama](https://github.com/ollama/ollama).

## Prerequisites

- [Ollama](https://ollama.com/download) should be installed and running
- Pull a model to use with the library: `ollama pull <model>` e.g. `ollama pull llama3.1`
  - See [Ollama models](https://ollama.com/models) for more information on the models available.

## Install

```sh
pip install ollama
```

## Usage

```python
from ollama import chat
from ollama._types import ChatResponse

response: ChatResponse = chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
```

See [_types.py](ollama/_types.py) for more information on the response types.

## Streaming responses

Response streaming can be enabled by setting `stream=True`

Streaming Tool/Function calling is not yet supported.

```python
from ollama import chat

stream = chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
```

## Custom client

A custom client can be created with the following fields:

- `host`: The Ollama host (default: `http://localhost:11434`)
- `timeout`: The timeout for requests (default: `None`)
- `follow_redirects`: Whether to follow redirects (default: `True`)
- `headers`: Additional headers to send with requests (default: `{}`)

```python
from ollama import Client
client = Client()
# or 
client = Client(
  host='http://localhost:11434',
  timeout=None,
  follow_redirects=True,
  headers={'x-some-header': 'some-value'}
)
response = client.chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
```

## Async client

The `AsyncClient` class is used to make asynchronous requests. It can be configured with the same fields as the `Client` class.

```python
import asyncio
from ollama import AsyncClient

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  response = await AsyncClient().chat(model='llama3.1', messages=[message])

asyncio.run(chat())
```

Setting `stream=True` modifies functions to return a Python asynchronous generator:

```python
import asyncio
from ollama import AsyncClient

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  async for part in await AsyncClient().chat(model='llama3.1', messages=[message], stream=True):
    print(part['message']['content'], end='', flush=True)

asyncio.run(chat())
```

## API

The Ollama Python library's API is designed around the [Ollama REST API](https://github.com/ollama/ollama/blob/main/docs/api.md)

### Chat

```python
ollama.chat(model='llama3.1', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])
```

### Generate

```python
ollama.generate(model='llama3.1', prompt='Why is the sky blue?')
```

### List

```python
ollama.list()
```

### Show

```python
ollama.show('llama3.1')
```

### Create

```python
modelfile='''
FROM llama3.1
SYSTEM You are mario from super mario bros.
'''

ollama.create(model='example', modelfile=modelfile)
```

### Copy

```python
ollama.copy('llama3.1', 'user/llama3.1')
```

### Delete

```python
ollama.delete('llama3.1')
```

### Pull

```python
ollama.pull('llama3.1')
```

### Push

```python
ollama.push('user/llama3.1')
```

### Embed

```python
ollama.embed(model='llama3.1', input='The sky is blue because of rayleigh scattering')
```

### Embed (batch)

```python
ollama.embed(model='llama3.1', input=['The sky is blue because of rayleigh scattering', 'Grass is green because of chlorophyll'])
```

### Ps

```python
ollama.ps()
```


## Errors

Errors are raised if requests return an error status or if an error is detected while streaming.

```python
model = 'does-not-yet-exist'

try:
  ollama.chat(model)
except ollama.ResponseError as e:
  print('Error:', e.error)
  if e.status_code == 404:
    ollama.pull(model)
```
