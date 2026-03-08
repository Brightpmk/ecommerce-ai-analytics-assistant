from app.config import Config

print("DB_HOST:", Config.DB_HOST)
print("DB_PORT:", Config.DB_PORT)
print("DB_NAME:", Config.DB_NAME)
print("MODEL_NAME:", Config.MODEL_NAME)
print("API KEY EXISTS:", bool(Config.OPENAI_API_KEY))