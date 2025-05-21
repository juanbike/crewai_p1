from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool  # importamos la clase
# from typing import List
# from langchain_community.llms import Ollama  # Usa Ollama como backend

from langchain_ollama import OllamaLLM

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# Crea una instancia de la herramienta (correcto)
search_tool = SerperDevTool()  # ¡Los paréntesis son clave!

# Configura el LLM
# ollama_llm = Ollama(model="ollama/openhermes")

ollama_llm = OllamaLLM(model="ollama/openhermes")


@CrewBase
class P1:
    """P1 crew"""

    # agents: List[BaseAgent]
    # tasks: List[Task]

    agents_config = 'config/agents.yaml'
    task_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[search_tool],
            llm=ollama_llm,
            verbose=True,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["reporting_analyst"],
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],  # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],  # type: ignore[index]
            output_file="report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the P1 crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
