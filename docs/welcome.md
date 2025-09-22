### Welcome to the Workshop!
This 1/2 day workshop will cover using Generative AI with FOLIO. We will be using Large Language 
Models, such as ChatGPT or Claude, with FOLIO's [APIs](https://dev.folio.org/reference/api/).

While optional, we will be using [Jupyter Notebooks](https://jupyter.org/) for certain 
topics. To install Jupyter follow these steps:

1. Install [uv][UV]
1. If you have [git](https://git-scm.com/) installed, you can also clone the following repositories:
    1. `git clone https://github.com/sul-dlss-labs/wolfcon-2025-ai-workshop.git`
    1. `git clone https://github.com/folio-labs/edge-ai.git`
1. You can also download the Workshop repository as a [zip file](https://github.com/sul-dlss-labs/wolfcon-2025-ai-workshop/archive/refs/heads/main.zip) and extract the repository,
1. Change directories to the Workshop repository: `cd wolfcon-2025-ai-workshop`
1. Create an `.env` file like the following:

```
export OPENAI_API_KEY={your_openai_key}
export GATEWAY_URL=https://folio-snapshot-okapi.dev.folio.org
export TENANT_ID=diku
export ADMIN_USER=diku_admin
export ADMIN_PASSWORD=admin
```
1. Run `uv sync`
1. Now you can launch Jupyter with `uv run jupyter lab` that should then be accessable at `http://localhost:8888`

**Note:** Generative AI was used in copyediting topics

[UV]: https://docs.astral.sh/uv/
