import os

def get_secret(path, key):
    # Mock implementation of get_secret for illustration purposes
    # Replace this with the actual logic to retrieve secrets
    return f'secret_value_for_{key}'

class Config:
    # Kafka Configuration
    KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'your-kafka-endpoint')


    # Amazon RDS Configuration
    RDS_HOST = os.getenv('RDS_HOST', 'your-rds-endpoint')
    RDS_USER = get_secret('database/rds', 'username')
    RDS_PASSWORD = get_secret('database/rds', 'password')
    RDS_DB = os.getenv('RDS_DB', 'your-rds-database')


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False