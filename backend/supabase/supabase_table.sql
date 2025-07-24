🧾 Supabase Tables (SQL Schema)

-- Stores OCR and image scan results
CREATE TABLE ocr_logs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  howl text,
  vision jsonb,
  created_at timestamptz DEFAULT timezone('utc', now())
);

-- Memory logs for assistant and user message threads
CREATE TABLE memory_logs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  thread_id text,
  role text CHECK (role IN ('user', 'assistant')),
  content text,
  created_at timestamptz DEFAULT timezone('utc', now())
);

-- Stores file/image uploads with OCR context
CREATE TABLE file_uploads (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_url text,
  card_name text,
  card_number text,
  meta jsonb,
  created_at timestamptz DEFAULT timezone('utc', now())
);

-- Stores embedded content (vector index base)
CREATE TABLE vector_store (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  namespace text,
  content text,
  embedding vector(1536),
  metadata jsonb,
  created_at timestamptz DEFAULT timezone('utc', now())
);

-- Agent action logs (useful for trace/debug)
CREATE TABLE task_logs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  task_type text,
  agent text,
  payload jsonb,
  result jsonb,
  created_at timestamptz DEFAULT timezone('utc', now())
);
