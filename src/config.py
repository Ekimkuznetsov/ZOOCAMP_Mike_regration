"""
Configuration module for the bike demand prediction pipeline.

This module contains constants and shared configuration settings used across the project.
"""

FEATURE_COLUMNS = [
    "hour",
    "temp",
    "humidity",
    "windspeed",
    "season",
    "weather",
    "workingday",
    "is_weekend",
]

TARGET_COLUMNS = [
    "datetime",
    "casual",
    "count",
    "registered",
    "weekday",
    "is_weekend",
    "season",  # Додано пропущену колонку
]
