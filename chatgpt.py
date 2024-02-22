from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.agents import AgentExecutor
tools=[]


class Chatbot():
    def __init__(self):
        self.openaikey="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"
        self.client = OpenAI(api_key=self.openaikey)
    
    def generatereponse(self,user_id:int,question:str,threadid:str=None,model="gpt-4-0125-preview",relation="mother",name="soham")->str:
        '''Generates a response from the chatbot model'''
        threadid=self._getthreadid(user_id)

        agent = OpenAIAssistantRunnable(
            name="Trial streamlit chatbot",
            instructions=f"You are a chatbot that helps users with their queries. You can answer questions, provide information, and help users with their problems. You can also ask questions to get more information",
            tools=tools,
            model=model,
            as_agent=True,
            client=OpenAI(api_key=self.openaikey),
            assistant_id='asst_8sFfdgyNIGM1hs4oZVYkgkUT'
        )
    
        agent_executor = AgentExecutor(agent=agent, tools=tools)
        resp=agent_executor.invoke({"content": f"{question}","thread_id":f"{threadid}",'assistant_id':'asst_8sFfdgyNIGM1hs4oZVYkgkUT'})
        
        return resp

    def _getthreadid(self,userid):
        threadid="thread_yiAHQfGRKbng9lctofsESEWM"
        return threadid
        pass

if __name__ =="__main__":
    chatbot=Chatbot()
    resp=chatbot.generatereponse(123,"What is the capital of India?")
    print(resp)