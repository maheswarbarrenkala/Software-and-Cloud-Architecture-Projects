import os

def get_secret(path, key):
    # Mock implementation of get_secret for illustration purposes
    # Replace this with the actual logic to retrieve secrets
    return f'secret_value_for_{key}'

class Config:
    # Kafka Configuration
    KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'your-kafka-endpoint')

    # AWS S3 Configuration
    S3_BUCKET = os.getenv('S3_BUCKET', 'your-s3-bucket')
    S3_ACCESS_KEY = get_secret('aws/s3', 'access_key')
    S3_SECRET_KEY = get_secret('aws/s3', 'secret_key')

    # MongoDB Configuration
    MONGO_HOST = os.getenv('MONGO_HOST', 'your-mongo-endpoint')
    MONGO_USER = get_secret('database/mongo', 'username')
    MONGO_PASSWORD = get_secret('database/mongo', 'password')
    MONGO_DB = os.getenv('MONGO_DB', 'your-mongo-database')

        
    # Cassandra Configuration
    CASSANDRA_HOST = os.getenv('CASSANDRA_HOST', 'your-cassandra-endpoint')
    CASSANDRA_USER = get_secret('database/cassandra', 'username')
    CASSANDRA_PASSWORD = get_secret('database/cassandra', 'password')

    # Amazon RDS Configuration
    RDS_HOST = os.getenv('RDS_HOST', 'your-rds-endpoint')
    RDS_USER = get_secret('database/rds', 'username')
    RDS_PASSWORD = get_secret('database/rds', 'password')
    RDS_DB = os.getenv('RDS_DB', 'your-rds-database')

    # Elasticsearch Configuration
    ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'your-elasticsearch-endpoint')


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False