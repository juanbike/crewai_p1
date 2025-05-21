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




CrewAI
CrewAI
Primeros pasos con CrewAI: Crea tu primera tripulación
Una guía paso a paso para crear equipos de agentes de IA colaborativos con el marco CrewAI

Si ha estado explorando el ecosistema de agentes de IA, probablemente conozca el potencial de los sistemas coordinados de múltiples agentes de IA. CrewAI es un marco de código abierto diseñado específicamente para simplificar el desarrollo de estas redes colaborativas de agentes, lo que permite la delegación y ejecución de tareas complejas sin las típicas complicaciones de implementación.

Esta guía lo guiará en la creación de su primer equipo de agentes desde cero, siguiendo nuestro último video tutorial a continuación.


Aprenderás a:

Configure su entorno de desarrollo con CrewAI y sus dependencias
Andamiaje de un nuevo proyecto utilizando nuestras herramientas CLI
Configure sus agentes y tareas a través de definiciones basadas en YAML
Implementar herramientas especializadas para búsquedas web y otras capacidades
Ejecuta a tu tripulación y observa la colaboración entre múltiples agentes en acción
Prerrequisitos
Antes de sumergirse, asegúrese de que su entorno cumpla con estos requisitos:

Gestor de paquetes uv : CrewAI utiliza uv de Astral (creadores de Ruff) para la gestión de dependencias. Este gestor de paquetes ultrarrápido mejora significativamente la velocidad y la fiabilidad de la instalación en comparación con el pip tradicional.
Python : CrewAI requiere Python >3.10 o <3.13 . Verifique su versión:
 python3 --version
Instalación: Configuración de su entorno
1. Instale el administrador de paquetes uv
Elija el método apropiado para su sistema operativo:

macOS / Linux:

 curl -LsSf https://astral.sh/uv/install.sh | sh
Ventanas (PowerShell):

 powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
Verificar la instalación:

 uv --version 
Nota : Para obtener opciones de instalación avanzadas o solución de problemas, consulte la documentación oficial de uv .

2. Instalar la CLI de CrewAI
Con uv listo, instale la interfaz de línea de comandos de CrewAI:

 uv tool install crewai
Si es la primera vez que usas uv tool , es posible que veas un mensaje para actualizar tu PATH . Sigue las instrucciones (normalmente ejecutando uv tool update-shell ) y reinicia tu terminal si es necesario.

Verifique su instalación:

 uv tool list
Debería ver crewai listado con su número de versión (por ejemplo, crewai v0.119.0 ).

Creación de Proyecto: Andamiaje de su primera tripulación
CrewAI ofrece un generador de proyectos estructurado para sentar las bases de tu equipo de agentes. Navega al directorio de proyectos y ejecuta:

 crewai create crew latest-ai-development 
Reemplace latest-ai-development con un nombre descriptivo para su proyecto.

La CLI le solicitará que:

Seleccione un proveedor de LLM : elija su proveedor de modelos de lenguaje grande preferido (OpenAI, Anthropic, Gemini, Ollama, etc.)
Seleccionar un modelo : elija un modelo específico del proveedor (por ejemplo, gpt-4o-mini )
Ingresar claves API : puede agregarlas ahora o más tarde
Estructura del proyecto generada
La CLI crea una estructura de directorio bien organizada:

 latest-ai-development/ ├── .env # Environment variables and API keys ├── .gitignore # Pre-configured to prevent committing # sensitive data ├── pyproject.toml # Project dependencies and metadata ├── README.md # Basic project information ├── knowledge/ # Storage for knowledge files (PDFs, etc.) └── src/ # Main source code └── latest_ai_development/ ├── config/ # YAML configuration files │ ├── agents.yaml │ └── tasks.yaml ├── tools/ # Custom tool implementations │ └── custom_tool.py ├── crew.py # Crew class definition └── main.py # Entry point
Navegue hasta el directorio de su proyecto:

 cd latest-ai-development 
Configuración
Aquí es donde define los agentes y las tareas de su tripulación a través de archivos de configuración YAML.

1. Claves API ( .env )
Abra el archivo .env y agregue sus claves API:

 MODEL=provider/your-preferred-model # eg gemini/gemini-2.5-pro-preview-05-06 <PROVIDER>_API_KEY=your_preffered_provider_api_key SERPER_API_KEY=your_serper_api_key # For web search capability 
