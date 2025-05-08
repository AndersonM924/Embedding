import { serve } from "https://deno.land/std@0.177.0/http/server.ts"

serve(async (req: Request) => {
  try {
    const body = await req.json()
    const rawText = body.rawText || body.text || body.summary || body.perfil

    if (!rawText || typeof rawText !== "string") {
      return new Response(JSON.stringify({ error: "Falta el campo rawText o no es texto válido." }), { status: 400 })
    }

    const apiKey = Deno.env.get("GEMINI_API_KEY")
    if (!apiKey) {
      return new Response(JSON.stringify({ error: "Falta la variable GEMINI_API_KEY" }), { status: 500 })
    }

    const response = await fetch(
      "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedText?key=" + apiKey,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: rawText,
          taskType: "RETRIEVAL_DOCUMENT"
        })
      }
    )

    const result = await response.json()

    if (!response.ok || !result.embedding?.values) {
      return new Response(JSON.stringify({ error: result }), { status: 500 })
    }

    return new Response(JSON.stringify({ embedding: result.embedding.values }), {
      headers: { "Content-Type": "application/json" }
    })

  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500 })
  }
})
