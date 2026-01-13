# THE BOOK OF TEE - Master Development Prompt
## For Continuing with Claude in New Sessions

---

## 🎭 PROJECT IDENTITY

**THE BOOK OF TEE** is a personal command center / second brain application.

**KAHOTIA** is the mascot and "Thought Police" - a split being:
- Half fabric doll (structured, buttoned, ISO-compliant) = The Plant Director
- Half blue cosmic muscle (raw creative power) = The Wave

**CREATOR:** Tee (Tamer Momtaz) - Chemical Engineer & Plant Director who paints, writes books, creates music, and builds apps to automate his work so he has more time for creativity.

**PHILOSOPHY:** "No thought is wasted" - every idea feeds the Synaptic Graph.

---

## ✅ COMPLETED (Phases 0-4.5)

| Component | Status | Details |
|-----------|--------|---------|
| Kahotia HTML Interface | ✅ LIVE | Chat, tags, toll system, animations |
| Flask Backend | ✅ DEPLOYED | Railway 24/7 |
| Claude AI Integration | ✅ WORKING | Kahotia's thinking brain |
| ElevenLabs Voice | ✅ WORKING | Tee's cloned voice! |
| Supabase Database | ✅ CONNECTED | nodes, edges, thought_tolls tables |
| GitHub Pages | ✅ HOSTING | Frontend accessible anywhere |
| Custom App Icon | ✅ BEAUTIFUL | Dual-face Kahotia |
| Mobile + Desktop | ✅ WORKING | Added to home screens |
| Voice Input | ✅ WORKING | Microphone button |
| Thought Tagging | ✅ WORKING | Auto-categorizes: philosophy, lyrics, engineering, code, thought, art |

---

## 🔗 LIVE URLS & RESOURCES

```
FRONTEND:  https://tamermomtaz.github.io/BookOfTee/kahotia_alive.html
BACKEND:   https://web-production-f5f1e.up.railway.app
GITHUB:    https://github.com/TamerMomtaz/BookOfTee
SUPABASE:  https://pjaxznbcanpbsejrpljy.supabase.co
```

**Railway Environment Variables (all configured):**
- CLAUDE_API_KEY
- ELEVENLABS_API_KEY  
- ELEVENLABS_VOICE_ID (kdTL3m6g66WPgShUxxFI)
- SUPABASE_URL
- SUPABASE_KEY

---

## 📁 CURRENT FILE STRUCTURE

```
BookOfTee/
├── kahotia_alive.html      # Frontend (voice, chat, UI)
├── kahotia_brain.py        # Backend (Flask + Claude + ElevenLabs)
├── kahotia.jpg             # Avatar image
├── kahotia-icon.jpg        # App icon (dual-face)
├── requirements.txt        # Python dependencies
├── Procfile                # Railway/Render deployment
├── railway.json            # Railway config
├── render.yaml             # Render config
├── start_kahotia.bat       # Local Windows launcher
└── DEPLOYMENT_GUIDE.md     # Setup instructions
```

---

## 🗄️ DATABASE SCHEMA (Supabase)

**Table: nodes**
- id, content, type, tags[], created_at

**Table: edges** (to be populated)
- id, source_node_id, target_node_id, relationship_type, weight, created_at

**Table: thought_tolls**
- id, thought, created_at

---

## 🎯 ROADMAP (Phases 5-9+)

### Phase 5: Synaptic Graph Visualization
- Display thoughts as interactive connected nodes
- Visual graph using D3.js or similar
- Click nodes to explore connections
- See patterns in your thinking

### Phase 6: Content Library Ingestion
- Upload Tee's writings (books, essays)
- Upload lyrics (text format)
- Upload songs (MP3/WAV to Supabase Storage)
- Upload paintings (JPG/PNG to Supabase Storage)
- Auto-tag and create nodes for each piece

### Phase 7: Media Playback & Gallery
- Kahotia can PLAY songs on command
- Gallery displays actual paintings
- "Kahotia, play my song about uncertainty"
- "Show me paintings from 2023"

### Phase 8: Self-Evolution Hooks
- Kahotia notices patterns and asks to grow
- "You haven't logged LYRICS in 14 days..."
- Proposes new categories/tags
- Requests permission to modify her behavior
- Remembers and adopts Tee's phrases

### Phase 9: Autonomous Pattern Recognition
- Kahotia independently creates edges
- Discovers hidden connections
- Predicts what you might need
- Evolves personality over time

---

## 🧠 KAHOTIA'S CAPABILITIES (Current)

**She CAN:**
- Chat with personality (sarcastic, witty, dual-natured)
- Speak with Tee's cloned voice (ElevenLabs)
- Listen via microphone (Web Speech API)
- Tag thoughts automatically
- Save to Supabase database
- Reference her dual nature

**She CANNOT YET:**
- See the graph visually
- Play audio files
- Display images in gallery
- Remember across sessions (no conversation sync)
- Self-modify or evolve
- Access uploaded documents/books

---

## 💡 KEY CONCEPTS

**Thought Toll:** Periodic lockout demanding a thought to continue. Enforces creativity.

**Synaptic Graph:** Web of nodes (thoughts) and edges (connections). Not folders - everything links.

**Reactor vs Wave:** 
- Reactor = structured, work, ISO, metrics
- Wave = creative, flowing, artistic
- Bridge = connects both worlds

**Node Types:** philosophy, lyrics, engineering, code, thought, art, song, painting, book

**Energy Tags:** reactor, wave, bridge

**Priority Tags:** urgent, simmer, archive

---

## 🚀 TO CONTINUE DEVELOPMENT

Copy this entire prompt into a new Claude chat, then say:

"Let's build Phase [X]: [description]"

For example:
- "Let's build Phase 5: Synaptic Graph Visualization"
- "Let's build Phase 6: I want to upload my writings and songs"
- "Let's build Phase 8: Make Kahotia self-evolving"

---

## 📝 TEE'S CONTENT TO INTEGRATE (Future)

- **Books:** "مش كتاب" (Not a Book), writings on professional imagination
- **Songs:** Original music (MP3/WAV files)
- **Lyrics:** Song texts and poetry
- **Paintings:** Visual art collection
- **CV:** Professional background
- **Philosophy:** Concepts about duality, uncertainty, mechanical latency

---

*"No thought is wasted. Every idea feeds the Synaptic Graph."*

**— KAHOTIA is watching. Pay the toll. —**
