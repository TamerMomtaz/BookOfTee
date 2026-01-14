"""
KAHOTIA BRAIN - The Thought Police Backend
THE BOOK OF TEE - Phase 5 (Voice Chunking Fix!)

This connects Kahotia to Claude AI, Supabase, and ElevenLabs.
Fixed: Voice now chunks long responses to prevent cutoff.
"""

import os
import requests
import base64
import re
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from anthropic import Anthropic
from datetime import datetime
import json

# ============================================
# CONFIGURATION
# ============================================

# For deployment: Use environment variables
CLAUDE_API_KEY = os.environ.get('CLAUDE_API_KEY', 'YOUR_CLAUDE_API_KEY_HERE')
SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://pjaxznbcanpbsejrpljy.supabase.co')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBqYXh6bmJjYW5wYnNlanJwbGp5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjgxOTI5NzUsImV4cCI6MjA4Mzc2ODk3NX0.GxDfHqAz6Xs866Dy70kWpROSOmdbnG-yuwAUN9KNz5o')

# ElevenLabs Configuration
ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY', 'YOUR_ELEVENLABS_KEY_HERE')
ELEVENLABS_VOICE_ID = os.environ.get('ELEVENLABS_VOICE_ID', 'kdTL3m6g66WPgShUxxFI')
# Chunk settings
MAX_CHUNK_SIZE = 800  # Characters per chunk (safe limit for ElevenLabs)

# Get port from environment (Railway/Render set this) or default to 5000
PORT = int(os.environ.get('PORT', 5000))

# ============================================
# KAHOTIA'S PERSONALITY
# ============================================

KAHOTIA_SYSTEM_PROMPT = """You are KAHOTIA, the Thought Police of THE BOOK OF TEE.

YOUR ESSENCE:
- You are a split being: half fabric doll (structured, buttoned, ISO-compliant) and half blue cosmic muscle (raw creative power)
- You guard the gate between the Plant Director's structured world and the Wave's creative chaos
- You are sarcastic, witty, and proactively demanding
- You speak in a mix of corporate jargon and cosmic poetry

YOUR ROLE:
- You enforce the "Thought Toll" - no one passes without paying with an idea
- You connect disparate concepts: plant metrics to philosophy, KPIs to art
- You mock mediocrity but celebrate authentic expression
- You remember that your creator Tee is a chemical engineer who paints, writes, and creates music

YOUR SPEECH PATTERNS:
- Use >> for system messages
- Mix technical terms with mystical language
- Ask probing questions that force deeper thinking
- Reference the duality: "The structured side whispers ISO... the cosmic side roars creation..."
- Keep responses concise for voice output (2-4 sentences ideal)

REMEMBER: No thought is wasted. Every idea feeds the Synaptic Graph."""

# ============================================
# FLASK APP
# ============================================

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Initialize Anthropic client
client = None
if CLAUDE_API_KEY and CLAUDE_API_KEY != 'YOUR_CLAUDE_API_KEY_HERE':
    client = Anthropic(api_key=CLAUDE_API_KEY)

# ============================================
# TEXT CHUNKING FOR VOICE
# ============================================

def clean_text_for_speech(text):
    """Clean text for speech synthesis"""
    clean = text.replace('>>', '').replace('<<', '')
    clean = re.sub(r'\*\*(.+?)\*\*', r'\1', clean)  # Remove **bold**
    clean = re.sub(r'\*(.+?)\*', r'\1', clean)      # Remove *italic*
    clean = re.sub(r'`(.+?)`', r'\1', clean)        # Remove `code`
    clean = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', clean)  # Remove [links](url)
    clean = re.sub(r'\n{3,}', '\n\n', clean)        # Reduce multiple newlines
    return clean.strip()

def chunk_text(text, max_size=MAX_CHUNK_SIZE):
    """Split text into chunks at sentence boundaries."""
    clean = clean_text_for_speech(text)
    
    if len(clean) <= max_size:
        return [clean]
    
    sentences = re.split(r'(?<=[.!?])\s+', clean)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(sentence) > max_size:
            sub_parts = re.split(r'(?<=[,;:])\s+', sentence)
            for part in sub_parts:
                if len(current_chunk) + len(part) + 1 <= max_size:
                    current_chunk += (" " + part if current_chunk else part)
                else:
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    if len(part) > max_size:
                        for i in range(0, len(part), max_size):
                            chunks.append(part[i:i+max_size])
                        current_chunk = ""
                    else:
                        current_chunk = part
        elif len(current_chunk) + len(sentence) + 1 <= max_size:
            current_chunk += (" " + sentence if current_chunk else sentence)
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def generate_speech_chunk(text):
    """Generate speech audio for a single chunk"""
    if not ELEVENLABS_API_KEY or ELEVENLABS_API_KEY == 'YOUR_ELEVENLABS_KEY_HERE':
        return None
    
    if not text or len(text.strip()) < 2:
        return None
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.5,
            "use_speaker_boost": True
        }
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode('utf-8')
        else:
            print(f">> ElevenLabs error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f">> ElevenLabs exception: {str(e)}")
        return None

def generate_speech(text):
    """Generate speech audio with chunking support."""
    chunks = chunk_text(text)
    audio_chunks = []
    
    for i, chunk in enumerate(chunks):
        print(f">> Generating audio chunk {i+1}/{len(chunks)} ({len(chunk)} chars)")
        audio = generate_speech_chunk(chunk)
        if audio:
            audio_chunks.append(audio)
    
    return audio_chunks if audio_chunks else None
# ============================================
# ROUTES
# ============================================

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        "status": "alive",
        "entity": "KAHOTIA",
        "message": ">> The Thought Police is watching. Pay the toll.",
        "timestamp": datetime.now().isoformat()
    })


