create_table_queries = [

"""
CREATE EXTENSION if not exists vector;
""",

"""
CREATE TABLE IF NOT EXISTS CIDs (
    cid      VARCHAR PRIMARY KEY,
    content  TEXT
)
""",

"""
CREATE TABLE IF NOT EXISTS youtube_metadata (
    id         VARCHAR PRIMARY KEY,
    metadata   JSON
)
""",

"""
CREATE TABLE IF NOT EXISTS youtube_transcripts (
    id              VARCHAR PRIMARY KEY,
    text_transcript TEXT,
    json_transcript JSON
)
""",

"""
CREATE TABLE IF NOT EXISTS messages_vectors_bert_t (
  id                   SERIAL PRIMARY KEY,
  yt_video_id          VARCHAR,
  yt_video_creator     VARCHAR,
  chunking_id          VARCHAR,
  chunking_incrementer INTEGER,
  content              VARCHAR,
  embedding_model      VARCHAR,
  embedding            vector
);
"""

]
