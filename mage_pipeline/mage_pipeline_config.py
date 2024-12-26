# Mage pipeline setup
import os
from mage_ai.data_preparation.repo_manager import RepoManager
from mage_ai.data_preparation.models.pipeline import Pipeline

# Initialize Mage repository
repo_path = 'mage_pipeline_repo'
os.makedirs(repo_path, exist_ok=True)
RepoManager.init_repo(repo_path)

# Create a new pipeline
pipeline_name = 'bike_demand_prediction'
pipeline = Pipeline.create(pipeline_name, repo_path)

# Add blocks to the pipeline
pipeline.add_block('data_ingestion', 'data_loader')
pipeline.add_block('data_processing', 'transformer', upstream_blocks=['data_ingestion'])
pipeline.add_block('model_training', 'transformer', upstream_blocks=['data_processing'])
pipeline.add_block('batch_prediction', 'transformer', upstream_blocks=['model_training'])
pipeline.add_block('monitoring', 'transformer', upstream_blocks=['batch_prediction'])

# Save pipeline
pipeline.save()

print(f'Pipeline {pipeline_name} created successfully with Mage.')
