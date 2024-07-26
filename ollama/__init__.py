from ollama._client import Client, AsyncClient
from ollama._types import (
  GenerateResponse,
  ChatResponse,
  ProgressResponse,
  Message,
  Options,
  RequestError,
  ResponseError,
)
from ollama.tool_calling import * 

__all__ = [
  'Client',
  'AsyncClient',
  'GenerateResponse',
  'ChatResponse',
  'ProgressResponse',
  'Message',
  'Options',
  'ToolRegistry',
  'RequestError',
  'ResponseError',
  'ToolRegisteredError',
  'ToolNotRegisteredError',
  'ParseError',
  'generate',
  'chat',
  'embed',
  'embeddings',
  'pull',
  'push',
  'create',
  'delete',
  'list',
  'copy',
  'show',
  'ps',
]

_client = Client()

generate = _client.generate
chat = _client.chat
embed = _client.embed
embeddings = _client.embeddings
pull = _client.pull
push = _client.push
create = _client.create
delete = _client.delete
list = _client.list
copy = _client.copy
show = _client.show
ps = _client.ps
