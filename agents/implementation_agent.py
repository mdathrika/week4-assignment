from base_agent import Agent

IMPLEMENTATION_PROMPT = """
You are an experienced software engineer is tasked to implement the milestone and \
    output the result in HTML, CSS, or markdown format. \

Mark the milestone as complete by checking the box next to it in the plan. 
"""
class ImplementationAgent(Agent):
    def __init__(self, name, client, prompt, gen_kwargs=None):
        super().__init__(name, client, IMPLEMENTATION_PROMPT, gen_kwargs)

    def perform_task(self, task):
        # Implement the task logic here
        print(f"{self.name} is performing task: {task}")