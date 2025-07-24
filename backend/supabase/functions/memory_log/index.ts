#deno run --allow-net --allow-env --allow-read backend/supabase/functions/memory_log/index.ts
// Import necessary modules
import { serve } from "https://deno.land/std@0.203.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.0.0";
// Create Supabase client
const supabaseUrl = Deno.env.get("SUPABASE_URL") || "";
const supabaseKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") || "";
const supabase = createClient(supabaseUrl, supabaseKey);


// Serve function to handle incoming requests
serve({ port: 8000 }, async (req) => {
  const { howl, vision } = await req.json();
  const { error } = await supabase.from("ocr_logs").insert([{ howl, vision }]);
  if (error) return new Response(JSON.stringify({ error }), { status: 500 });
  return new Response(JSON.stringify({ msg: "Howl received!" }));

})
// Serve the function
console.log("Memory log function is running on port 8000");
// Serve the function
serve({ port: 8000 }, async (req) => {
  const { howl, vision } = await req.json();
  const { error } = await supabase.from("ocr_logs").insert([{ howl, vision }]);
  
  if (error) {
    return new Response(JSON.stringify({ error }), { status: 500 });
  }
  
  return new Response(JSON.stringify({ msg: "Howl received!" }), {
    headers: { "Content-Type": "application/json" },
  });
});
// Log the function is running
console.log("Memory log function is running on port 8000");

// Serve the function
serve({ port: 8000 }, async (req) => {
  const { howl, vision } = await req.json();
  const { error } = await supabase.from("ocr_logs").insert([{ howl, vision }]);
  
  if (error) {
    return new Response(JSON.stringify({ error }), { status: 500 });
  }
  
  return new Response(JSON.stringify({ msg: "Howl received!" }), {
    headers: { "Content-Type": "application/json" },
  });
}); 
// Log the function is running
console.log("Memory log function is running on port 8000");
// Log the function is running