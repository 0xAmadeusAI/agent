"""
package for integrations with LLMs
MUST follow the same interface
For now we have integration with Ollama only
In the nearest future might add integrations with OpenRouter, Claude and OpenAI

Why separate package?
want to abstract away the boilerplate and provide one interface and make it easier to swap integrations

Future implementations of the interface should be in separate {integration_name}_generator.py file
"""