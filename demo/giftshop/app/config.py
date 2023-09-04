import openai

class Config:
    openai_key = "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"
    serpapi_key = "85e533d13902cae321b126805920538fda1efed6a10c8fab426489eb4889989d"
    
    @staticmethod
    def get_openai_key():
        return Config.openai_key
    
    @staticmethod
    def get_serpapi_key():
        return Config.serpapi_key


