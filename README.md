# P1 Crew

Welcome to the P1 Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/p1/config/agents.yaml` to define your agents
- Modify `src/p1/config/tasks.yaml` to define your tasks
- Modify `src/p1/crew.py` to add your own logic, tools and specific args
- Modify `src/p1/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the p1 Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The p1 Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the P1 Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.




Error-Principal
****************************
Como puedo resolver este error: The class `Ollama` was deprecated in LangChain 0.3.1 and will be removed in 1.0.0. An updated version of the class exists in the :class:`~langchain-ollama package and should be used instead. To use it run `pip install -U :class:`~langchain-ollama` and import as `from :class:`~langchain_ollama import OllamaLLM``.
  ollama_llm = Ollama(model="ollama/openhermes")


Este error ocurre porque la clase `Ollama` en **LangChain 0.3.1** está obsoleta y se ha movido a un paquete separado llamado `langchain-ollama`. Para solucionarlo, sigue estos pasos:

### **Solución paso a paso:**
1. **Desinstalar la versión antigua (si es necesario)**  
   Si tenías una versión previa de `langchain` que incluía `Ollama`, no es necesario desinstalarla, pero puedes asegurarte de tener la última versión.

2. **Instalar el nuevo paquete `langchain-ollama`**  
   Ejecuta el siguiente comando con **UV** (o `pip` si prefieres):
   ```bash
   uv pip install langchain-ollama
   ```

3. **Actualizar LangChain (opcional pero recomendado)**  
   Asegúrate de que tienes una versión reciente de LangChain:
   ```bash
   uv pip install --upgrade langchain
   ```

4. **Modificar tu código**  
   Cambia la importación y el uso de `Ollama` por la nueva clase `OllamaLLM`:
   ```python
   # Antes (obsoleto)
   # from langchain.llms import Ollama
   # ollama_llm = Ollama(model="ollama/openhermes")

   # Ahora (correcto)
   from langchain_ollama import Ollama
   ollama_llm = Ollama(model="openhermes")  # Nota: "ollama/" ya no es necesario en el nombre del modelo
   ```

   **Nota:**  
   - El modelo ahora se pasa directamente como `"openhermes"` (sin `ollama/`).  
   - Si usas un modelo personalizado o uno que requiere prefijo, consulta la [documentación de langchain-ollama](https://python.langchain.com/docs/integrations/llms/ollama).

5. **Verifica que funcione**  
   Ejecuta tu código nuevamente y el error debería desaparecer.

### **¿Por qué ocurrió esto?**  
LangChain está modularizando sus integraciones para hacer el paquete principal más ligero. Por eso, `Ollama` se movió a `langchain-ollama`.

Si tienes más problemas, verifica:  
- Que no hay conflictos entre `langchain` y `langchain-community` (otro paquete que a veces causa confusiones).  
- Que el modelo `openhermes` está correctamente descargado en tu instancia local de Ollama (usa `ollama pull openhermes` si es necesario).

¿Necesitas ayuda con algo más relacionado con **CrewAI** o **Ollama**? 😊


 
 ***********************************************************************************
  Bonus: Usa Uv también para gestionar el entorno
    Si aún no lo haces, puedes usar Uv también para crear un entorno virtual limpio:

    uv venv
source .venv/bin/activate  # o el equivalente en Windows
uv pip install crewai langchain-ollama

*************************************************************************************