import os 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from  langchain.chains import SequentialChain
os.environ["OPENAI_API_KEY"] = ""

llm = OpenAI(temperature = 0.6)

prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template  = 'I want to open a resturante or {cuisine}  food. suggest a fency name for the resturante'
)
name_chain = LLMChain(llm = llm , prompt  = prompt_template_name,output_key = "resturant_name")

prompt_template_items = PromptTemplate(
    input_variables = ['resturant_name'],
    template  = 'suggest some menu items for {resturant_name}. return it as comma seperated values'
)

food_items_chain = LLMChain(llm = llm , prompt  = prompt_template_items,output_key = "menu_items")

chain = SequentialChain(chains = [name_chain , food_items_chain ],
               input_variables = ['cuisine'],
                output_variables = ['resturant_name','menu_items']
                
               )

answer = chain({'cuisine':'Arabic'})

print(answer)