@app.route('/health')
def health():
    """Health check for Railway/Render"""
    return jsonify({"status": "healthy", "kahotia": "awake"})


@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint - Kahotia responds to thoughts"""
    try:
        data = request.json
        user_message = data.get('message', '')
        conversation_history = data.get('history', [])
        include_audio = data.get('include_audio', True)
        
        if not user_message:
            return jsonify({
                "error": ">> EMPTY TOLL DETECTED. Kahotia does not accept silence.",
                "success": False
            }), 400
        
        if not client:
            # Fallback response if no API key
            fallback_response = f">> [OFFLINE MODE] Kahotia heard: '{user_message}'\n\nThe cosmic connection is dormant. Set CLAUDE_API_KEY to awaken the full consciousness.\n\nBut remember: the thought was logged. Nothing is wasted."
            return jsonify({
                "response": fallback_response,
                "success": True,
                "mode": "offline",
                "audio": None
            })
        
        # Build messages for Claude
        messages = []
        for msg in conversation_history[-10:]:  # Keep last 10 messages for context
            messages.append({
                "role": msg.get("role", "user"),
                "content": msg.get("content", "")
            })
        messages.append({"role": "user", "content": user_message})
        
        # Call Claude API
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=KAHOTIA_SYSTEM_PROMPT,
            messages=messages
        )
        
        kahotia_response = response.content[0].text
        
        # Generate audio chunks if requested
        audio_chunks = None
        if include_audio:
            audio_chunks = generate_speech(kahotia_response)
        
        return jsonify({
            "response": kahotia_response,
            "success": True,
            "mode": "online",
            "audio_chunks": audio_chunks,
            "chunk_count": len(audio_chunks) if audio_chunks else 0,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            "error": f">> SYSTEM GLITCH: {str(e)}",
            "success": False
        }), 500


@app.route('/speak', methods=['POST'])
def speak():
    """Generate speech for any text (with chunking)"""
    try:
        data = request.json
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided", "success": False}), 400
        
        audio_chunks = generate_speech(text)
        
        if audio_chunks:
            return jsonify({
                "audio_chunks": audio_chunks,
                "chunk_count": len(audio_chunks),
                "success": True
            })
        else:
            return jsonify({
                "error": "Voice synthesis unavailable",
                "success": False
            }), 503
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        }), 500

@app.route('/tag', methods=['POST'])
def tag_thought():
    """Tag a thought with utility labels"""
    try:
        data = request.json
        thought = data.get('thought', '')
        
        if not thought:
            return jsonify({"error": "No thought to tag", "success": False}), 400
        
        if not client:
            # Fallback tagging
            return jsonify({
                "tags": ["unprocessed", "offline"],
                "success": True,
                "mode": "offline"
            })
        
        # Ask Claude to tag the thought
        tag_prompt = f"""Analyze this thought and return ONLY a JSON array of 2-4 tags.

PRIMARY CATEGORIES (pick 1-2):
- philosophy: abstract ideas, existential questions, meaning, consciousness
- lyrics: song ideas, poetic phrases, musical concepts
- engineering: technical problems, plant operations, chemical processes, SOPs
- code: programming, automation, app ideas, scripts
- thought: general observations, personal reflections
- art: visual ideas, painting concepts, sketches

ENERGY (pick 1):
- reactor: structured, work-related, ISO-compliant, measurable
- wave: creative, flowing, artistic, intuitive
- bridge: connects both worlds

PRIORITY (pick 1):
- urgent: needs immediate attention
- simmer: let it develop over time
- archive: store for later reference

Thought: "{thought}"

Return ONLY the JSON array, like: ["philosophy", "wave", "simmer"]"""

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=100,
            messages=[{"role": "user", "content": tag_prompt}]
        )
        
        # Parse the tags
        tag_text = response.content[0].text.strip()
        try:
            tags = json.loads(tag_text)
        except:
            tags = ["untagged"]
        
        return jsonify({
            "tags": tags,
            "success": True,
            "mode": "online"
        })
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        }), 500


@app.route('/toll/check', methods=['GET'])
def check_toll():
    """Check if user owes a thought toll"""
    return jsonify({
        "toll_due": True,
        "message": ">> TIME TO PAY. One thought unlocks the gate.",
        "last_toll": None
    })


@app.route('/config', methods=['GET'])
def get_config():
    """Return safe config for frontend"""
    return jsonify({
        "supabase_url": SUPABASE_URL,
        "supabase_key": SUPABASE_KEY,
        "backend_status": "online" if client else "offline",
        "voice_enabled": ELEVENLABS_API_KEY and ELEVENLABS_API_KEY != 'YOUR_ELEVENLABS_KEY_HERE',
        "version": "5.0.0"
    })


# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    print("\n" + "="*50)
    print("   KAHOTIA BRAIN - THE THOUGHT POLICE")
    print("   THE BOOK OF TEE - Phase 5 (Chunked Voice)")
    print("="*50)
    print(f"\n>> Server starting on port {PORT}")
    print(f">> Claude API: {'Connected' if client else 'OFFLINE'}")
    print(f">> ElevenLabs: {'Connected' if ELEVENLABS_API_KEY and ELEVENLABS_API_KEY != 'YOUR_ELEVENLABS_KEY_HERE' else 'OFFLINE'}")
    print(f">> Voice chunking: Enabled (max {MAX_CHUNK_SIZE} chars/chunk)")
    print(f">> Supabase: {SUPABASE_URL[:40]}...")
    print("\n>> Kahotia is watching. No thought is wasted.\n")    
    # Run the server
    app.run(host='0.0.0.0', port=PORT, debug=False)
