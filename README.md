install# Twitter AI Agent

An intelligent agent for automated Twitter engagement using AI language models. Create AI-powered tweets and engage with your audience through smart replies.

## Features

- 🤖 AI-powered tweet generation based on configurable prompts
- 💬 Automated replies to users in specified Twitter lists
- ⚙️ YAML-based configuration for easy customization

## Quick Start
1. Install [ollama](https://ollama.com)
2. Install python3 (version 3.10)
3. install poetry
4. Run `ollama run {model_name}`
5. Update configs (agent/config.yaml). Fill all the configs that were not filled
6. Run `poetry install`
7. Run `twitter --config='{path_to_your_config_file}'` 

## Roadmap

### Q2 2024
- 🔍 RAG integration for context-aware responses
  - PostgreSQL + pgvector for tweet storage
  - Semantic search capabilities
  - Historical context integration
- 🔑 Official Twitter API support
  - OAuth 2.0 authentication
  - Webhook support for real-time events
- 🤖 Additional AI providers
  - OpenRouter integration
  - Claude API support
  - Local LLM support

### Q3 2024
- 📈 Advanced analytics dashboard
- 🎯 Audience segmentation
- 🔄 A/B testing framework
- 🌐 Multi-account support

### Q4 2024
- 🎨 Custom UI for management
- 📱 Mobile app integration
- 🔒 Enterprise security features
- 🌍 Internationalization

## Architecture

```
src/
├── bot/
│   ├── poster_bot.py
├── llm/
│   ├── model.py
│   ├── ollama_generator.py
│   └── service.py
├── rag/
│   ├── model.py
│   ├── storage.py
│   └── service.py
├── config.yaml
└── main.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