Nota de seguridad : Nunca envíe este archivo al control de versiones. El .gitignore generado ya está configurado para excluirlo.

2. Definiciones de agente ( agents.yaml )
Define tus agentes inteligentes en src/<your_project>/config/agents.yaml :

 researcher: role: '{topic} Senior Data Researcher' goal: 'Uncover cutting-edge developments in {topic} with comprehensive research' backstory: 'You are a seasoned researcher with expertise in identifying emerging trends. Your specialty is finding information that others miss, particularly in technical domains.' reporting_analyst: role: '{topic} Reporting Analyst' goal: 'Create detailed, actionable reports based on {topic} research data' backstory: 'You are a meticulous analyst with a talent for transforming raw research into coherent narratives. Your reports are known for their clarity and strategic insights.' 
Variables dinámicas : Tenga en cuenta los marcadores de posición {topic} . Estos se reemplazan dinámicamente en tiempo de ejecución con los valores de su archivo main.py

3. Definiciones de tareas ( tasks.yaml )
Define lo que cada agente debe lograr en src/<your_project>/config/tasks.yaml :

 research_task: description: > Conduct thorough research about {topic}. Focus on: 1. Latest developments (make sure to find information from {current_year}) 2. Key players and their contributions 3. Technical innovations and breakthroughs 4. Challenges and limitations 5. Future directions expected_output: > A list with 10 bullet points covering the most significant findings about {topic}, with emphasis on technical details relevant to developers. agent: researcher reporting_task: description: > Review the research findings and create a comprehensive report on {topic}. Expand each bullet point with supporting evidence, technical explanations, and implementation considerations. expected_output: > A fully fledged technical report with sections covering each major aspect of {topic}. Include code examples where relevant. Format as markdown without code block indicators. agent: reporting_analyst output_file: report.md # Automatically saves output to this file 
4. Integración de herramientas ( crew.py )
Los agentes suelen necesitar herramientas especializadas para interactuar con sistemas externos. Añadamos una función de búsqueda web para nuestro agente investigador:

Primero, importe la herramienta en la parte superior de crew.py :

 from crewai_tools import SerperDevTool
Luego, busque la definición del agente investigador y agregue la herramienta:

 @agent def researcher(self) -> Agent: return Agent( config=self.agents_config['researcher'], tools=[SerperDevTool()], # Enable web search capability verbose=True, llm=self.openai_llm ) 
5. Punto de entrada ( main.py )
Este archivo inicializa su tripulación con parámetros de entrada dinámicos:

 from datetime import datetime # Variables that will be interpolated in your YAML configurations inputs = { 'topic': 'Open source AI agent frameworks', 'current_year': str(datetime.now().year) } # Initialize and run the crew LatestAiDevelopment().crew().kickoff(inputs=inputs) 
Consejo de personalización : ajusta el valor topic para cambiar lo que investiga tu tripulación.

Ejecución: Dirigir a tu tripulación
Con todo configurado, instala las dependencias del proyecto:

 crewai install
Este comando usa uv para instalar y bloquear todas las dependencias definidas en pyproject.toml .

Ahora, ejecuta a tu tripulación:

 crewai run
¡Observa cómo tus agentes cobran vida en tu terminal! Verás:

El agente investigador que utiliza la herramienta SerperDev para buscar información
El agente reporting_analyst que recibe los resultados de la investigación
Ambos agentes trabajan en cooperación para generar el informe final.
Cuando se complete la ejecución, encontrará el archivo de salida ( report.md ) en el directorio de su proyecto, que contiene el informe completo creado por su equipo de IA.

Próximos pasos: Ampliar tus habilidades de CrewAI
¡Felicitaciones por crear tu primer equipo de agentes de IA! Desde aquí, podrás:

Agregue agentes más especializados para diferentes aspectos de su flujo de trabajo
Cree herramientas personalizadas para el acceso a bases de datos, la integración de API o el procesamiento de datos
Experimente con diferentes proveedores de LLM para optimizar el costo o la capacidad
Utilice flujos para procesos de agencia más complejos
Implemente su tripulación utilizando CrewAI Enterprise para entornos de producción.
Siga este tutorial para implementar el proyecto local que acabamos de crear en este blog.

