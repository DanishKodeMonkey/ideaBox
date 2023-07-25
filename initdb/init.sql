-- init.sql

-- Create the database
CREATE DATABASE idea_box;

-- Connect to the database
\c idea_box;

-- Create the table for ideas
CREATE TABLE ideas (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL
);